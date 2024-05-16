import pygame
import sys
import config
from game import Game
from menu import Menu, Option


def fade_transition(screen: pygame.Surface) -> None:
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 10):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

    fade_surface.set_alpha(255)
    screen.blit(fade_surface, (0, 0))
    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_caption(config.NAME)
    screen = pygame.display.set_mode(config.WINDOW_SIZE)
    clock = pygame.time.Clock()

    while True:
        menu = Menu(screen, clock)
        option = menu.run()

        if option == Option.RUN:
            fade_transition(screen)
            game = Game(screen, clock)
            game.run()
            pygame.quit()
            sys.exit()
        elif option == Option.EXIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
