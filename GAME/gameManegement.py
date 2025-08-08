import pygame
import config
import UI.but




class GameState():
    def __init__(self):
        abc=[0,0,0,0,0,0,0,0,0]
        from UI.screens import Menu_Screen, Game_Screen
        self.menuScreen= UI.screens.Menu_Screen(self)
        self.gameScreen= UI.screens.Game_Screen(self, abc)
        self.currentState= "menu"

    def switch_To_GameState(self):
        if self.currentState== "menu":
            self.currentState= "game"

    def switch_To_MenuState(self):
        if self.currentState=="game":
            self.currentState="menu"

    def getCurrentState(self):
        if self.currentState== "menu":
            return self.menuScreen

        if self.currentState=="game":
            return self.gameScreen


    