def robber(inpArray):
    '''
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
        connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

        

        Example 1:

        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
        rob1,rob2,n,n+1,n+2,....

    '''
    rob1=0
    rob2=0

    for num in inpArray:
        print(num)
        n= max( rob1+num, rob2)
        rob1=rob2 # this will always be the 
        rob2=n # this will alwyas be the max of all the robs other than the current num
    return rob2

print(robber([1,2,3,1]))