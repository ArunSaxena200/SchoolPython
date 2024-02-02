'''
5, 9, 8, 7, 6

i=0,j=1; indexS = 0
i = 1, j=2 , indexS = 4
5, 6, 8, 7, 9
i=2,j=3,7<8,indexS = 4 =3
5,6,7,8,9
i=3,j=4
'''

def selectionSort(input):
    for i in range(len(input)):
        indexS = i
        for j in range(i+1,len(input)):
            if (input[j]<input[i]):
                indexS = j
        temp = input[i]
        input[i] = input[indexS]
        input[indexS]=temp
        print(f"pass {i} = {input}")
    return input

print(selectionSort([5,9,8,7,6]))



