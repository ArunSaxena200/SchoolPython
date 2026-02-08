"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]

Output:         [[1,0,1],
                 [0,0,0],
                 [1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
"""


def setZero(grid):
    rows = len(grid)
    cols = len(grid[0])

    first_row_zero  = False
    first_col_zero  = False

    for j in range(cols):
        if grid[0][j]==0:
            first_row_zero = True
            break
    for i in range(rows):
        if grid[i][0]==0:
            first_col_zero = True
            break
    for i in range(1,rows):
        for j in range(1,cols):
            if grid[i][j]==0:
                grid[0][j]=0
                grid[i][0]=0
    for i in range(1,rows):
        for j in range(1,cols):
            if grid[0][j]==0 or grid[i][0]==0:
                grid[i][j]=0
    if first_row_zero:
        for j in range(cols):
            grid[0][j]=0
    if first_col_zero:
        for i in range(rows):
            grid[i][0]=0



mat = [[1,0,1],[1,0,1],[1,1,1]]
setZero(mat)
print(mat)   # yahi updated matrix print hoga