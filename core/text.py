import pygame


class Text:
    def __init__(self, text: str, font: str, size: int, color: tuple[int, int, int] = (0, 0, 0), x: int = 0, y: int = 0) -> None:
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center=(x, y))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.text, self.rect)