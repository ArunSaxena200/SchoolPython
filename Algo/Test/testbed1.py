def perms(inpSTring):
    res = []
    def backtrack(i,combinatin):
        if i == len(combinatin):
            return res.append(combinatin)
        for letters in combinatin:
            print(letters)
            backtrack(i+1,combinatin+letters)
        backtrack(0,[])

print(perms('123'))