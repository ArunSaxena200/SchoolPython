def compress(chars):
    i, j, index = 0, 0, 0
    while i < len(chars):
        count = 0
        while j < len(chars) and chars[i] == chars[j]:
            j = j + 1
            count = count + 1
        chars[index] = chars[i]
        index = index + 1

        if count > 1:
            for digit in str(count):
                chars[index] = digit
                index = index + 1
        i = j
    return chars[0:j]

print(compress(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']))

