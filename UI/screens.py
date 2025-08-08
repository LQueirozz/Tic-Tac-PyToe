import pygame
import config
from UI.but import Button, ButtonManagement
from GAME import WLD

screen = config.init_Pygame()

class Menu_Screen:
    def __init__(self, stateManager):
        self.MG= ButtonManagement()
        self.state=stateManager
        self.settingUp()

    def testingClicks(self):
        print('You chose PvP!')
        self.state.switch_To_GameState()

    def testingClicks2(self):
        print('You chose PvComp!')

    def settingUp(self):
        btn1= Button(
            num= 0,
            x=220, y=200, 
            wdt= 360, hgt=80, 
            txt='Player Vs Player', font= config.MEDIUM_FONT, 
            act=self.testingClicks, bRad=40)
        
        btn2= Button(
            num=1,
            x=220, y=320, 
            wdt= 360, hgt=80, 
            txt='Player Vs Machine', font= config.MEDIUM_FONT, 
            act=self.testingClicks2, bRad=40)
        
        self.MG.settingUpButtons(btn1, btn2)

    def handleEvents(self, event, screen):
        self.MG.execute_All(event, screen)

    def draw(self, screen,):
        title= config.BIG_FONT.render('TIC - TAC - (.PY)TOE', True, config.GREEN)
        screen.blit(title, (220, 40))
        self.MG.draw_All(screen)

class Game_Screen:
    def __init__(self, stateManeger, pos:list):
        self.player_turn=1
        self.numTurns=0

        self.winning_line=0
        self.game_over=False

        self.lst= pos
        self.state=stateManeger
        self.MG= ButtonManagement()
        self.settingUp()

    def turns(self, screen):
        who= self.player_turn
        self.Player1_Rect= pygame.Rect(0, config.SCREEN_HEIGHT-80, config.SCREEN_WIDTH, 80)
        self.Player2_Rect= pygame.Rect(0, 0, config.SCREEN_WIDTH, 80)
        font= config.MEDIUM_FONT
        textSurface1= font.render('Player 1', True, (0,0,0))
        textSurface2= font.render('Player 2', True, (0,0,0))
        textRect1= textSurface1.get_rect(topleft= (10, 760))
        textRect2= textSurface2.get_rect(topleft= (10, 5))
        
        if who== 1:
            clr1= config.MEDIUM_GREEN
            clr2= config.GREEN
        else:
            clr1= config.GREEN
            clr2= config.MEDIUM_GREEN

        pygame.draw.rect(screen, clr1, self.Player1_Rect, border_top_left_radius=20, border_top_right_radius=20)
        pygame.draw.rect(screen, clr2, self.Player2_Rect, border_bottom_left_radius=20, border_bottom_right_radius=20)
        screen.blit(textSurface1, textRect1)
        screen.blit(textSurface2, textRect2)

    def where_Will_You_Place(self, screen):
        obj=self.player_turn
        alreadyPlaced= self.lst
        listOfButtons= self.MG.btnList
        mouse = pygame.mouse.get_pos()
        color= config.MEDIUM_GREEN
        inSquare=False

        for b in listOfButtons:
            if b.rect.collidepoint(mouse):
                inSquare=True
                if alreadyPlaced[b.num] !=0:
                    continue
                if obj==1:
                    X= config.X_FONT.render('X', True, color)
                    screen.blit(X, config.X_POS[b.num])
                elif obj==-1:
                    pygame.draw.circle(screen, color, config.O_POS[b.num], config.O_RADIUS , 20)
                break
                
        if not inSquare:
            if obj==1:
                X= config.X_FONT.render('X', True, color)
                screen.blit(X, mouse)
            elif obj==-1:
                pygame.draw.circle(screen, color, mouse, config.O_RADIUS , 20)


    def settingUp(self):
        INITIAL_POS= 200
        DIMENSION= 130

        for i in range(0, 9, 1):
            btn= Button(
                num=i,
                x=INITIAL_POS + (i%3)*(DIMENSION+20),
                y= INITIAL_POS + (i//3)*(DIMENSION+20),
                wdt= DIMENSION,
                hgt=DIMENSION, 
                txt='', font= config.MEDIUM_FONT, 
                act=lambda num=i: self.place_object(num), bRad=40)
        
            self.MG.settingUpButtons(btn)

    def handleEvents(self, event, screen):
        self.MG.execute_All(event, screen)

    def draw(self, Xplaces:list, Oplaces: list ,screen):
        screen.fill(config.BACKGROUND_COLOR)
        pygame.draw.line(screen, config.BLACK, (190, 330), (610, 330), 12) #Horizontal top
        pygame.draw.line(screen, config.BLACK, (190, 470), (610, 470), 12) #Horizontal bottom

        pygame.draw.line(screen, config.BLACK, (330, 190), (330, 610), 12) #Vertical left
        pygame.draw.line(screen, config.BLACK, (470, 190), (470, 610), 12) #Vertical right

        for p, i in enumerate(self.lst):
            if i==1:
                X= config.X_FONT.render('X', True, config.GREEN)
                screen.blit(X, Xplaces[p])

            elif i==-1:
                pygame.draw.circle(screen, config.GREEN, Oplaces[p], config.O_RADIUS , 20)

            elif i==0:
                continue

        if not self.game_over:
            self.where_Will_You_Place(screen)

        self.turns(screen)

        if self.game_over:
            if self.winner != 0:
                self.Win_Screen(screen, self.winning_line)
            else:  
                self.Tie_Screen(screen)
    
    def place_object(self, Num: int):
        if self.game_over==False:
            if self.lst[Num]==0:
                self.lst[Num]= self.player_turn

            win_coords = WLD.Win_Or_Draw.Win(self.lst)
            if len(win_coords) != 0:
                self.game_over = True
                self.winner = self.player_turn
                self.winning_line = WLD.Win_Or_Draw.Calculate_Line(win_coords)

            elif WLD.Win_Or_Draw.Tie(self.lst):
                self.game_over = True
                self.winner = 0

            else:
                self.player_turn*=-1 

            self.draw(config.X_POS, config.O_POS, screen)

    def Win_Screen(self, screen, coordinates: list):
        if self.winner==1:
            center= self.Player1_Rect.center
        elif self.winner==-1:
            center=self.Player2_Rect.center

        font= config.BIG_FONT
        textSurface= font.render('WINNER!', True, (0,0,0))
        textRect= textSurface.get_rect(center=center)
        screen.blit(textSurface, textRect)
        start= coordinates[0]
        end= coordinates[1]
        pygame.draw.line(screen, config.DARK_PINK, start, end, 8)


    def Tie_Screen(self, screen):
        center1= self.Player1_Rect.center
        center2=self.Player2_Rect.center

        font= config.BIG_FONT
        textSurface1= font.render('TIE!', True, (0,0,0))
        textRect1= textSurface1.get_rect(center=center1)
        screen.blit(textSurface1, textRect1)

        textSurface2= font.render('TIE!', True, (0,0,0))
        textRect2= textSurface2.get_rect(center=center2)
        screen.blit(textSurface2, textRect2)







    


        
 

    





