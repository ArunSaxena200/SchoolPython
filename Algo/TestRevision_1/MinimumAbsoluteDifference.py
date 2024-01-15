def minDiff(inp1,inp2):
    '''
    1,3,6,7

    2,4,8,9


    '''
    inp1.sort()
    inp2.sort()
    i = 0
    j = 0
    small = 99999

    while (i < len(inp1) and j < len(inp2)):
        first = inp1[i]
        second = inp2[j]

        if first > second:
            diff = first -second
            j = j+1
        elif second > first:
            diff = second - first
            i = i+1
        if diff < small:
            small = diff
            res = [first,second]
    return (res)

print(minDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

