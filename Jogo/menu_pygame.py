import pygame
import sys
from settings import *
from play_in_pygame import *
from levels import * 
from create_board import *



BG = pygame.image.load("Resources\Images\_menu_background.png")
BG_LEVEL=pygame.image.load("Resources\Images\_background.png")

def get_font(size): 
    font = pygame.font.Font("Resources\Text\Orbitron\orbitron.ttf", size)
    return font


def run_easy(screen, game):
    game
    if game == 'back':
        easy(screen)
    elif game == 'menu':
        main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)


def run_medium(screen, game):
    game
    if game == 'back':
        medium(screen)
    elif game == 'menu':
        main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)


def run_hard(screen, game):
    game
    if game == 'back':
        hard(screen)
    elif game == 'menu':
        main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)

def easy(screen):                                          
    while True:
        DIF_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit (BG_LEVEL, (0, 0))

        EASY_BACK =Button(image=None, pos=(480, 590), text_input="BACK", 
                            font=get_font(30), base_color="Pink", hovering_color=(173, 216, 230))
        EASY_BACK.changeColor(DIF_MOUSE_POS)
        EASY_BACK.update(screen)

        LEVEL1_BUTTON = Button(image=None, pos=(200,260),
                        text_input= "LEVEL 1", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL1_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL1_BUTTON.update(screen)       

        LEVEL2_BUTTON = Button(image=None, pos=(425,260),
                        text_input= "LEVEL 2", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL2_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL2_BUTTON.update(screen)

        LEVEL3_BUTTON = Button(image=None, pos=(200,385),
                        text_input= "LEVEL 3", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL3_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL3_BUTTON.update(screen)

        LEVEL4_BUTTON = Button(image=None, pos=(425,385),
                        text_input= "LEVEL 4", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL4_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL4_BUTTON.update(screen)

        LEVEL5_BUTTON = Button(image=None, pos=(310,515),
                        text_input= "LEVEL 5", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")     
        LEVEL5_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL5_BUTTON.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BACK.checkForInput(DIF_MOUSE_POS):
                    play(screen)
                elif LEVEL1_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 1', level1_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_easy(screen, game)
                elif LEVEL2_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 2', level2_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_easy(screen, game)
                elif LEVEL3_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 3', level3_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_easy(screen, game)
                elif LEVEL4_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 4', level4_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_easy(screen, game)
                elif LEVEL5_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 5', level5_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_easy(screen, game)

        pygame.display.update()


def medium(screen):                                               
    while True:
        DIF_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit (BG_LEVEL, (0, 0))

        MEDIUM_BACK = Button(image=None, pos=(480, 590), text_input="BACK", 
                        font=get_font(30), base_color="Pink", hovering_color=(173, 216, 230))
        MEDIUM_BACK.changeColor(DIF_MOUSE_POS)
        MEDIUM_BACK.update(screen)

        LEVEL6_BUTTON = Button(image=None, pos=(200,260),
                        text_input= "LEVEL 6", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL6_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL6_BUTTON.update(screen)       

        LEVEL7_BUTTON = Button(image=None, pos=(425,260),
                        text_input= "LEVEL 7", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL7_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL7_BUTTON.update(screen)

        LEVEL8_BUTTON = Button(image=None, pos=(200,385),
                        text_input= "LEVEL 8", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL8_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL8_BUTTON.update(screen)

        LEVEL9_BUTTON = Button(image=None, pos=(425,385),
                        text_input= "LEVEL 9", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL9_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL9_BUTTON.update(screen)

        LEVEL10_BUTTON = Button(image=None, pos=(310,515),
                        text_input= "LEVEL 10", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")     
        LEVEL10_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL10_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MEDIUM_BACK.checkForInput(DIF_MOUSE_POS):
                    play(screen)
                elif LEVEL6_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 6', level6_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_medium(screen, game)
                elif LEVEL7_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 7', level7_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_medium(screen, game)
                elif LEVEL8_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 8', level8_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_medium(screen, game)
                elif LEVEL9_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 9', level9_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_medium(screen, game)
                elif LEVEL10_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 10', level10_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_medium(screen, game)                
        pygame.display.update()


def hard(screen):                                   
    while True:
        DIF_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit (BG_LEVEL, (0, 0))

        HARD_BACK = Button(image=None, pos=(480, 590), text_input="BACK", 
                        font=get_font(30), base_color="Pink", hovering_color=(173, 216, 230))
        HARD_BACK.changeColor(DIF_MOUSE_POS)
        HARD_BACK.update(screen)

        LEVEL11_BUTTON = Button(image=None, pos=(200,260),
                        text_input= "LEVEL 11", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL11_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL11_BUTTON.update(screen)       

        LEVEL12_BUTTON = Button(image=None, pos=(425,260),
                        text_input= "LEVEL 12", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL12_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL12_BUTTON.update(screen)

        LEVEL13_BUTTON = Button(image=None, pos=(200,385),
                        text_input= "LEVEL 13", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL13_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL13_BUTTON.update(screen)

        LEVEL14_BUTTON = Button(image=None, pos=(425,385),
                        text_input= "LEVEL 14", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")
        LEVEL14_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL14_BUTTON.update(screen)

        LEVEL15_BUTTON = Button(image=None, pos=(310,515),
                        text_input= "LEVEL 15", font=get_font(30), base_color=(173, 216, 230), hovering_color="Pink")     
        LEVEL15_BUTTON.changeColor(DIF_MOUSE_POS)
        LEVEL15_BUTTON.update(screen)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HARD_BACK.checkForInput(DIF_MOUSE_POS):
                    play(screen)
                elif LEVEL11_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 11', level11_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_hard(screen, game)
                elif LEVEL12_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 12', level12_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_hard(screen, game)
                elif LEVEL13_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 13', level13_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_hard(screen, game)
                elif LEVEL14_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 14', level14_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_hard(screen, game)
                elif LEVEL15_BUTTON.checkForInput(DIF_MOUSE_POS):                         
                    game = play_game_in_pygame(screen, 'LEVEL 15', level15_pieces, board, colorblind_options.colorblind, search_method.choose, max_depth_options.depth)
                    run_hard(screen, game)
        pygame.display.update()


def play(screen):
    pygame.display.set_caption("Play")
    while True:
      PLAY_MOUSE_POS = pygame.mouse.get_pos()
      screen.blit (BG_LEVEL, (0, 0))

      DIF_TEXT = get_font(30).render("CHOOSE THE DIFFICULTY", True,"white")
      DIF_RECT = DIF_TEXT.get_rect(center= (316, 200))
      screen.blit(DIF_TEXT, DIF_RECT)

 
      PLAY_BACK = Button(image =None, pos=(310, 600), 
                            text_input ="BACK", font=get_font(30), base_color="Pink", hovering_color=(173, 216, 230)) 
      PLAY_BACK.changeColor(PLAY_MOUSE_POS)
      PLAY_BACK.update(screen)

      EASY_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(230,310), 
                                    text_input="EASY", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink") 
      EASY_BUTTON.changeColor(PLAY_MOUSE_POS)
      EASY_BUTTON.update(screen)

      MEDIUM_BUTTON = Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(400,400), 
                                    text_input="MEDIUM", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink") 
      MEDIUM_BUTTON.changeColor(PLAY_MOUSE_POS)
      MEDIUM_BUTTON.update(screen)

      HARD_BUTTON = Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(230,490), 
                                    text_input="HARD", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink") 
      HARD_BUTTON.changeColor(PLAY_MOUSE_POS)
      HARD_BUTTON.update(screen)

      for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN:
                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                     main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)
             if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    easy(screen)
             if event.type == pygame.MOUSEBUTTONDOWN:
                if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    medium(screen)
             if event.type == pygame.MOUSEBUTTONDOWN:
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    hard(screen)
                     
      pygame.display.update()


def options(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method): 
    pygame.display.set_caption("Options")

    OPTIONS_BACK = Button(image=None, pos=(315,600),
                              text_input= "BACK", font=get_font(40), base_color="Pink", hovering_color=(173, 216, 230))
    
    OPTIONS_TEXT = get_font(40).render("OPTIONS", True,"white")
    DIF_RECT = OPTIONS_TEXT.get_rect(center= (316, 155))

    COLORBLIND = Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(210,245),
                              text_input= "COLORBLIND", font=get_font(20), base_color="Pink", hovering_color=(173, 216, 230))
    
    BFS = Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(210,325),
                              text_input= "BFS", font=get_font(20), base_color="Pink", hovering_color=(173, 216, 230))
    
    A_STAR = Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(210,405),
                              text_input= "A*", font=get_font(20), base_color="Pink", hovering_color=(173, 216, 230))
    
    GREEDY = Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(210,485),
                              text_input= "GREEDY", font=get_font(20), base_color="Pink", hovering_color=(173, 216, 230))
    
    DEPTH = Button(image=None, pos=(210,545),
                              text_input= "DEPTH:", font=get_font(20), base_color="Pink", hovering_color=(173, 216, 230))

    

    while True:
        OPTIONS_MOUSE_POS= pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    update_search_method(search_method)
                    main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)
                if COLORBLIND_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    colorblind_options.colorblind = True
                if COLORBLIND_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    colorblind_options.colorblind = False
                if BFS_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    bfs_options.bfs = True
                    a_star_options.a_star = False
                    greedy_options.greedy = False
                if BFS_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    bfs_options.bfs = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                if A_STAR_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    bfs_options.bfs = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                if A_STAR_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    bfs_options.bfs = False
                    a_star_options.a_star = False
                    greedy_options.greedy = True
                if GREEDY_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    bfs_options.bfs = False
                    a_star_options.a_star = False
                    greedy_options.greedy = True
                if GREEDY_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    bfs_options.bfs = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                if first_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    max_depth_options.depth = 15
                if second_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    max_depth_options.depth = 50
                if third_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    max_depth_options.depth = 100



        screen.blit (BG_LEVEL, (0, 0))

        screen.blit(OPTIONS_TEXT, DIF_RECT)

        if colorblind_options.colorblind == True:
            COLORBLIND_ON_BUTTON = Button(image=None, pos=(400,240),
                            text_input= "ON", font=get_font(20), base_color='Green', hovering_color='Pink')
            COLORBLIND_OFF_BUTTON = Button(image=None, pos=(480,240),
                                    text_input= "OFF", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        else:
            COLORBLIND_ON_BUTTON = Button(image=None, pos=(400,240),
                        text_input= "ON", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            COLORBLIND_OFF_BUTTON = Button(image=None, pos=(480,240),
                                    text_input= "OFF", font=get_font(20), base_color='Red', hovering_color='Pink')  
        COLORBLIND.update(screen)
        COLORBLIND_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        COLORBLIND_ON_BUTTON.update(screen)
        COLORBLIND_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        COLORBLIND_OFF_BUTTON.update(screen)

        if bfs_options.bfs == True:
            BFS_ON_BUTTON = Button(image=None, pos=(400,320),
                            text_input= "ON", font=get_font(20), base_color='Green', hovering_color='Pink')
            BFS_OFF_BUTTON = Button(image=None, pos=(480,320),
                                    text_input= "OFF", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        else:
            BFS_ON_BUTTON = Button(image=None, pos=(400,320),
                        text_input= "ON", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            BFS_OFF_BUTTON = Button(image=None, pos=(480,320),
                                    text_input= "OFF", font=get_font(20), base_color='Red', hovering_color='Pink')
        BFS.update(screen)
        BFS_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BFS_ON_BUTTON.update(screen)
        BFS_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BFS_OFF_BUTTON.update(screen)

        if a_star_options.a_star == True:
            A_STAR_ON_BUTTON = Button(image=None, pos=(400,400),
                            text_input= "ON", font=get_font(20), base_color='Green', hovering_color='Pink')
            A_STAR_OFF_BUTTON = Button(image=None, pos=(480,400),
                                    text_input= "OFF", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        else:
            A_STAR_ON_BUTTON = Button(image=None, pos=(400,400),
                        text_input= "ON", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            A_STAR_OFF_BUTTON = Button(image=None, pos=(480,400),
                                    text_input= "OFF", font=get_font(20), base_color='Red', hovering_color='Pink')
        A_STAR.update(screen)
        A_STAR_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        A_STAR_ON_BUTTON.update(screen)
        A_STAR_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        A_STAR_OFF_BUTTON.update(screen)

        if greedy_options.greedy == True:
            GREEDY_ON_BUTTON = Button(image=None, pos=(400,480),
                            text_input= "ON", font=get_font(20), base_color='Green', hovering_color='Pink')
            GREEDY_OFF_BUTTON = Button(image=None, pos=(480,480),
                                    text_input= "OFF", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        else:
            GREEDY_ON_BUTTON = Button(image=None, pos=(400,480),
                        text_input= "ON", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            GREEDY_OFF_BUTTON = Button(image=None, pos=(480,480),
                                    text_input= "OFF", font=get_font(20), base_color='Red', hovering_color='Pink')
        GREEDY.update(screen)
        GREEDY_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        GREEDY_ON_BUTTON.update(screen)
        GREEDY_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        GREEDY_OFF_BUTTON.update(screen)

        if max_depth_options.depth == 15:
            first_BUTTON = Button(image=None, pos=(320,545),
                            text_input= "15", font=get_font(20), base_color='Green', hovering_color='Pink')
            second_BUTTON = Button(image=None, pos=(400,545),
                                    text_input= "50", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            third_BUTTON = Button(image=None, pos=(480,545),
                            text_input= "100", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        elif max_depth_options.depth == 50:
            first_BUTTON = Button(image=None, pos=(320,545),
                            text_input= "15", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            second_BUTTON = Button(image=None, pos=(400,545),
                                    text_input= "50", font=get_font(20), base_color='Green', hovering_color='Pink')
            third_BUTTON = Button(image=None, pos=(480,545),
                            text_input= "100", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        else:
            first_BUTTON = Button(image=None, pos=(320,545),
                            text_input= "15", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            second_BUTTON = Button(image=None, pos=(400,545),
                                    text_input= "50", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            third_BUTTON = Button(image=None, pos=(480,545),
                            text_input= "100", font=get_font(20), base_color='Green', hovering_color='Pink')
        DEPTH.update(screen)
        first_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        first_BUTTON.update(screen)
        second_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        second_BUTTON.update(screen)
        third_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        third_BUTTON.update(screen)

        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)       

        update_search_method(search_method)
        pygame.display.update()


def main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method): 
    pygame.display.set_caption("Menu")
    while True:
        screen.blit (BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("MAIN MENU", True, (173, 216, 230))
        MENU_RECT = MENU_TEXT.get_rect(center= (316, 200))
        screen.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON = Button(image=None, pos=(316, 312),
                             text_input="PLAY", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
        OPTIONS_BUTTON = Button(image=None, pos=(316, 425),
                             text_input="OPTIONS", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
        QUIT_BUTTON = Button(image=None, pos=(316, 535),
                             text_input="QUIT", font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(screen)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def start_pygame():
    pygame.init()
    screen = pygame.display.set_mode((630,750))
    main_menu(screen, colorblind_options, bfs_options, a_star_options, greedy_options, max_depth_options, search_method)
