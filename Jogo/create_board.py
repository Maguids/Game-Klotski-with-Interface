
from copy import deepcopy
board = [
    ['*', '*', '*', '*', '*', '*'],
    ['*', '0', '0', '0', '0', '*'],
    ['*', '0', '0', '0', '0', '*'],
    ['*', '0', '0', '0', '0', '*'],
    ['*', '0', '0', '0', '0', '*'],
    ['*', '0', '0', '0', '0', '*'],
    ['*', '*', ' ', ' ', '*', '*']
    ]


def create_game_board(pieces, game_board):
    # Create a deep copy of the game_board to avoid modifying the original board
    game_board = deepcopy(board)
    for piece_id in pieces:
        for position in pieces[piece_id]:
            position_x = position[0]
            position_y = position[1]
           # Check if the cell on the game_board is empty
            if game_board[position_x][position_y] == '0':
                # Update the game_board with the piece ID at the position
                game_board[position_x][position_y] = piece_id

    return (game_board)