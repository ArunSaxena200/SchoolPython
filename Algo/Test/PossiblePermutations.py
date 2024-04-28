'''
1,2,3

start = 0,1; 0,2; 0,3


'''

def permute(nums):
    res = []
    def backtrack(start):
        #base
        if start == len(nums):
            res.append(nums[:])
            return
        for i in range(start,len(nums)):
            nums[start],nums[i] = nums[i],nums[start]
            backtrack(start+1)
            nums[start],nums[i] = nums[i],nums[start]
    backtrack(0)
    return res

print(permute([1,2,3,4]))
