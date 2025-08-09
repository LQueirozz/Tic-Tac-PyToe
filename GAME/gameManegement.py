import pygame
import config
import UI.but

class GameState():
    def __init__(self):
        self.abc=[0, 0, 0 , 0, 0, 0, 0, 0, 0]
        from UI.screens import Menu_Screen, PVP_Game_Screen, PVComp_Game_Screen, Win_Screen, Tie_Screen
        self.menuScreen= Menu_Screen(self)
        self.PVPgameScreen= PVP_Game_Screen(self, self.abc)
        self.PVCOMPgameScreen= PVComp_Game_Screen(self, self.abc)
        compId= self.PVCOMPgameScreen.comp
        self.WinScreen=Win_Screen(self, self.abc, compId)
        self.TieState= Tie_Screen(self, self.abc)
        self.Numturn=1

        self.currentState= ["menu"]

    def changeTurn(self):
        self.Numturn+=1

    def switch_To_PVPGameState(self):
        self.currentState.append("PVPgame")
        
    def switch_To_PVCOMPGameState(self):
        self.currentState.append( "PVCOMPgame")

    def switch_To_MenuState(self):
        self.currentState.append("PVPmenu")

    def switch_To_WinState(self):
        self.currentState.append("WIN")

    def switch_To_TieState(self):
        self.currentState.append('TIE')

    def getCurrentState(self):
        if self.currentState[-1]== "menu":
            return self.menuScreen

        if self.currentState[-1]=="PVPgame":
            return self.PVPgameScreen
        
        if self.currentState[-1]=="PVCOMPgame":
            return self.PVCOMPgameScreen
        
        if self.currentState[-1]=="WIN":
            return self.WinScreen
        
        if self.currentState[-1]== 'TIE':
            return self.TieState



    