import pygame

pygame.init()
#Screen settings
SCREEN_HEIGHT=800
SCREEN_WIDTH=800
BACKGROUND_COLOR= (140,192,202) #Light/greyish blue

#Colors
WHITE=(255,255,255)
GREEN= (16, 126, 129)
MEDIUM_GREEN= (35, 177, 182)
LIGHTER_GREEN= (45, 182, 186)
PURPLE= (150, 0, 200)
PINK= (230, 164, 217)
DARK_PINK= (245, 73, 210)
BLACK= (0,0,0)

#Positions for O's in the hashtag
O_POS=[(260, 260), (400, 260), (540, 260), (260, 400), (400, 400), (540, 400), (260, 540), (400, 540), (540, 540)] 
X_POS=[(220, 220), (360, 220), (500, 220), (220, 360), (360, 360), (500, 360), (220, 500), (360, 500), (500, 500)]
LINE_POS= [(200,200), (400, 200), (600, 200), (200, 400), (400, 400), (600,400), (200,600), (400, 600), (600,600)]
O_RADIUS= 45

#Fonts
X_FONT= pygame.font.SysFont('Boulder', 150, True)
BIG_FONT= pygame.font.SysFont('Arial', 40, True)
MEDIUM_FONT= pygame.font.SysFont('Arial', 25, True)
SMALL_FONT= pygame.font.SysFont('Arial',20)

def init_Pygame():
    pygame.init()
    screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    pygame.display.set_caption("Tic-Tac-(.PY)Toe")
    return screen
