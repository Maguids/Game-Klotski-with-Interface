
from copy import deepcopy
from game import Game, get_possible_moves, execute_moves


def breadth_first_search(game, max_depth):
    visited = []
    queue = []
    path = []
    depth = 0
    queue.append((depth, game.game_board, game.pieces, path ))
    visited.append(game.game_board)
    while len(queue) != 0:
        current_depth, current_board, current_pieces, current_path = queue.pop(0)
        new_game = Game(current_pieces, current_board)

        # check if the game has been won
        if new_game.win() == True:
            return current_path
        
        # Check if the maximum depth has been reached.
        if current_depth < max_depth:
            # Explore the possible moves from the current state.
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
                # Execute the move and update the game state.
                execute_moves(new_game_state, move)
                # Check if the resulting state has already been visited.
                if new_game_state.game_board not in visited:
                    # If the state has not been visited, add it to the queue along with its depth, game board, pieces, and path.
                    visited.append(new_game_state.game_board)
                    new_path = current_path + [move]
                    queue.append((current_depth + 1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None

    return None
