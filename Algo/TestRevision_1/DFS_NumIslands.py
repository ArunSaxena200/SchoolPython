def numIslands(grid):

    def dfs(i,j):
        #base case
        if  0<= i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "visited"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
    
    numIslands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                numIslands = numIslands + 1
                dfs(i,j)
    return numIslands



grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid1))  # Output: 1
