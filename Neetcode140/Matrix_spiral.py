"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3]
                ,[4,5,6],
                 [7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
"""

def spiralMatrix(grid):
    left, right = 0,len(grid[0])-1
    top,bottom = 0,len(grid)-1
    res = []
    while top<=bottom and left <= right:
        for c in range(left,right+1):
            res.append(grid[top][c])
        top+=1
        
        for r in range(top,bottom+1):
            res.append(grid[r][right])
        right-=1
        if top <= bottom:
            for c in range(right,left-1,-1):
                res.append(grid[bottom][c])
            bottom-=1
        if left<=right:
            for r in range(bottom,top-1,-1):
                res.append(grid[r][left])
            left+=1
    return res


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(spiralMatrix(matrix))    



