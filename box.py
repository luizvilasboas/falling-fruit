import pygame
import random


class Box(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.images = []
        self.scale = 1.5
        self.load_animations()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.game.SCREEN_WIDTH - self.rect.width)
        self.rect.y = -20

    def load_animations(self):
        box_1 = pygame.image.load("sprites/items/boxes/box-1/idle.png")
        box_2 = pygame.image.load("sprites/items/boxes/box-2/idle.png")
        box_3 = pygame.image.load("sprites/items/boxes/box-3/idle.png")

        self.images = [pygame.transform.scale(x, (32 * self.scale, 32 * self.scale)) for x in [box_1, box_2, box_3]]
        self.image = self.images[random.randint(0, 2)]

    def on_hit(self):
        self.kill()

    def update(self):
        self.rect.y += 5

        if self.rect.y > self.game.SCREEN_HEIGHT:
            self.kill()
