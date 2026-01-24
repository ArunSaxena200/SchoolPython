def pacificAtlantic(height):
    rows = len(height)
    cols = len(height[0])
    pacific = set()
    atlantic = set()

    def dfs(i,j,ocean_set, prev_height):
        if 0<=i<rows and 0<=j<cols and (i,j) not in ocean_set and prev_height>=height[i][j]:
            ocean_set.add((i,j))
            dfs(i,j+1,ocean_set,height[i][j])
            dfs(i,j-1,ocean_set,height[i][j])
            dfs(i+1,j,ocean_set,height[i][j])
            dfs(i-1,j,ocean_set,height[i][j])
    
    # Pacific edges - avoid corner duplicates
    for i in range(rows):
        dfs(i,0,pacific,height[i][0])  # Left edge
    for j in range(1,cols):  # Start from 1 to skip top-left corner
        dfs(0,j,pacific,height[0][j])  # Top edge

    # Atlantic edges - avoid corner duplicates
    for i in range(rows):
        dfs(i,cols-1,atlantic,height[i][cols-1])  # Right edge
    for j in range(cols-1):  # End before last column to skip bottom-right corner
        dfs(rows-1,j,atlantic,height[rows-1][j])  # Bottom edge
    
    result = list(pacific & atlantic)
    return result

heights = [[1,2,2,3],[3,2,3,4],[2,4,5,5],[4,4,1,4]]
print(pacificAtlantic(heights))
# Expected: [[0,2],[1,0],[1,1],[2,2],[3,0],[3,1]]