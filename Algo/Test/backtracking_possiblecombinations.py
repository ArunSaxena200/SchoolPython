def letter_combinations(digits):
    if not digits:
        return []
    '''
    use hash map for matching
    abc - def 

    '''


    # Define the mapping of digits to letters
    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(index, current_combination):
        # If the current combination is of the same length as digits, add it to the result
        #print(index,current_combination)
        if index == len(digits):
            result.append(current_combination)
            #print("res",result)
            return

        # Get the letters corresponding to the current digit
        letters = digit_mapping[digits[index]]
        #print("l",digits[index])

        # Explore all possible combinations by appending each letter to the current combination
        for letter in letters:
            backtrack(index + 1, current_combination + letter)

    result = []
    backtrack(0, '')

    return result

# Example usage:
digits = "23"
result = letter_combinations(digits)
print(result)
