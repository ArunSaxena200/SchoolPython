'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
''' 
def longestPalindrome(s):
    length = 0
    res = ""
    for i in range(len(s)):
        left = i
        right = i
        while left >=0 and right < len(s) and s[left]==s[right]:
            
            if (right-left + 1)>length:
                length = right - left +1
                res = s[left:right+1]

            left = left -1
            right = right +1
        left = i
        right = i+1
        while left >=0 and right < len(s) and s[left]==s[right]:
            
            if (right-left + 1)>length:
                length = right - left +1
                res = s[left:right+1]

            left = left -1
            right = right +1
    return res

print(longestPalindrome("cbbd"))