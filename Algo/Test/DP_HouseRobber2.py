'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''

def hb2(inpArray):
    return max(inpArray[0],helper(inpArray[1:]),helper(inpArray[:-1]))

def helper(inpArray):
    rob1,rob2 = 0,0
    for i in inpArray:
        temp = max(rob1 + i, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(hb2([2,3,2]))