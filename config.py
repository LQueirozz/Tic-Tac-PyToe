import pygame

pygame.init()
#Screen settings
SCREEN_HEIGHT=800
SCREEN_WIDTH=800
BACKGROUND_COLOR= (229, 204, 255) #REALLY Light purple

#Colors
WHITE=(255,255,255)
BLACK= (0,0,0)
GREEN= (16, 126, 129)
LIGHTER_GREEN= (35, 177, 182)
BLUE= (102, 178, 255)
LIGHTER_BLUE= (153, 204, 255)
ORANGE= (255, 161, 66)
LIGHTER_ORANGE=(255, 195, 136)
PINK= (255, 102, 178)
LIGHTER_PINK= (255, 153, 204)
PURPLE=(204, 153, 255)
LILAC= (153, 153, 255 )



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
