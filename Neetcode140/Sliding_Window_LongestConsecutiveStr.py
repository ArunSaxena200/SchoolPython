"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""
def longestStringReplacement(string):
	# This function returns another function that solves the problem
	def solution(s, k):
		count = {}  # Dictionary to count each character in the window
		maxf = 0    # Max frequency of a single character in the window
		left = 0    # Left pointer of the window
		res = 0     # Result: max length found
		for right in range(len(s)):
			char = s[right]  # Current character
			count[char] = count.get(char, 0) + 1  # Add to count
			maxf = max(maxf, count[char])  # Update max frequency
			# If we need to change more than k chars, move left pointer
			while (right - left + 1) - maxf > k:
				left_char = s[left]  # Char at left pointer
				count[left_char] -= 1  # Remove from count
				left += 1  # Move left pointer right
			res = max(res, right - left + 1)  # Update result if bigger window
		return res  # Return the answer
	return solution  # Return the function
    
