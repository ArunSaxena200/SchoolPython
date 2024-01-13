def maxVowels(input,k):
    '''
    leetcode
    01234567


    3

    '''
    vowels = ['a','e','i','o','u']
    left = 0
    lent = len(input) -1
    right = k
    start = 0
    count = 0
    res = []
    while left < lent:
        if len(input[start:right])==3:
            testStr = input[start:right].lower()
            #print(testStr,sum(testStr.count(char) for char in vowels))
            res.append(sum(testStr.count(char) for char in vowels))
            start = start + 1
            right = right + 1
            left = left + 1
        else:
            break
    return max(res) if res is not None else 0
    
print(maxVowels("leetcode",3))