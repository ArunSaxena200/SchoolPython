def validSubseq(inputs,s):
    '''
    s = "a b c", input = "a h bgdc"

    '''
    i,j = 0,0
    while i < len(s) and j < len(inputs):
        if s[i] == inputs[j]:
            i+=1
        j+=1
    return i == len(s)


print(validSubseq("a h bgdc","abc"))