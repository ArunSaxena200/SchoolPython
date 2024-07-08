
import math
import os
import random
import re
import sys



def better_compression(compressed: str) -> str:
    import re
    
    # Dictionary to store accumulated frequencies
    frequency_dict = {}
    
    # Regular expression to find all character-frequency pairs
    pairs = re.findall(r'([a-z])(\d+)', compressed)
    print("pairs",pairs)
    
    # Accumulate frequencies in the dictionary
    for char, freq in pairs:
        if char in frequency_dict:
            frequency_dict[char] += int(freq)
        else:
            print("fp",char)
            frequency_dict[char] = int(freq)
    
    # Create a sorted list of characters
    sorted_characters = sorted(frequency_dict.keys())
    
    # Construct the new compressed string
    result = ''.join(f'{char}{frequency_dict[char]}' for char in sorted_characters)
    
    return result

# Test cases
print(better_compression("a1234563c9b2c1"))  # Output: "a3b2c10"
#print(better_compression("c2b3a1"))    # Output: "a1b3c2"
#print(better_compression("a2b4c1"))    # Output: "a2b4c1"
