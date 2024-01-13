def revString(input):
    stack = []
    output = ""
    for char in input:
         stack.append(char)
    while len(stack)>0:
        output += stack.pop()
    return (output)

print(revString("arun"))
