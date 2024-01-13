def smallesDiff(array1,array2):
    array1.sort()
    array2.sort()
    print(array1)
    print(array2)
    i=0
    j=0
    smallest = 9999999
    #result =[]
    while i<len(array1) and j<len(array2):
        first = array1[i]
        second = array2[j]

        if first<second:
            diff = second-first
            i=i+1
        if first>second:
            diff = first-second
            j = j+1
        
        if smallest>diff:
            smallest = diff
            result = [first,second]
    return result

print(smallesDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))