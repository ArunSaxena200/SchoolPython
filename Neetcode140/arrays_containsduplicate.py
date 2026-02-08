def contups(inp):
    a = set()
    for char in inp:
        a.add(char)
    return len(a)==len(inp)

print(contups([1,2,3]))
