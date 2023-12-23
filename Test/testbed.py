def equalRowCol(grid):
    n = len(grid)

    row_map = {}
    col_map = {}
    count = 0

    for i in range(n):
        row_tuple = tuple(grid[i])
        col_tuple = tuple(grid[j][i] for j in range(n))
        
        count = count + row_map.get(row_tuple,0)
        count = count + col_map.get(col_tuple,0)

        row_map = 

equalRowCol([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])