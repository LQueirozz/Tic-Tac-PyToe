import pygame
from config import init_Pygame, BACKGROUND_COLOR, GREEN, O_POS, X_POS
import GAME.gameManegement
from UI.screens import Menu_Screen, PVComp_Game_Screen, PVP_Game_Screen, Win_Screen, Tie_Screen

def main():
    screen = init_Pygame()
    state= GAME.gameManegement.GameState()
    clock = pygame.time.Clock()

    running= True
    while running:
        screen.fill(BACKGROUND_COLOR)
        scr= state.getCurrentState()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if isinstance(scr, Menu_Screen):
                scr.handleEvents(event, screen)

            elif isinstance(scr, PVP_Game_Screen):
                scr.handleEvents(event, screen)

            elif isinstance(scr, PVComp_Game_Screen):
                scr.handleEvents(event, screen)

        scr.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__== "__main__":
    main()