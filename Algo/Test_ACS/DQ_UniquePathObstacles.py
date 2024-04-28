'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

0,0,0
0,1,0
0,0,0
  
  j
i 1,1,1
  1,0,0
  1,0,0


'''
def uniquePathsWithObstacles(grid):
    m = len(grid)
    n = len(grid[0])

    # If the starting cell has an obstacle, there is no path.
    if grid[0][0] == 1:
        return 0

    # Initialize the grid for storing the number of paths.
    paths = [[0] * n for _ in range(m)]
    #print(paths)
    # Base case: There is exactly one way to reach the starting cell.
    paths[0][0] = 1

    # Fill in the first row. If there's an obstacle, stop filling in subsequent cells.
    for j in range(1, n):
        if grid[0][j] == 1:
            break
        paths[0][j] = 1
    #print(paths)

    # Fill in the first column. If there's an obstacle, stop filling in subsequent cells.
    for i in range(1, m):
        if grid[i][0] == 1:
            break
        paths[i][0] = 1

    # Calculate the number of paths for each cell based on the presence of obstacles.
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:  # If the cell is not an obstacle.
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    print(paths)
    # The result is stored in the bottom-right corner of the grid.
    return paths[m - 1][n - 1]

uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])