'''
345
354

'''


def permSum(nums):
    res = []
    def backtrack(levels):
        # base case
        if levels==len(nums):
            print("inside",levels)
            res.append(nums[:])
            return
        #iteration
        for i in range(levels,len(nums)):
            print("level and i",levels,i)
            nums[levels],nums[i]= nums[i],nums[levels]
            print(nums)
            backtrack(levels+1)
            nums[levels],nums[i]= nums[i],nums[levels]
    backtrack(0)
    return res

print(permSum(['a','b','c']))


