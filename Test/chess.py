class ChessGame:
    def __init__(self):
        # Initialize the chessboard
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        # Initialize pieces on the chessboard
        # 'p' for pawn, 'r' for rook, 'n' for knight, 'b' for bishop
        # 'q' for queen, 'k' for king (lowercase for black pieces)
        pieces_order = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        for i in range(8):
            self.board[1][i] = 'p'  # Black pawns
            self.board[6][i] = 'P'  # White pawns
            self.board[0][i] = pieces_order[i]  # Black back row
            self.board[7][i] = pieces_order[i].upper()  # White back row

    def print_board(self):
        # Print the current state of the chessboard
        for row in self.board:
            print(' '.join(piece if piece else '.' for piece in row))
        print()

    def move(self, start, end):
        # Move a chess piece from start to end
        start_row, start_col = 8 - int(start[1]), ord(start[0].lower()) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0].lower()) - ord('a')

        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            print("Invalid move.")
            return

        # Perform the move
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = ''

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        # Check if the move is valid (basic validation)
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Additional validation logic can be added based on chess rules

        return True


# Example usage:
chess_game = ChessGame()
chess_game.print_board()

# Move a pawn from e2 to e4
chess_game.move('e2', 'e4')
chess_game.print_board()

# Move a knight from g1 to f3
chess_game.move('g1', 'f3')
chess_game.print_board()
