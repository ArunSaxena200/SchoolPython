def matrix(grid):
    '''
      L              R     
      1,  2,   3,   4
     5,  TB6,   7,   8
     9,  B10,  11,  12
    
    '''     
    left = 0
    right = len(grid[0])
    top = 0
    bottom = (len(grid))
    res = []

    while left < right and top < bottom:
        # i in top row
        for i in range(left,right):
            res.append(grid[top][i])
        top = top +1
       
        for i in range(top,bottom):
            res.append(grid[i][right-1])
        right = right -1

        for i in range(right-1,left-1,-1):
            res.append(grid[bottom-1][i])
        bottom = bottom - 1

        for i in range(bottom-1,top-1,-1):
            res.append(grid[i][left])
        left = left + 1
    return res

print(matrix([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]))