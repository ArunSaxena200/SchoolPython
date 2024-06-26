def permute(nums):
    res = []
    def backtrack(start):
        # base case
        if start == len(nums):
            res.append(nums[:])
        # iteration
        for i in range(start,len(nums)):
            nums[start],nums[i] = nums[i],nums[start]
            backtrack(start+i)
            nums[start],nums[i] = nums[i],nums[start]

    backtrack(0)
    return res

print(permute([1,2,3]))

