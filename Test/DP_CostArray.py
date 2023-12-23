def costArray(costArrayInp):
    '''
    [10,15,20,45,67,87],0

    '''
    costArrayInp.append(0)
    for i in range(len(costArrayInp)-3,-1,-1):
        #print("i",i)
        #print(costArrayInp[i])
        costArrayInp[i] = min(costArrayInp[i]+costArrayInp[i+1],costArrayInp[i]+costArrayInp[i+2])
        #print(costArrayInp[i])
    print(min(costArrayInp[0],costArrayInp[1]))


costArray([10,15,20,45,67,87])
