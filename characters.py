# Thief
def insert_player(board, y, x):
    """Inserts player in board in certain (x, y) position"""

    player = "🚹"
    board[y][x] = player
    
    return board