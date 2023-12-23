def product(nums):
    '''
    [1,2,0,4,5]


    '''
    mul = 1
    index = 0
    zero = 0

    for i in range(len(nums)):
        if nums[i] !=0:
            mul = mul*nums[i]
        elif nums[i] ==0:
            zero = zero+1
    if zero == len(nums):
        mul = 0
         
    for j in range(len(nums)):
        if zero>=1 and nums[j]!=0:
            nums[j]=0
        elif zero>=1 and nums[j]==0:
            nums[j]=mul
        elif nums[j]!=0:
            nums[j] = int(mul/nums[j])

            #index = index +1
    print(nums)

product([-1,1,0,-3,3]
)