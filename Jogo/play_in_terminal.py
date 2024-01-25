
from create_board import*
from game import *
from levels import *
from bfs import breadth_first_search
from a_star import a_star
from greedy import greedy


def choose_hint(game):
    search_method = 'a_star'
    max_depth = 30
    n_hints = '1'
    print('Predifined: A* that gives you one hint with depth=30')
    hint_input = input('Would you like to change it? (y/n) ')
    while hint_input not in ['y', 'Y', 'n', 'N']:
        print("Wrong Input. Please try again")
        hint_input = input('Would you like to change it? (y/n) ')

    if hint_input in ['n', 'N']:
        get_hint(game, search_method, max_depth, n_hints)
    else:
        print("You can change: the search method to: 'bfs', 'a_star' or 'greedy'.")
        print("                the maximum depth to any number (recommended 30) ")
        print("                the number of hints to '1', '2', 'all' ")

        search_method = str(input("search method: "))
        while search_method not in ['bfs', 'a_star', 'greedy']:
            print("Wrong Input. Please try again")
            search_method = str(input("search method: "))

        max_depth = int(input("maximum depth: "))

        n_hints = str(input("number of hints: "))
        while n_hints not in ['1', '2', 'all']:
            n_hints = str(input("number of hints: "))
                          
        get_hint(game, search_method, max_depth, n_hints)


def get_hint(game, search_method, max_depth, n_hints):
    if n_hints == '1':
        n = 1
    elif n_hints == '2':
        n = 2
    else:
        n = None
    
    if search_method == 'bfs':
        path = breadth_first_search(game, max_depth)
        if path is not None:
            print("Resposta bfs: ", path[:n])
        else:
            print('OUT OF RANGE: Try any move')
    elif search_method == 'a_star':
        path = a_star(game, max_depth)
        if path is not None:
            print("Resposta A*: ", path[:n])
        else:
            print('OUT OF RANGE: Try any move')
    elif search_method == 'greedy':
        path = greedy(game, max_depth)
        if path is not None:
            print("Resposta greedy: ", path[:n])
        else:
            print('OUT OF RANGE: Try any move')





def play_game_in_terminal(pieces, board, stamp):
    level_pieces = deepcopy(pieces)
    game_board = create_game_board(level_pieces, board)
    game = Game(level_pieces, game_board)
    game.print_game()

    game_piece_id = []
    for piece_id in level_pieces:
        game_piece_id.append(piece_id)
    game_direction = ['up', 'down', 'left', 'right']

    while game.win() == False:
    
        move_input = input("Qual peça você gostaria de mover e em que direção (exemplo: 1 up)? ")
        move_input = move_input.split()

        list_move_input = []
        for word in move_input:
            list_move_input.append(word)

        if len(list_move_input) == None:
            print("Wrong Input. Please try again")
        elif len(list_move_input) == 1:
            if list_move_input[0] == 'quit':
                print("")
                print("Goodbye!")
                quit()
            elif list_move_input[0] in ['menu', 'Menu']:
                return False
            elif list_move_input[0] == 'hint':
                choose_hint(game)
            elif list_move_input[0] == 'r':
                level_pieces = deepcopy(pieces)
                game_board = create_game_board(level_pieces, board)
                game = Game(level_pieces, game_board)
                game.print_game()
            else:
                print("Wrong Input. Please try again")
        elif len(list_move_input) == 2:
            piece_id = move_input[0]
            direction = move_input[1]

            if (piece_id in game_piece_id) and (direction in game_direction):
                game.move_pieces(piece_id, direction, stamp)
                
            else:
                print("Wrong Input. Please try again")
        else:
            print("Wrong Input. Please try again")
    
    return True
