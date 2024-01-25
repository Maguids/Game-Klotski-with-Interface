
from copy import deepcopy
from game import Game, get_possible_moves, execute_moves


def a_star(game, max_depth):
    # Initialize an empty priority queue, a visited set, a path list and a depth counter.
    queue = []
    visited = []
    path = []
    depth = 0
    # Set the total cost of the initial node as the sum of the heuristic value.
    #game.manhattan_distane = h(n)
    #game.cost = g(n)
    cost_t = game.manhattan_distance() + game.cost
    queue.append((cost_t, depth, game.game_board, game.pieces, path))
    visited.append(game.game_board)
    while len(queue) != 0:
        queue.sort()
        # Pop the node with the lowest total cost from the queue.
        _, current_depth, current_board, current_pieces, current_path = queue.pop(0)
        new_game = Game(current_pieces, current_board)

        # Check if the game has been won.
        if new_game.win() == True:
            return current_path
        
        if current_depth < max_depth:
            # Explore the possible moves from the current state.
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
               # Execute the move and update the game state
                execute_moves(new_game_state, move)
                # Check if the resulting state has already been visited
                if new_game_state.game_board not in visited:
                    # If the state has not been visited, add it to the queue along with its heuristic value, depth, game board, pieces, and path.
                    visited.append(new_game_state.game_board)
                    new_path = current_path + [move]
                    cost_t = new_game_state.manhattan_distance() + new_game_state.cost
                    queue.append((cost_t, current_depth +1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None
    
    return None

