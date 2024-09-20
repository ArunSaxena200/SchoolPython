import re
def betterCompression(s):
    s = s.lower()
    if not s:
        return ''
    
    
    freqChar = {}

    for char,val in re.findall(r'([a-z])(\d+)',s):
        if char in freqChar:
            freqChar[char] += int(val)
        else:
            freqChar[char] = int(val)
    
    
    sortedChar = sorted(freqChar)

    return "".join(f'{char}{freqChar[char]}' for char in sortedChar)

def decompressed(d):
    res = []
    for char,val in re.findall(r'([a-z])(\d+)',d):
        res.append(char*int(val))
    print(res)
    return "".join(res)

compressed = betterCompression("a3c9b2c1")
print(compressed)
print(decompressed(compressed))  # Output: "aaabccccc"
