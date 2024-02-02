def insertion(input):
    for i in range(1,len(input)):
        j=i
        while(j>0 and input[j]<input[j-1]):
            print(j)
            temp = input[j]
            input[j] = input[j-1]
            input[j-1] = temp
            j=j-1
            print(f"pass {j} = {input}")
    return(input)

print(insertion([10, 2, 78, 4, 45, 32, 7, 11]))