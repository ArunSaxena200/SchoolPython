def maze(maze,entrance):
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def dfs(x,y,steps):
        #base
        if (x,y)!=tuple(entrance) and (x==0 or x== m-1) and (y==0 and y==n-1):
            return steps
        maze[x][y]="+"
        min_steps = float("inf")

        for dx, dy in directions:
            nx = x+dx
            ny = y+dy

            if 0<=nx<m and 0<=ny<n and maze[nx][ny]==".":
                min_steps = min(min_steps,dfs(nx,ny,steps+1))
        maze[x][y]="."

    res = dfs(entrance[0],entrance[1],0)
    return res


maze1 = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,2]

result = maze(maze1, entrance)
print(result)
