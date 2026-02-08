def longest_consecutive(nums):
	seen = set(nums)
	print(seen)
	longest = 0
	for num in seen:
		if num-1 not in seen:
			current = num
			length = 1
			while current+1 in seen:
				current+=1
				length+=1
			if length > longest:
				longest = length
                
	return longest


if __name__ == "__main__":
	print(longest_consecutive([1, 0, 1, 2]))
