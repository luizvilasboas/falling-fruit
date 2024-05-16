import pygame
from .text import Text


class Button:
    def __init__(self, image: str, width: int, height: int, x: int, y: int, text: str, font: str, text_color: tuple[int, int, int] = (0, 0, 0)) -> None:
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.text = Text(text, font, 30, text_color, self.rect.centerx + 2, self.rect.centery)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
        self.text.draw(screen)
