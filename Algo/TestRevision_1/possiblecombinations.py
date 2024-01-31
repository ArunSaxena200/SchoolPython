def pc(digits):
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
     res = []
     def backtrack(index,combination):
          if index == len(digits):
               res.append(combination)
               return
          
          letters = digit_mapping[digits[index]]

          for letter in letters:
               backtrack(index+1,combination+letter)
        
        backtrack(0,'')
        return res
               