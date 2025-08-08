import pygame
import config
from UI.but import Button, ButtonManagement
from GAME import gameManegement

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
            x=220, y=200, 
            wdt= 360, hgt=80, 
            txt='Player Vs Player', font= config.MEDIUM_FONT, 
            act=self.testingClicks, bRad=40)
        
        btn2= Button(
            x=220, y=320, 
            wdt= 360, hgt=80, 
            txt='Player Vs Machine', font= config.MEDIUM_FONT, 
            act=self.testingClicks2, bRad=40)
        
        self.MG.settingUpButtons(btn1, btn2)

    def handleEvents(self, event, screen):
        self.MG.execute_All(event, screen)

    def draw(self, places: list, screen):
        title= config.BIG_FONT.render('TIC - TAC - (.PY)TOE', True, config.GREEN)
        screen.blit(title, (220, 40))
        self.MG.draw_All(screen)

class Game_Screen:
    def __init__(self, stateManeger, pos:list):
        self.lst= pos

    def handleEvents(self, event, screen):
        print('chora')

    def draw(self, places:list, screen):
        screen.fill(config.BACKGROUND_COLOR)
        pygame.draw.line(screen, config.BLACK, (200, 340), (600, 340), 12)
        pygame.draw.line(screen, config.BLACK, (340, 200), (340, 600), 12)
        pygame.draw.line(screen, config.BLACK, (200, 460), (600, 460), 12)
        pygame.draw.line(screen, config.BLACK, (460, 200), (460, 600), 12)

        for p, i in enumerate(self.lst):
            if i==1:
                X= config.X_FONT.render('X', True, config.GREEN)
                screen.blit(X, places[p])

            elif i==-1:
                pygame.draw.circle(screen, config.GREEN, places[p], 35, 10)

            elif i==0:
                continue





