"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

def input(s1,s2):
    m =len(s1)
    n= len(s2)
    window = [0]*26
    need = [0]*26

    if m>n:
        return False
    for char in s1:
        need[ord(char)-ord('a')]+=1
    for i in range(m):
        window[ord(s2[i])-ord('a')]+=1
    if window == need:
        return True
    
    for i in range(m,n):
        window[ord(s2[i])- ord('a')]+=1
        window[ord(s2[i-m])- ord('a')]-=1
        if window == need:
            return True
    return False


    
s1 = "ab" 
s2 = "eidbaooo"
print(input(s1,s2))


