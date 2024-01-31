def revWords(input):
    '''
    Tim Is Great

    Great Is Tim
    '''
    res = []
    start = 0

    for i in range(len(input)):
        char = input[i]
        if char == " ":
            res.append(input[start:i])
            start = i
        elif input[start]  == " ":
         res.append(" ")
         start = i
    res.append(input[start:])
    print("".join(revThings(res)))
    print("hello")

def revThings(array):
    left,right = 0,len(array)-1
    while left < right:
        array[left],array[right] = array[right],array[left]
        left = left + 1
        right = right -1
    return array
        
            
    

revWords("tim is great")