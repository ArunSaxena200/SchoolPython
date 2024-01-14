def GCD(n1,n2):
    '''
    20,8
    20/8 = 4 = r
    b =4
    a = 8

    8/4 = 0

    10/4 = 0
    '''
    while (n2!=0):
        t= n1
        n1 = n2
        r = t%n2
        n2 =r
    return n1

print(GCD(10,8))
