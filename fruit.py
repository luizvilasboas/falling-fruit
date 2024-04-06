import pygame
import random


class Fruit(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.images = []
        self.index = 0
        self.scale = 2
        self.load_animations_fruits()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.game.SCREEN_WIDTH - self.rect.width)
        self.rect.y = -20
    
    def load_animations_fruits(self):
        fruits = [
            "sprites/items/fruits/apple.png",
            "sprites/items/fruits/bananas.png",
            "sprites/items/fruits/cherries.png",
            "sprites/items/fruits/kiwi.png",
            "sprites/items/fruits/melon.png",
            "sprites/items/fruits/orange.png",
            "sprites/items/fruits/pineapple.png",
            "sprites/items/fruits/strawberry.png"
        ]

        fruit_animation_sheet = pygame.image.load(random.choice(fruits))

        for i in range(0, fruit_animation_sheet.get_width(), 32):
            image = pygame.transform.scale(fruit_animation_sheet.subsurface((i, 0, 32, 32)), (32 * self.scale, 32 * self.scale))        
            self.images.append(image)
        
        self.image = self.images[self.index]

    def update(self):
        self.rect.y += 5

        if self.rect.top > self.game.SCREEN_HEIGHT:
            self.kill()
        
        self.index += 0.5
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]
