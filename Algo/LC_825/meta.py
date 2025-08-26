class metaDb:
    def __init__(self):
        self.store  = {}
    def set(self, key, value, now, ttl=None):
        expire_ts = None if ttl is None else now + ttl
        self.store.setdefault(key,[]).append([now,value,expire_ts,False])
    def get(self,key,now):
        return self.get_at(key,now)
    def get_at(self,key,t):
        versions = self.store.get(key,[])
        for write_ts, value, expire_ts, isDeleted in reversed(versions):
            if write_ts<=t:
                if isDeleted:
                    return None
                if expire_ts is None or t<expire_ts:
                    return value
        return None
    def delete(self, key, now):
        self.store.setdefault(key,[]).append([now,None,None,True])

db = metaDb()

# Stage 1: set/get + overwrite
db.set("a", "A1", now=1)
assert db.get("a", now=1) == "A1"
db.set("a", "A2", now=2)
assert db.get("a", now=2) == "A2"
assert db.get_at("a", t=1) == "A1"

# Stage 2: TTL (exclusive)
db.set("b", "B1", now=10, ttl=2)   # expires at 12, visible at t=10,11
assert db.get("b", now=10) == "B1"
assert db.get("b", now=11) == "B1"
assert db.get("b", now=12) is None  # expired exactly at 12

# Stage 3: PIT gaps & boundaries
db.set("c", "C1", now=20)
db.set("c", "C2", now=25)
assert db.get_at("c", 19) is None
assert db.get_at("c", 20) == "C1"
assert db.get_at("c", 24) == "C1"
assert db.get_at("c", 25) == "C2"

# Stage 4: delete semantics
db.delete("c", now=30)
assert db.get("c", now=30) is None          # tombstoned now
assert db.get_at("c", 25) == "C2"           # pre-delete still visible

# TTL + delete interplay
db.set("d", "D1", now=40, ttl=3)            # expires at 43
db.delete("d", now=41)
assert db.get("d", now=41) is None          # deleted
assert db.get_at("d", 40) == "D1"           # before delete
assert db.get_at("d", 43) is None           # expired at 43
print("basic sanity OK")
                
        