def robber(inpArray):
    '''
    1,2,3,1
    '''
    lenArray = len(inpArray)
    rob = max(inpArray[0]+inpArray[2:lenArray-1],rob[1:lenArray-1])
    