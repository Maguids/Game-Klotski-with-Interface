from menu_pygame import start_pygame
from menu_terminal import * 

def start():
    print("Welcome to our version of the 'Puzzle Packed IQ Game'!")
    print("Please chose if you rather play in Pygame or Terminal:")
    print("     Pygame (1)")
    print("     Terminal (2)")
    print("     Quit (3)")
    choice = input("Please choose the number of your choice (ex: 1): ")

    while choice not in ['1', '2', '3']:
        print("Wrong input, please try again")
        choice = input("Please choose the number of your choice (ex: 1): ")

    if choice == '3':
        exit()
    elif choice == '1':
        pass
        start_pygame()
    else:
        start_terminal()

start()