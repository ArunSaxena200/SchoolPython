def countBattleships(board):
    if not board or not board[0]:
        return 0

    rows, cols = len(board), len(board[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                count += 1

    return count
