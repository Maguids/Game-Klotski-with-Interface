# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARKGREY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOUR = BLACK

#game settings
WIDTH = 630 
HEIGHT = 750 
FPS= 60 
title = "PuzzlePacked IQ Games"
TILESIZE = 70 
GAME_SIZE = 4 

#menu buttons
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos [0]
        self.y_pos = pos [1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image= self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect =self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update (self, screen):
        #update the button on the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)    
        screen.blit(self.text, self.text_rect)

    def checkForInput(self,position):
        #Check if the position passed as a parameter is inside the button
        if position [0] in range (self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
       #Change the color of the button to the hovering color if the mouse cursor is over it
        if position [0] in range (self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text= self.font.render(self.text_input, True, self.base_color)


#define colorblind 'on' or'off'
class _Colorblind_():
    def __init__(self, colorblind):
        self.colorblind = colorblind

colorblind = False
colorblind_options = _Colorblind_(colorblind)


#define bfs 'on' or 'off'
class _BFS_():
    def __init__(self, bfs):
        self.bfs = bfs
    
bfs = False
bfs_options = _BFS_(bfs)

#define A* 'on' or 'off'
class _A_STAR_():
    def __init__(self, a_star):
        self.a_star = a_star
    
a_star = True
a_star_options = _A_STAR_(a_star)

#define greedy 'on' or 'off'
class _GREEDY_():
    def __init__(self, greedy):
        self.greedy = greedy
    
greedy = False
greedy_options = _GREEDY_(greedy)


#define the search method being used:
class _SEARCH_METHOD_():
    def __init__(self, search_method):
        self.choose = search_method

search_method = _SEARCH_METHOD_('bfs')

def update_search_method(search_method):
    if bfs_options.bfs == True:
        search_method.choose = 'bfs'
    elif a_star_options.a_star == True:
        search_method.choose = 'a_star'
    elif greedy_options.greedy == True:
        search_method.choose = 'greedy'


#define the max depth of the nodes
class _DEPTH_():
    def __init__(self, depth):
        self.depth = depth
    
max_depth = 50
max_depth_options = _DEPTH_(max_depth)
