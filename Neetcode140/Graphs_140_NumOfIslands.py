"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
"""
def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    def dfs(i,j):
        if  0<=i<rows and 0<=j<cols and grid[i][j]=="1":
            grid[i][j] ='seen'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
    num_islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                num_islands +=1
                dfs(i,j)
                print(grid)
    return num_islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(num_islands(grid))