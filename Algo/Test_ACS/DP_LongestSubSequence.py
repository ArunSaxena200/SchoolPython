'''
1,2,4,3
1,2,1,1 
'''

def LIS(input):
    lis = [1]*len(input)
    print(lis)
    for i in range(len(input),-1,-1):
        for j in range(i+1,len(input)):
            if input[i]<input[j]:
                lis[i]= max(lis[i],1+lis[j])
    return lis
    


print(LIS([1,2,4,3]))