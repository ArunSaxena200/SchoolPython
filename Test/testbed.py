def countBattleships(board):
    if not board or not board[0]:
        return 0
    
    num_ships = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X' and (i == 0 or board[i-1][j]!='X') and (j==0 or board[i][j-1]!='X'):
                num_ships +=1
    return num_ships

# Example usage:
board = [
    ['X', '.', '.', 'X'],
    ['.', '.', 'X', 'X'],
    ['.', '.', '.', 'X']
]

result = countBattleships(board)
print(result)  # Output: 2
