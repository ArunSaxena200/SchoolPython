def threeNumSum(inputarray,target):
    
    '''
    1,2,3,4,5,6,7
    11
    2,3,6
    '''
    inputarray.sort()
    res = []
    #loop thru the array
    for i in range(len(inputarray)):
        left = i+1
        right = len(inputarray)-1

        while (left<right):
            if inputarray[i] + inputarray[left] + inputarray[right] < target:
                left = left + 1
            elif inputarray[i] + inputarray[left] + inputarray[right] > target:
                right = right -1
            elif inputarray[i] + inputarray[left] + inputarray[right] == target:

                res.append([inputarray[i],inputarray[left],inputarray[right]])

                left = left + 1
                right = right -1
    return res

print(threeNumSum([12,3,1,2,-6,5,-8,6],-2))
