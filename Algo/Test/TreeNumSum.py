def threeNumSum(input,targetSum):

    '''
    [1,2,3,4,5] 11
    '''
    input.sort()
    result = []
    for i in range(len(input)):
        left = i + 1
        right = len(input) -1 
        while left < right:
            if input[i]+ input[left] + input[right] < targetSum:
                left = left +1 
            elif input[i]+ input[left] + input[right] > targetSum:
                right = right -1
            elif input[i]+ input[left] + input[right] == targetSum:
                #left = left + 1
                #right = right -1
                result.append([input[i],input[left],input[right]])
                left = left + 1
                right = right -1
    return result

print(threeNumSum([1,2,3,4,5,6], 11))



