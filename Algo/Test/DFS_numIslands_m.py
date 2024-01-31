def numIslands(grid):
    if not grid:
        return 0
    def dfs(i,j):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1":
            grid[i][j] ='visited'
            
            dfs(i + 1, j)      # Explore down
            dfs(i - 1, j)      # Explore up
            dfs(i, j + 1)      # Explore right
            dfs(i, j - 1)      # Explore left
        
    num_islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":
                num_islands = num_islands+1
                dfs(i,j)
                print(grid)
    return num_islands

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(numIslands(grid1))  # Output: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid2))  # Output: 3

