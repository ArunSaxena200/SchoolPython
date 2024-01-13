def nearestExit(maze, entrance):
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def dfs(x, y, steps):
        if (x, y) != entrance and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
            return steps  # Found the nearest exit

        maze[x][y] = 'visited'  # Mark the cell as visited

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
maze = [
    ['+', '+', '+', '+', '+', '+'],
    ['+', 'E', '.', '.', '.', '+'],
    ['+', '.', '+', '+', '.', '+'],
    ['+', '.', '.', '.', '.', '+'],
    ['+', '+', '+', '+', '+', '+']
]
entrance = [1, 1]

result = nearestExit(maze, entrance)
print(result)
