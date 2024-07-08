from collections import Counter
def betterCompression(compressed: str):
    # Create a hash map counter object
    cnt = Counter()
    # Initiate the iterator variables
    i, n = 0, len(compressed)
    while i < n:
        j = i + 1
        x = 0
        while j < n and compressed[j].isdigit():
            x = x * 10 + int(compressed[j])
            print("j",j,"x=",x)
            j += 1
        cnt[compressed[i]] += x
        print("cnt=",cnt)
        i = j
    return "".join(sorted(f"{k}{v}" for k, v in cnt.items()))
    
print(betterCompression("a12b56c1a105"))