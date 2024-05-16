import pygame
import sys
import math

class Button:
    def __init__(self, image: str, width: int, height: int, x: int, y: int, text: str, font: str, text_color: tuple[int, int, int] = (0, 0, 0)) -> None:
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.text = Text(text, font, 30, text_color, self.rect.centerx, self.rect.centery)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
        self.text.draw(screen)


class Text:
    def __init__(self, text: str, font: str, size: int, color: tuple[int, int, int] = (0, 0, 0), x: int = 0, y: int = 0) -> None:
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center=(x, y))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.text, self.rect)

class Menu:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BLACK = (0, 0, 0)
    WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    BACKGROUND_SPEED = 0.5

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.background = pygame.image.load("sprites/background/purple.png")
        pygame.display.set_caption("Menu do Jogo")

        self.FONT = "font/font.otf"
        self.TITLE_FONT_SIZE = 48
        self.OPTION_FONT_SIZE = 36
        self.y_position = 0

        self.button_start_game = Button("sprites/menu/buttons/button.png", 140, 70, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, "Iniciar", self.FONT)
        self.button_end_game = Button("sprites/menu/buttons/button.png", 140, 70, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 + 100, "Sair", self.FONT)

    def draw(self):
        title_text = pygame.font.Font(self.FONT, self.TITLE_FONT_SIZE).render("Falling Fruit", True, self.BLACK)
        title_rect = title_text.get_rect(center=(math.ceil(self.SCREEN_WIDTH / 2), 200))
        self.screen.blit(title_text, title_rect)

        self.button_start_game.draw(self.screen)
        self.button_end_game.draw(self.screen)

    def move_background(self):
        background_width, background_height = self.background.get_rect().size
        self.y_position -= self.BACKGROUND_SPEED
        if self.y_position < -background_height:
            self.y_position = 0

        self.screen.fill((0, 0, 0))
        for x in range(0, self.SCREEN_WIDTH, background_width):
            for y in range(int(self.y_position), self.SCREEN_HEIGHT, background_height):
                self.screen.blit(self.background, (x, y))

    def main(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_start_game.rect.collidepoint(event.pos):
                        print("Iniciando...")
                    elif self.button_end_game.rect.collidepoint(event.pos):
                        print("Saindo...")

            self.move_background()
            self.draw()
            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    menu = Menu()
    menu.main()
