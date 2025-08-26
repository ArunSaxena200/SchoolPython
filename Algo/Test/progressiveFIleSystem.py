# Simple, readable implementation of the file hosting service

from typing import Optional, List, Tuple

class SimpleFS:
    def __init__(self):
        # files[name] = {"size": int, "created": int, "ttl": int|None}
        self.files = {}
        # history = list of events for rollback replay
        # each event: {"ts": int, "op": "UPLOAD"|"COPY", ...}
        self.history = []

    # ---------- tiny helpers ----------
    def _alive(self, ts: int, name: str) -> bool:
        """Is file 'name' alive (not expired) at time ts?"""
        meta = self.files.get(name)
        if not meta:
            return False
        if meta["ttl"] is None:
            return True
        return ts < meta["created"] + meta["ttl"]

    def _sweep(self, ts: int) -> None:
        """Remove any expired files at time ts."""
        to_delete = []
        for name, meta in self.files.items():
            if meta["ttl"] is not None and ts >= meta["created"] + meta["ttl"]:
                to_delete.append(name)
        for name in to_delete:
            del self.files[name]

    def _remaining_ttl(self, ts: int, meta: dict) -> Optional[int]:
        """Remaining seconds of life at ts (or None if infinite)."""
        if meta["ttl"] is None:
            return None
        remain = (meta["created"] + meta["ttl"]) - ts
        return max(0, remain)

    # ---------- Level 1 (simple versions call the *_AT with ts=0) ----------
    def FILE_UPLOAD(self, file_name: str, size: int) -> None:
        self.FILE_UPLOAD_AT(0, file_name, size)

    def FILE_GET(self, file_name: str) -> Optional[int]:
        return self.FILE_GET_AT(0, file_name)

    def FILE_COPY(self, source: str, dest: str) -> None:
        self.FILE_COPY_AT(0, source, dest)

    def FILE_SEARCH(self, prefix: str) -> List[Tuple[str, int]]:
        return self.FILE_SEARCH_AT(0, prefix)

    # ---------- Level 3: time-aware versions with TTL ----------
    def FILE_UPLOAD_AT(self, timestamp: int, file_name: str, file_size: int, ttl: Optional[int] = None) -> None:
        self._sweep(timestamp)
        if self._alive(timestamp, file_name):
            raise RuntimeError("File already exists")
        self.files[file_name] = {"size": file_size, "created": timestamp, "ttl": ttl}
        self.history.append({"ts": timestamp, "op": "UPLOAD", "name": file_name, "size": file_size, "ttl": ttl})

    def FILE_GET_AT(self, timestamp: int, file_name: str) -> Optional[int]:
        self._sweep(timestamp)
        return self.files[file_name]["size"] if self._alive(timestamp, file_name) else None

    def FILE_COPY_AT(self, timestamp: int, file_from: str, file_to: str) -> None:
        self._sweep(timestamp)
        if not self._alive(timestamp, file_from):
            raise RuntimeError("Source file does not exist")
        src = self.files[file_from]
        # Copy inherits remaining TTL (None means infinite)
        rem = self._remaining_ttl(timestamp, src)
        ttl_for_dest = None if rem is None else rem
        self.files[file_to] = {"size": src["size"], "created": timestamp, "ttl": ttl_for_dest}
        self.history.append({"ts": timestamp, "op": "COPY", "src": file_from, "dst": file_to})

    def FILE_SEARCH_AT(self, timestamp: int, prefix: str) -> List[Tuple[str, int]]:
        self._sweep(timestamp)
        # alive + startswith(prefix)
        items = [(name, meta["size"])
                 for name, meta in self.files.items()
                 if name.startswith(prefix) and self._alive(timestamp, name)]
        # Order by size DESC, then name ASC; top 10
        items.sort(key=lambda x: (-x[1], x[0]))
        return items[:10]

    # ---------- Level 4: rollback ----------
    def ROLLBACK(self, timestamp: int) -> None:
        """
        Rebuild the state as of 'timestamp', and reset TTLs so each file
        has only its remaining lifetime from that point forward.
        """
        # 1) Replay history up to 'timestamp' into a fresh FS
        fresh = SimpleFS()
        for ev in sorted(self.history, key=lambda e: e["ts"]):
            if ev["ts"] > timestamp:
                break
            if ev["op"] == "UPLOAD":
                fresh.FILE_UPLOAD_AT(ev["ts"], ev["name"], ev["size"], ev["ttl"])
            elif ev["op"] == "COPY":
                # Only copy if source exists/alive at that moment
                if fresh._alive(ev["ts"], ev["src"]):
                    fresh.FILE_COPY_AT(ev["ts"], ev["src"], ev["dst"])

        # 2) Remove anything already expired by 'timestamp'
        fresh._sweep(timestamp)

        # 3) Recalculate TTLs to remaining-from-rollback
        for name in list(fresh.files.keys()):
            meta = fresh.files[name]
            if meta["ttl"] is None:
                # infinite: keep as-is but set created to rollback time (clean mental model)
                fresh.files[name] = {"size": meta["size"], "created": timestamp, "ttl": None}
            else:
                remain = fresh._remaining_ttl(timestamp, meta)
                if remain <= 0:
                    del fresh.files[name]
                else:
                    fresh.files[name] = {"size": meta["size"], "created": timestamp, "ttl": remain}

        # 4) Replace current state and trim history
        self.files = fresh.files
        self.history = [ev for ev in self.history if ev["ts"] <= timestamp]


