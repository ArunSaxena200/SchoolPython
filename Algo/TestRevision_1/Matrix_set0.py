def setZero(grid):
    rows = len(grid)
    cols = len(grid[0])
    print(cols)

    array_zero_row = []
    array_zero_col = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                array_zero_row.append(i)
                array_zero_col.append(j)
    
    for row in array_zero_row:
        for j in range(cols):
            grid[row][j]=0
    
    for col in array_zero_col:
        for i in range(rows):
            grid[i][col] = 0

    return grid




# Example usage:
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1]
]

result = setZero(matrix)
print(result)