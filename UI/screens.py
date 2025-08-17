import pygame
import config
from UI.but import Button, ButtonManagement
from GAME import WLD

screen = config.init_Pygame()

def basicGameScreen(turn, lst: list, screen, comp=0):
    screen.fill(config.BACKGROUND_COLOR)
    Player1_Rect= pygame.Rect(0, config.SCREEN_HEIGHT-80, config.SCREEN_WIDTH, 80)
    Player2_Rect= pygame.Rect(0, 0, config.SCREEN_WIDTH, 80)
    font= config.MEDIUM_FONT
    if comp==1:
        textSurface1= font.render('Computer', True, (0,0,0))
        textSurface2= font.render('Player (you)', True, (0,0,0))

    elif comp==-1:
        textSurface1= font.render('Player (you)', True, (0,0,0))
        textSurface2= font.render('Computer', True, (0,0,0))

    elif comp==0:
        textSurface1= font.render('Player 1', True, (0,0,0))
        textSurface2= font.render('Player 2', True, (0,0,0))


    textRect1= textSurface1.get_rect(topleft= (10, 760))
    textRect2= textSurface2.get_rect(topleft= (10, 5))
        
    if turn== 1:
        clr1= colors(1, False)
        clr2= colors(2, True)
    elif turn==-1:
        clr1= colors(1, True)
        clr2= colors(2, False)
    else:
        clr1= colors(1, False)
        clr2= colors(2, False)

    pygame.draw.rect(screen, clr1, Player1_Rect, border_top_left_radius=20, border_top_right_radius=20)
    pygame.draw.rect(screen, clr2, Player2_Rect, border_bottom_left_radius=20, border_bottom_right_radius=20)
    screen.blit(textSurface1, textRect1)
    screen.blit(textSurface2, textRect2)

    pygame.draw.line(screen, config.BLACK, (190, 330), (610, 330), 12) #Horizontal top
    pygame.draw.line(screen, config.BLACK, (190, 470), (610, 470), 12) #Horizontal bottom

    pygame.draw.line(screen, config.BLACK, (330, 190), (330, 610), 12) #Vertical left
    pygame.draw.line(screen, config.BLACK, (470, 190), (470, 610), 12) #Vertical right

    for p, i in enumerate(lst):
        if i==1:
            X= config.X_FONT.render('X', True, colors(1, False))
            screen.blit(X, config.X_POS[p])

        elif i==-1:
            pygame.draw.circle(screen, colors(2, False), config.O_POS[p], config.O_RADIUS , 20)

        elif i==0:
            continue


class Menu_Screen:
    def __init__(self, stateManager):
        self.MG= ButtonManagement()
        self.state=stateManager
        self.settingUp()

    def Start_PVP(self):
        #print('You chose PvP!')
        self.state.switch_To_PVPGameState()

    def Start_PVCOMP(self):
        #print('You chose PvComp!')
        self.state.switch_To_PVCOMPGameState()

    def settingUp(self):
        btn1= Button(
            num= 0, clr= config.PURPLE,
            x=220, y=200, 
            wdt= 360, hgt=80, 
            txt='Player Vs Player', font= config.MEDIUM_FONT, 
            act=self.Start_PVP, bRad=40)
        
        btn2= Button(
            num=1, clr= config.PURPLE,
            x=220, y=320, 
            wdt= 360, hgt=80, 
            txt='Player Vs Machine', font= config.MEDIUM_FONT, 
            act=self.Start_PVCOMP, bRad=40)
        
        self.MG.settingUpButtons(btn1, btn2)

    def handleEvents(self, event, screen):
        self.MG.execute_All(event, screen)

    def draw(self, screen,):
        title= config.BIG_FONT.render('TIC - TAC - (.PY)TOE', True, config.BLACK)
        screen.blit(title, (220, 40))
        self.MG.draw_All(screen)

class PVP_Game_Screen:
    def __init__(self, stateManeger, pos:list):
        self.player_turn=1
        self.game_over=False
        self.board= pos
        self.state=stateManeger
        self.MG= ButtonManagement()
        self.settingUp()

    def where_Will_You_Place(self, screen):
        obj=self.player_turn
        alreadyPlaced= self.board
        listOfButtons= self.MG.btnList
        mouse = pygame.mouse.get_pos()
        colorX= colors(1, True)
        colorO= colors(2, True)
        inSquare=False

        for b in listOfButtons:
            if b.rect.collidepoint(mouse):
                inSquare=True
                if alreadyPlaced[b.num] !=0:
                    continue
                if obj==1:
                    X= config.X_FONT.render('X', True, colorX)
                    screen.blit(X, config.X_POS[b.num])
                elif obj==-1:
                    pygame.draw.circle(screen, colorO, config.O_POS[b.num], config.O_RADIUS , 20)
                break
                
        if not inSquare:
            if obj==1:
                X= config.X_FONT.render('X', True, colorX)
                screen.blit(X, mouse)
            elif obj==-1:
                pygame.draw.circle(screen, colorO, mouse, config.O_RADIUS , 20)


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

    def draw(self, screen):
        basicGameScreen(self.player_turn, self.board, screen)
        if not self.game_over:
            self.where_Will_You_Place(screen)
    
    def place_object(self, Num: int):
        if self.game_over==False:
            if self.board[Num]==0:
                self.board[Num]= self.player_turn

            win_coords = WLD.Win_Or_Draw.Win(self.board)
            if len(win_coords) != 0:
                self.game_over = True
                self.state.switch_To_WinState()

            elif WLD.Win_Or_Draw.Tie(self.board):
                self.game_over = True
                self.state.switch_To_TieState()                

            else:
                self.player_turn*=-1    
                self.draw(screen)

