import pygame
from config import init_Pygame, BACKGROUND_COLOR, GREEN, pos
import GAME.gameManegement
from UI.screens import Menu_Screen

def main():
    screen = init_Pygame()
    state= GAME.gameManegement.GameState()
    clock = pygame.time.Clock()

    running= True
    while running:
        scr= state.getCurrentState()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            scr.handleEvents(event, screen)


        screen.fill(BACKGROUND_COLOR)
        scr.draw(pos, screen)
        pygame.display.flip()

        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__== "__main__":
    main()