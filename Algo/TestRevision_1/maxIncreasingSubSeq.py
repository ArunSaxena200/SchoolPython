def Lis(inputarray):
    lis = [1] * len(inputarray)
    for i in range(len(inputarray)-1,-1,-1):
        for j in range(i+1,len(inputarray)):
            if inputarray[i]<inputarray[j]:
                lis[i] = max(lis[i],1+lis[j])
    print(lis)


print(Lis([0,1,0,3,2,3] ))