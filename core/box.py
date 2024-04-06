import pygame

class Box:
    @staticmethod
    def draw(screen, box_color, border_color, x, y, width, height):
        pygame.draw.rect(screen, box_color, (x, y, width, height))
        pygame.draw.rect(screen, border_color, (x + 2, y + 2, width - 4, height - 4))