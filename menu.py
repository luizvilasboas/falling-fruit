import pygame
import math
import sys
from core.button import Button
from core.text import Text
import config


class Option:
    RUN = 0
    EXIT = 1


class Menu:
    BACKGROUND_SPEED = 0.5

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        self.screen = screen
        self.clock = clock
        self.background = pygame.image.load("sprites/background/purple.png")
        self.y_position = 0
        self.title = Text("Falling Fruit", config.FONT, 40, x=math.ceil(config.SCREEN_WIDTH / 2), y=200)
        self.button_start_game = Button("sprites/menu/buttons/button.png", 140, 70, config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2, "Iniciar", config.FONT)
        self.button_end_game = Button("sprites/menu/buttons/button.png", 140, 70, config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 100, "Sair", config.FONT)

    def draw(self) -> None:
        self.title.draw(self.screen)
        self.button_start_game.draw(self.screen)
        self.button_end_game.draw(self.screen)

    def move_background(self) -> None:
        background_width, background_height = self.background.get_rect().size
        self.y_position -= self.BACKGROUND_SPEED
        if self.y_position < -background_height:
            self.y_position = 0

        self.screen.fill((0, 0, 0))
        for x in range(0, config.SCREEN_WIDTH, background_width):
            for y in range(int(self.y_position), config.SCREEN_HEIGHT, background_height):
                self.screen.blit(self.background, (x, y))

    def run(self) -> int:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_start_game.rect.collidepoint(event.pos):
                        return Option.RUN
                    elif self.button_end_game.rect.collidepoint(event.pos):
                        return Option.EXIT

            self.move_background()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)