# ------------------- Minimal demo -------------------
if __name__ == "__main__":
    fs = SimpleFS()

    # Level 1
    fs.FILE_UPLOAD("file-1.zip", 4321)
    print("GET file-1.zip ->", fs.FILE_GET("file-1.zip"))  # 4321
    fs.FILE_COPY("file-1.zip", "dir-a/file-1-copy.zip")
    print("SEARCH 'file' ->", fs.FILE_SEARCH("file"))

    # Level 3 (time + TTL)
    fs.FILE_UPLOAD_AT(10, "dir-a/dir-c/file-2.txt", 1100, ttl=20)  # lives 10..30
    fs.FILE_UPLOAD_AT(12, "dir-a/dir-c/file-3.csv", 2122)          # infinite
    fs.FILE_UPLOAD_AT(15, "dir-b/file-4.mdx", 3378, ttl=10)        # lives 15..25

    print("GET_AT t=20 file-2 ->", fs.FILE_GET_AT(20, "dir-a/dir-c/file-2.txt"))  # 1100
    print("GET_AT t=35 file-2 ->", fs.FILE_GET_AT(35, "dir-a/dir-c/file-2.txt"))  # None (expired)

    fs.FILE_COPY_AT(22, "dir-b/file-4.mdx", "dir-b/file-4-copy.mdx")  # remaining ttl ~3s
    print("GET_AT t=23 file-4-copy ->", fs.FILE_GET_AT(23, "dir-b/file-4-copy.mdx"))  # 3378
    print("GET_AT t=30 file-4-copy ->", fs.FILE_GET_AT(30, "dir-b/file-4-copy.mdx"))  # None (expired)

    print("SEARCH_AT t=20 'dir-a/dir-c/' ->", fs.FILE_SEARCH_AT(20, "dir-a/dir-c/"))
    # [('dir-a/dir-c/file-3.csv', 2122), ('dir-a/dir-c/file-2.txt', 1100)]

    # Level 4 (rollback)
    fs.ROLLBACK(22)
    print("After ROLLBACK(22):")
    print("GET_AT t=23 file-2 ->", fs.FILE_GET_AT(23, "dir-a/dir-c/file-2.txt"))  # 1100
    print("GET_AT t=31 file-2 ->", fs.FILE_GET_AT(31, "dir-a/dir-c/file-2.txt"))  # None (expired)
