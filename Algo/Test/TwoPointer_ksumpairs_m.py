def ksum(input,targetsum):
    '''
    [1,2,3,4]
    5
    6
    '''
    left = 0 
    right = len(input) -1
    res = []
    count = 0
    input.sort()
    #print(input)
    while left < right:
        #print(left,right)
        #print(input[left],input[right],targetsum)
        if input[left] + input[right] == targetsum:
            left = left + 1
            right = right - 1
            count = count + 1
        elif input[left] + input[right] < targetsum:
            left = left + 1
        elif input[left] + input[right] > targetsum:
            right = right -1
    return count

print(ksum([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4],2))

