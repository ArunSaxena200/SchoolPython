def digitPerm(digits):
    '''
    423 - 432,234,243,342,324
    '''
    res = []
    def backtrack(index,combination):
        #base case
        if index == len(digits):
            res.append(combination)
            return
    
        for nums in digits:
            if nums not in combination: #avoid same numbers permutations
                backtrack(index+1,combination+nums)
    backtrack(0,'')
    return res



print(digitPerm('423'))