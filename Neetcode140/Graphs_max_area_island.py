"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_area = 0

    def dfs(i,j):
        if 0<=i<rows and 0<=j<cols and grid[i][j]==1:
            grid[i][j] = 'Seen'  # Mark as visited
            area = 1
            area = area + dfs(i-1,j)
            area = area + dfs(i+1,j)
            area = area + dfs(i,j-1)
            area = area + dfs(i,j+1)
            return area
        return 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                area = dfs(i,j)
                max_area = max(max_area,area)
    
    # Print grid after all DFS
    print("Grid after DFS:")
    for row in grid:
        print(row)
    
    return max_area

grid =[[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,1,1,0,1,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))               