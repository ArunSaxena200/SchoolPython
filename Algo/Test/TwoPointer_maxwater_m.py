def maxWater(input):
    left = 0
    right = len(input)-1
    '''
    L*B = area
    '''    
    maxwater = 0
    while left < right:
        waterArea = (right - left) * min(input[left],input[right])
        maxwater = max(maxwater,waterArea)
        if input[left] < input[right]:
            left = left +1
        else:
            right = right -1
    return maxwater

print(maxWater([2,3,4,5,18,17,6]))

def max_area(height):
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate the width of the container
        width = right - left

        # Calculate the height of the container
        container_height = min(height[left], height[right])

        # Update the maximum water if the current container holds more water
        max_water = max(max_water, width * container_height)

        # Move the pointers towards each other
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage:
height = [2, 3, 4, 5, 18, 17, 6]
result = max_area(height)
print(result)