class Win_Screen:
    def __init__(self, stateManager, lst:list, comp=0):
        self.state=stateManager
        self.board= lst
        self.comp=comp
       
    def draw(self, screen):
        self.winner= WLD.Win_Or_Draw.WhoWon(self.board)
        coordinates = WLD.Win_Or_Draw.Win(self.board)
        winning_line = WLD.Win_Or_Draw.Calculate_Line(coordinates)
        basicGameScreen(self.winner, self.board, screen, self.comp)
        font= config.BIG_FONT
        textSurface= font.render('WINNER!', True, (0,0,0))

        if self.winner== 1:
            c= (400, 760)

        else:
            c=(400,40)
        textRect= textSurface.get_rect(center=c)
        screen.blit(textSurface, textRect)
        start= winning_line[0]
        end= winning_line[1]
        pygame.draw.line(screen, config.ORANGE, start, end, 8)


class Tie_Screen:
    def __init__(self, stateManager, lst, comp: int=0):
        self.state= stateManager
        self.board=lst
        self.comp=comp
    def draw(self, screen):
        basicGameScreen(0, self.board, screen, self.comp)
        center1= (400, 760)
        center2= (400, 40)

        font= config.BIG_FONT
        textSurface1= font.render('TIE!', True, (0,0,0))
        textRect1= textSurface1.get_rect(center=center1)
        screen.blit(textSurface1, textRect1)

        textSurface2= font.render('TIE!', True, (0,0,0))
        textRect2= textSurface2.get_rect(center=center2)
        screen.blit(textSurface2, textRect2)

class PVComp_Game_Screen:
    def __init__(self, stateManager, pos:list):
        from GAME import compAlg
        self.player_turn=1
        self.comp= self.defineNums()
        self.player= -1* self.comp
        self.computer= compAlg.computer(pos, self.comp)
        self.game_over=False
        self.board= pos
        self.state=stateManager
        self.MG= ButtonManagement()
        self.settingUp()

    def defineNums(self):
        from random import randint
        comp= randint(1,2)
        if comp==2:
            comp=-1

        return comp

    def where_Will_You_Place(self, screen):
        obj=self.player
        alreadyPlaced= self.board
        listOfButtons= self.MG.btnList
        mouse = pygame.mouse.get_pos()
        colorX= colors(1, True)
        colorO= colors(2, True)
        inSquare=False

        for b in listOfButtons:
            if b.rect.collidepoint(mouse):
                inSquare=True
                if alreadyPlaced[b.num] !=0:
                    continue
                if obj==1:
                    X= config.X_FONT.render('X', True, colorX)
                    screen.blit(X, config.X_POS[b.num])
                elif obj==-1:
                    pygame.draw.circle(screen, colorO, config.O_POS[b.num], config.O_RADIUS , 20)
                break
                
        if not inSquare:
            if obj==1:
                X= config.X_FONT.render('X', True, colorX)
                screen.blit(X, mouse)
            elif obj==-1:
                pygame.draw.circle(screen, colorO, mouse, config.O_RADIUS , 20)


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

    def computerTurn(self):
        m = self.computer.Best_Score()
        self.board[m]=self.comp

    def computerPlay(self):
        from time import time
        if self.player_turn == self.comp:
            #If you want the computer to look like it's thinking:
            """if not hasattr(self, 'start_thinking_time'):
                self.start_thinking_time= time()

            elif time()- self.start_thinking_time >= 1.0:
                self.computerTurn()
                self.player_turn= -1*self.player_turn
                delattr(self, 'start_thinking_time')"""

            #if not:
            self.computerTurn()
            self.player_turn= -1*self.player_turn
        win_coords = WLD.Win_Or_Draw.Win(self.board)
        if len(win_coords) != 0:
            self.game_over = True
            self.state.switch_To_WinState()

        elif WLD.Win_Or_Draw.Tie(self.board):
            self.game_over = True
            self.state.switch_To_TieState()   

    def draw(self, screen):
        basicGameScreen(self.player_turn, self.board, screen, comp= self.comp)
        if self.player_turn == self.comp:             
            self.computerPlay()
        else:
            if not self.game_over:
                self.where_Will_You_Place(screen)
    
    def place_object(self, Num: int):
        if self.game_over==False and self.player_turn==self.player:
            if self.board[Num]==0:
                self.board[Num]= self.player_turn

            win_coords = WLD.Win_Or_Draw.Win(self.board)
            if len(win_coords) != 0:
                self.game_over = True
                self.state.switch_To_WinState()

            elif WLD.Win_Or_Draw.Tie(self.board):
                self.game_over = True
                self.state.switch_To_TieState()                

            else:
                self.player_turn*=-1    
        
        self.draw(screen)
    
        

def colors(num: int, light: bool):
    if num==1 and light:
        return config.LIGHTER_BLUE
        
    if num==1 and not light:
        return config.BLUE
        
    if num==2 and light:
        return config.LIGHTER_PINK
        
    if num==2 and not light:
        return config.PINK
    







    


        
 

    





