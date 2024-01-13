def testStar(input):
    stack = []
    for char in input:
        if char == "*":
            stack.pop()
        else:
            stack.append(char)
            #print(stack)
    return "".join(stack)

print(testStar("le*etcode"))