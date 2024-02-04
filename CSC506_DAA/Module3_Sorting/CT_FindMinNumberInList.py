def findMin1(inputList):
    '''
    10,7,2,6,-1,5,4
    Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list O(n2). 
    The second function should be linear O(n).
    '''
    temp = 99999
    for i in range(len(inputList)):
        for j in range(len(inputList)):
            #print("pass",inputList[i],inputList[j])
            if inputList[i]<inputList[j] and inputList[i]<temp:
                temp = inputList[i]               
    return temp
            
def findMin2(inputList):
    temp = 99999
    for i in range(len(inputList)):
        if inputList[i]<temp:
            temp = inputList[i]
    return temp

print(findMin2([10,7,2,-9,-10,6,5,4]))
