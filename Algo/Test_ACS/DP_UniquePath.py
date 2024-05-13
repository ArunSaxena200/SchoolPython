'''
start,1,1,1,1,1,1
1    ,2,3,4,5,6,7
1    ,3,6,10,15,21,28->END

either rt or down

'''
def uniquePaths(m: int, n: int):
    grid = [[1] * n for _ in range(m)]
    #print(grid)
    for i in range(1,m):
        for j in range(1,n):
            grid[i][j]= grid[i-1][j]+grid[i][j-1]
    return grid[m-1][n-1]

print(uniquePaths(3,7))