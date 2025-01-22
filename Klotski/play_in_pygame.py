from create_board import*
from game import *
from levels import *
from bfs import breadth_first_search
from a_star import a_star
from greedy import greedy
from settings import Button


import pygame
from sys import exit

WIDTH = 630
HEIGHT = 750
ROWS = 7
COLUMNS = 6
SIZE = 70
BG = pygame.image.load("Resources\Images\_background.png")
BG_LEVEL = pygame.image.load("Resources\Images\_background_level.png")


def get_font(size): 
    font = pygame.font.Font("Resources\Text\Orbitron\orbitron.ttf", size)
    return font

#depending on the serach method selected end the max depth it returns a hint
def get_hint(game, search_method, max_depth):
    if search_method == 'bfs':
        path = breadth_first_search(game, max_depth)
        if path is not None:
            return str(path[0])
        else:
            return 'Try any move'
    elif search_method == 'a_star':
        path = a_star(game, max_depth)
        if path is not None:
            return str(path[0])
        else:
            return 'Try any move'
    elif search_method == 'greedy':
        path = greedy(game, max_depth)
        if path is not None:
            return str(path[0])
        else:
            return 'Try any move'

# create a dictionary that binds the piece's ID with it´s respective rectangles on the board 
def create_dic(game_board):
    dic = {}

    for x_matrix in range(ROWS):
        for y_matrix in range(COLUMNS):
            y_board = x_matrix
            x_board = y_matrix

            piece_id = game_board[x_matrix][y_matrix]
            rect = pygame.Rect(x_board * SIZE, y_board * SIZE, SIZE, SIZE)
            new_list = []
            if piece_id in dic:
                for old_rect in dic[piece_id]:
                    new_list.append(old_rect)
                new_list.append(rect)
                dic[piece_id] = new_list
            else:
                new_list.append(rect)
                dic[piece_id] = new_list
    return dic

# joins rectangles into one
def rectangles_union(piece_id, dic):
    for rectangle in dic[piece_id]:
                if rectangle == dic[piece_id][0]:
                    old_rect = rectangle
                else:
                    new_rect = old_rect.union(rectangle)
                    old_rect = new_rect
    return new_rect

# if colorblind 'on' or 'hint' selected it shows the piece's ID on the rectangles
def draw_colorblind(piece_id, new_rect, screen):
    font = pygame.font.Font("Resources\Text\Orbitron\orbitron.ttf", 30)
    text = font.render(piece_id, True, 'Black')
    rect_position = new_rect.center
    text_position = (rect_position[0] + 95, rect_position[1] + 115)
    screen.blit(text, text_position)

# draws the board
def draw_board(screen, game_board_surface, game_board, colorblind):
    dic = create_dic(game_board)
    

    for piece_id in dic:
        if piece_id == '*':
            for rectangle in dic[piece_id]:
                pygame.draw.rect(game_board_surface, 'Black', rectangle)
        elif piece_id == '!':
            new_rect = rectangles_union(piece_id, dic)
            pygame.draw.rect(game_board_surface, 'Red', new_rect)
            pygame.draw.rect(game_board_surface, (0, 0, 0), new_rect, 2)
            if colorblind == True:
                draw_colorblind(piece_id, new_rect, screen)
                
        elif piece_id == ' ':
            for rectangle in dic[piece_id]:
                pygame.draw.rect(game_board_surface, 'White', rectangle)
        elif piece_id == '0':
            for rectangle in dic[piece_id]:
                pygame.draw.rect(game_board_surface, 'White', rectangle)
        else:
            if len(dic[piece_id]) == 1:
                for rectangle in dic[piece_id]:
                    pygame.draw.rect(game_board_surface, 'Yellow', rectangle)
                    pygame.draw.rect(game_board_surface, (0, 0, 0), rectangle, 2)
                    if colorblind == True:
                        draw_colorblind(piece_id, rectangle, screen)

            else:
                new_rect = rectangles_union(piece_id, dic)
                pygame.draw.rect(game_board_surface, 'Blue', new_rect)
                pygame.draw.rect(game_board_surface, (0, 0, 0), new_rect, 2) 
                if colorblind == True:
                    draw_colorblind(piece_id, new_rect, screen)
 
# detects the piece ID where the mouse was pressed
def detect_piece_id(level, mouse_position_down):
    x_mouse_position_down, y_mouse_position_down = mouse_position_down
    x_matrix = (y_mouse_position_down - 160) // SIZE
    y_matrix = (x_mouse_position_down - 105) // SIZE
    piece_id = level.game_board[x_matrix][y_matrix]
    if piece_id in ['0', '*']:
        moving = False
    else:
        moving = True
    return piece_id, moving

