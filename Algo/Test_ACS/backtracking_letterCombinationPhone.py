def phonemap(digits):
    res = []

    digit_map ={

        "2":"abc",
        "3":"def"
    }

    def backtrack(index,combination):
        #base
        if index == len(digits):
            res.append(combination)
            return
        
        letters = digit_map[digits[index]]
        print(letters)

        # iterations
        for letter in letters:
            backtrack(index+1,combination+letter)
    backtrack(0,'')
    return res


print(phonemap('23'))

