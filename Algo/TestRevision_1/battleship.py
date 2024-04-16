def battleship(grid):
    num=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="X" and (i==0 or grid[i-1][j]!="X") and (j==0 or grid[i][j-1]!="X"):
                num = num+1
    return num 


# Example usage:
board = [
    ['X', '.', '.', 'X'],
    ['.', '.', 'X', 'X'],
    ['.', '.', '.', 'X']
]

result = battleship(board)
print(result)  # Output: 2