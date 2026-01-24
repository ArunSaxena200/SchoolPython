"""
Given a string s, find the length of the longest substring without duplicate characters.

"""
def longestSubSeq(chars):
    left =0
    seen = {}
    best = 0

    for i in range(len(chars)):
        c = chars[i]
        if c in seen and seen[c]>=left:
            left = seen[c]+1
        seen[c] = i
        best = max(best,i-left+1)
    return best


s = "ssssssssssssssssssssss"
print(longestSubSeq(s))  # Expected: 3 ("abc")