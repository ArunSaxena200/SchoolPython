def reverse(input):
    '''
    adding strip is the key here
    '''
    start = 0
    res = []
    test = ""
    for i in range(len(input)):
        if input[i]==" ":
            res.append(input[start:i].strip())
            start = i 
        elif input[start] == " ":
            res.append(" ")
            start = i
    res.append(input[start:])
    print(res)
    buildStr(res)
    return test.join(res)

def buildStr(array1):
    left = 0
    right = len(array1)-1
    while left<right:
        array1[left],array1[right] = array1[right],array1[left]
        left = left +1
        right = right-1


print(reverse("a good   example"))

