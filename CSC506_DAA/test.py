def binary_search(arr, target):
    # Binary search function
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

def threeNumSum(input, targetSum):
    input.sort()
    result = []

    for i in range(len(input) - 2):
        left = i + 1
        right = len(input) - 1

        while left < right:
            current_sum = input[i] + input[left] + input[right]

            if current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1
            else:
                result.append([input[i], input[left], input[right]])

                left += 1
                right -= 1

    return result

print(threeNumSum([1, 2, 3, 4, 5, 6], 11))
