def maxSubseq(inpArray):    
    '''
    [10,9,2,5,3,7,101,18]
    [,4,3,2,1,1]    

    '''
    LIS = [1] * len(inpArray)
    for i in range(len(inpArray)-1,-1,-1):
        for j in range(i+1,len(inpArray)):
            print(inpArray[i],inpArray[j])
            if inpArray[i]<inpArray[j]:
                LIS[i] = max(LIS[i],1+LIS[j])
    return LIS 
            
    
print(maxSubseq([10,9,2,5,3,7,101,18] ))