import pygame
import config

class Button():
    def __init__(self, num, x, y, wdt, hgt, txt, font, act, textColor=config.WHITE, clr= config.GREEN, bRad: int=-1):
        """
        -> x and y coordinates
        -> width and height
        -> txt: text, text color, text font
        -> act: function to do when clicked
        -> clr: button color
        -> bRad: borderRadius
        """
        self.rect= pygame.Rect(x, y, wdt, hgt)
        self.text= txt
        self.tColor=textColor
        self.font=font
        self.action= act
        self.color= clr
        self.border= bRad
        self.num=num

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius= self.border)
        font= self.font
        textSurface= font.render(self.text, True, self.tColor)
        textRect= textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)

    def doTheThing(self, event, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color= config.LILAC    
            self.draw(screen)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.action()

        else:
            self.color= config.PURPLE
            self.draw(screen)


class ButtonManagement():
    def __init__(self):
        self.btnList= []

    def settingUpButtons(self, *butn: Button):
        for b in butn:
            self._add(b)

    def _add(self, btn: Button):
        if btn not in self.btnList:
            self.btnList.append(btn)

    def draw(self, screen, btn: Button):
        btn.draw(screen)

    def draw_All(self, screen):
        for b in self.btnList:
            b.draw(screen)

    def execute(self, btn: Button, event, screen):
        btn.doTheThing(event, screen)

    def execute_All(self, event, screen):
        for b in self.btnList:
            b.doTheThing(event, screen)

    def rmv(self, btn: Button):
        self.btnList.remove(btn)

    def clearAll(self):
        self.btnList=[]