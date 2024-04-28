'''
same letters - we can do it by set
abcde -> aecdb 1st case letters are same but jumbled - we can so it using a hash map 
aacabb ->bbcbaa -> a:3; b:3 - > values
'''
def closeStr(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1Set,s2Set = set(s1),set(s2)
    if s1Set != s2Set:
        return False
    freqs1,freqs2 = {},{}
    for str in s1:
        freqs1[str] = freqs1.get(str,0)+1
    for str2 in s2:    
        freqs2[str2] = freqs2.get(str2,0)+1
    if freqs1.values()!=freqs2.values():
        return False
    print(s1Set,s2Set,freqs1,freqs2,set(freqs1.values()),set(freqs2.values()))
    return True



print(closeStr("aaabbbbccddeeeeefffff","aaaaabbcccdddeeeeffff"))
