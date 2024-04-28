def maxSubseq(inpArray):    
    '''
    [0,1,0,3,2,3]
    [1,1,1,1,2,1]    

    '''
    LIS = [1] * len(inpArray)
    print(LIS)
    for i in range(len(inpArray)-1,-1,-1):
        
        for j in range(i+1,len(inpArray)):
            #print(inpArray[i],inpArray[j])
            if inpArray[i]<inpArray[j]:
                LIS[i] = max(LIS[i],1+LIS[j])
    return LIS 
            
    
print(maxSubseq([1,2,4,3] ))