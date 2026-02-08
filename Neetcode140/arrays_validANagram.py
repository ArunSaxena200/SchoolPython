"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

def va(s,t):
    count= {}

    for chr in s:
        count[chr] = count.get(chr,0)+1
    
    for chr in t:
        if chr not in count:
            return False
        count[chr]-=1
        print(count)
        
        if count[chr]<0:
            return False
    return True

    print(count)
s,t = "ab", "a"

print(va(s,t))
