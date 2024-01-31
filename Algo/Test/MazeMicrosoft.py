'''
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] 
denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
'''

def nearestExit(maze, entrance):


    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def dfs(x, y, steps):
        if (x, y) != entrance and (x == 0 or x == m - 1 or y == 0 or y == n - 1): # checks for first row, last row or firstcol last col as boundry is an exit
            return steps  # Found the nearest exit

        maze[x][y] = '.'  # Mark the cell as visited

        min_steps = float('inf')
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                min_steps = min(min_steps, dfs(nx, ny, steps + 1))

        maze[x][y] = '.'  # Backtrack: mark the cell as unvisited
        return min_steps

    result = dfs(entrance[0], entrance[1], 0)
    return result if result != float('inf') else -1

# Example usage:
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

result = nearestExit(maze, entrance)
print(result)
