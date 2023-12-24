def decode_string(s):
        current_num = 0
        current_str = ""
        stack = []
        for char in s:
            if char.isdigit():
                current_num = int(char)
                
            elif char == '[':
                stack.append((current_num,current_str))
                current_str = ""
                current_num = 0
            elif char == ']':
                prev_num,prev_str = stack.pop()
                print(prev_str,current_str)
                current_str = prev_str + current_str*prev_num
            else:
                current_str = current_str + char
            
        return current_str

# Example usage:
s = "3[a]2[bc]"
result = decode_string(s)
print(result)  # Output: "aaabcbc"
