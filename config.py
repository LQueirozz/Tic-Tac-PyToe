import pygame

pygame.init()
#Screen settings
SCREEN_HEIGHT=800
SCREEN_WIDTH=800
BACKGROUND_COLOR= (140,192,202) #Light/greyish blue

#Colors
WHITE=(255,255,255)
GREEN= (16, 126, 129)
LIGHTER_GREEN= (45, 182, 186)
PURPLE= (150, 0, 200)
BLACK= (0,0,0)

#Positions for X's and O's in the hashtag
pos=[(280, 280), (400, 280), (560, 280), (280, 400), (400, 400), (560, 400), (280, 560), (400, 560), (560, 560)] 

#Fonts
X_FONT= pygame.font.SysFont('Arial', 60, True)
BIG_FONT= pygame.font.SysFont('Arial', 40, True)
MEDIUM_FONT= pygame.font.SysFont('Arial', 25, True)

def init_Pygame():
    pygame.init()
    screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    pygame.display.set_caption("Tic-Tac-(.PY)Toe")
    return screen
