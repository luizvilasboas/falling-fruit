import pygame
import config
import random


class Object(pygame.sprite.Sprite):
    def __init__(self, color=config.WHITE, score=1):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(config.SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(3, 6)
        self.score = score

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > config.SCREEN_HEIGHT:
            self.kill()
