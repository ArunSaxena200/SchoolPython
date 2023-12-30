def mte(input,toMove):
    left = 0
    right = len(input)-1
    while left<right:
        if input[right] == toMove:
            right = right -1
        if input[left] == toMove:
            input[left],input[right]=input[right],input[left]
        left = left + 1
    return input




print(mte([0,1,0,3,12],0))