#detects the mouse direction after selecting the piece
def detect_direction(mouse_position_down, mouse_position_up):
    x_mouse_position_down, y_mouse_position_down = mouse_position_down
    x_mouse_position_up, y_mouse_position_up = mouse_position_up
    x_abs, y_abs = 0, 0
    direction, x_direction, y_direction = None, None, None
    
    if x_mouse_position_up < x_mouse_position_down:
        x_direction = 'left'
        x_abs = abs(x_mouse_position_up - x_mouse_position_down)
    elif x_mouse_position_up > x_mouse_position_down:
        x_direction = 'right'
        x_abs = abs(x_mouse_position_up - x_mouse_position_down)

    if y_mouse_position_up < y_mouse_position_down:
        y_direction = 'up'
        y_abs = abs(y_mouse_position_up - y_mouse_position_down)
    elif y_mouse_position_up > y_mouse_position_down:
        y_direction = 'down'
        y_abs = abs(y_mouse_position_up - y_mouse_position_down)

    if x_abs >= y_abs:
        direction = x_direction
    else:
        direction = y_direction

    return direction

#binds pygame menu and game 
def play_game_in_pygame(screen, level, pieces, board, colorblind, search_method, max_depth):
    level_pieces = deepcopy(pieces)
    game_board = create_game_board(level_pieces, board)
    game = Game(level_pieces, game_board)
    colorblind_options = deepcopy(colorblind)

    pygame.init()
    pygame.display.set_caption("Klotski")


    game_board_surface = pygame.Surface((420,490))
    game_board_surface.fill('Cyan')
    game_board_rectangle = game_board_surface.get_rect(topleft = (105,130))
    pieces_move_surface = pygame.Surface((280, 350))
    pieces_move_rectangle = pieces_move_surface.get_rect(topleft = (175,200))

    LEVEL_NUMBER_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(318, 45), 
                                    text_input=level, font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink") 
    
    BACK_BUTTON=Button(image=None, pos=(540, 45), 
                                    text_input="BACK", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
    
    MENU_BUTTON=Button(image=None, pos=(80, 45), 
                                    text_input="MENU", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")

    HINT_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(169, 710), 
                                    text_input="HINT", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink") 
    
    QUIT_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(465, 710), 
                                    text_input="QUIT", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
    
    RETRY_BUTTON=Button(image=pygame.image.load("Resources\Images\_retry_button.png"), pos=(490, 170), 
                                    text_input=None, font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
    
    CONTINUE_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(169, 710), 
                                    text_input="CONTINUE?", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")

    CONTINUE_YES_BUTTON=Button(image=None, pos=(420, 710), 
                                    text_input="YES", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
    
    CONTINUE_NO_BUTTON=Button(image=None, pos=(510, 710), 
                                    text_input="NO", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
    
    run = True
    moving = False
    while run:
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position_down = pygame.mouse.get_pos()

                if CONTINUE_YES_BUTTON.checkForInput(mouse_position_down):
                    return 'back'

                if CONTINUE_NO_BUTTON.checkForInput(mouse_position_down):
                    pygame.quit()
                    exit()

                if QUIT_BUTTON.checkForInput(mouse_position_down):
                    pygame.quit()
                    exit()

                if BACK_BUTTON.checkForInput(mouse_position_down):
                    return 'back'
                
                if MENU_BUTTON.checkForInput(mouse_position_down):
                    return 'menu'
                    
                if HINT_BUTTON.checkForInput(mouse_position_down):
                    if game.win() == False:
                        hint = get_hint(game, search_method, max_depth)
                        HINT_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(169, 710), 
                                        text_input=hint, font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
                        colorblind = True
                    else:
                        pass

                if pieces_move_rectangle.collidepoint(mouse_position_down):
                    moving = True
                    piece_id, moving = detect_piece_id(game, mouse_position_down)

                if RETRY_BUTTON.checkForInput(mouse_position_down):
                    level_pieces = deepcopy(pieces)
                    game_board = create_game_board(level_pieces, board)
                    game = Game(level_pieces, game_board)

            elif event.type == pygame.MOUSEBUTTONUP and moving == True: 
                mouse_position_up = pygame.mouse.get_pos()
                direction = detect_direction(mouse_position_down, mouse_position_up) 
                if direction == None:
                    pass
                else:
                    stamp = False
                    if game.win() == False:
                        game.move_pieces(piece_id, direction, stamp)
                    else:
                        pass
                    HINT_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(169, 710), 
                                    text_input='HINT', font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
                    if colorblind_options == False:
                        colorblind = False
                moving = False
        screen.blit(BG, (0,0))
        screen.blit(pieces_move_surface, pieces_move_rectangle)
        screen.blit(game_board_surface, game_board_rectangle)
        draw_board(screen, game_board_surface, game.game_board, colorblind)
        screen.blit(BG_LEVEL, (0, 0))
        
        LEVEL_NUMBER_BUTTON.update(screen)

        MENU_BUTTON.changeColor(mouse_position)
        MENU_BUTTON.update(screen)

        BACK_BUTTON.changeColor(mouse_position)
        BACK_BUTTON.update(screen)

        RETRY_BUTTON.update(screen)

        HINT_BUTTON.changeColor(mouse_position)
        HINT_BUTTON.update(screen)

        if game.win() == False:
            QUIT_BUTTON.changeColor(mouse_position)
            QUIT_BUTTON.update(screen)

        if game.win() != False:
            CONTINUE_BUTTON.update(screen)

            CONTINUE_YES_BUTTON.changeColor(mouse_position)
            CONTINUE_YES_BUTTON.update(screen)

            CONTINUE_NO_BUTTON.changeColor(mouse_position)
            CONTINUE_NO_BUTTON.update(screen)

        pygame.display.update()
