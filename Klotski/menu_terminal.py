
from game import *
from play_in_terminal import *
from create_board import board


easy_levels = {
    '1': level1_pieces,
    '2': level2_pieces,
    '3': level3_pieces,
    '4': level4_pieces,
    '5': level5_pieces,
}

medium_levels = {
    '1': level6_pieces,
    '2': level7_pieces,
    '3': level8_pieces,
    '4': level9_pieces,
    '5': level10_pieces
}

hard_levels = {
    '1': level11_pieces,
    '2': level12_pieces,
    '3': level13_pieces,
    '4': level14_pieces,
    '5': level15_pieces
}


def choose_difficulty():
    print("")
    print("Menu:")
    print("  Easy")
    print("  Medium")
    print("  Hard")
    print("")
    difficulty_input = input("Choose the level difficulty (exemple: Easy): ")
    while difficulty_input not in ['Easy', 'easy', 'Medium', 'medium', 'Hard', 'hard', 'quit']:
        print("Wrong Input. Please try again")
        difficulty_input = input("Choose the level difficulty (exemple: Easy): ")
    
    return difficulty_input


def easy_mode():
    print("")
    print("LEVELS - EASY:")
    print("  Level 1")
    print("  Level 2")
    print("  Level 3")
    print("  Level 4")
    print("  Level 5")
    print("")
    level_input = input("Choose the level (exemple: 1): ")
    while level_input not in ['1', '2', '3', '4', '5', 'quit', 'menu', 'Menu']:
        print("Wrong Input. Please try again")
        level_input = input("Choose the level (exemple: 1): ")

    if level_input == 'quit':
        print("")
        print("Goodbye!")
        quit()
    elif level_input in ['menu', 'Menu']:
        menu()  
    else:
        stamp = True
        next = play_game_in_terminal(deepcopy(easy_levels[level_input]), board, stamp)
        next
        if level_input == '5':
            pass
        else:
            while next == True:
                level_input = next_level(level_input)
                if level_input != '99':
                    next = play_game_in_terminal(deepcopy(easy_levels[level_input]), board, stamp)
                    next
        menu()


def medium_mode():
    print("")
    print("LEVELS - MEDIUM:")
    print("  Level 1")
    print("  Level 2")
    print("  Level 3")
    print("  Level 4")
    print("  Level 5")
    print("")
    level_input = input("Choose the level (exemple: 1): ")
    while level_input not in ['1', '2', '3', '4', '5', 'quit', 'menu', 'Menu']:
            print("Wrong Input. Please try again")
            level_input = input("Choose the level (exemple: 1): ")

    if level_input == 'quit':
        print("")
        print("Goodbye!")
        quit()
    elif level_input in ['menu', 'Menu']:
        menu()  
    else:
        stamp = True
        next = play_game_in_terminal(deepcopy(medium_levels[level_input]), board, stamp)
        next
        if level_input == '5':
            pass
        else:
            while next == True:
                level_input = next_level(level_input)
                if level_input != '99':
                    next = play_game_in_terminal(deepcopy(medium_levels[level_input]), board, stamp)
                    next
        menu()



def hard_mode():
    print("")
    print("LEVELS - HARD:")
    print("  Level 1")
    print("  Level 2")
    print("  Level 3")
    print("  Level 4")
    print("  Level 5")
    print("")
    level_input = input("Choose the level (exemple: 1): ")
    while level_input not in ['1', '2', '3', '4', '5', 'quit', 'menu', 'Menu']:
            print("Wrong Input. Please try again")
            level_input = input("Choose the level (exemple: 1): ")

    if level_input == 'quit':
        print("")
        print("Goodbye!")
        quit()
    elif level_input in ['menu', 'Menu']:
        menu()  
    else:
        stamp = True
        next = play_game_in_terminal(deepcopy(hard_levels[level_input]), board, stamp)
        next
        if level_input == '5':
            pass
        else:
            while next == True:
                level_input = next_level(level_input)
                if level_input != '99':
                    next = play_game_in_terminal(deepcopy(hard_levels[level_input]), board, stamp)
                    next
        menu()

def next_level(level_input):
    if int(level_input) + 1 < 6:
        new_level_input = str(int(level_input) + 1)
        next_level_input = input("Whould you like to go to level" + str(new_level_input) + "?(y/n) ")
        while next_level_input not in ['y', 'Y', 'n', 'N', 'quit']:
            print("Wrong Input. Please try again")
            next_level_input = input("Whould you like to go to level" + str(new_level_input) + "?(y/n) ")

        if next_level_input == 'quit':
            print("")
            print("Goodbye!")
            quit()
        elif next_level_input in ['y', 'Y']:
            return new_level_input
        else:
            new_level_input = '99'
            return new_level_input
    else:
        new_level_input = '99'
        return new_level_input


def menu():
    difficulty_input = choose_difficulty()

    if difficulty_input in ['Easy', 'easy']:
        easy_mode()    
    elif difficulty_input in ["Medium", "medium"]:
        medium_mode()
    elif difficulty_input in ["Hard", "hard"]:
        hard_mode()
    else:
        print("")
        print("Goodbye!")
        quit()
    

def start_terminal():
    print(" ")
    print("Hello! Welcome to our version of the Puzzle Packed IQ Game in terminal!")
    print("Whenever you want to quit the game, just type 'quit'.")
    print("If you want to go back to the menu, type 'menu'.")
    print("Or if you simply want to restart the level type 'r'.")

    start = input("Ready to start? (y/n) ")
    while start not in ['y', 'n', 'Y', 'N', 'quit']:
        print("Wrong Input. Please try again")
        start = input("Ready to start?(y/n) ")

    if start in ['n', 'N', 'quit']:
        print("")
        print("Goodbye!")
        quit()
    else:
        menu()