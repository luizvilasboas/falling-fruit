import pygame
import random
from player import Player
from box import Box
from fruit import Fruit


class FruitCollectionAnimation(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.images = []
        self.index = 0
        self.scale = 2
        self.load_animation_fruit_collection()
        self.rect.x = x
        self.rect.y = y

    def load_animation_fruit_collection(self):
        fruit_collection_animation_sheet = pygame.image.load("sprites/items/fruits/collected.png")

        for i in range(0, fruit_collection_animation_sheet.get_width(), 32):
            image = pygame.transform.scale(fruit_collection_animation_sheet.subsurface(
                (i, 0, 32, 32)), (32 * self.scale, 32 * self.scale))
            self.images.append(image)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

    def update(self):
        self.index += 0.5
        if self.index >= len(self.images):
            self.index = 0
            self.kill()

        self.image = self.images[int(self.index)]


class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.LIGHT_BLUE = (0, 150, 255)
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Falling Fruit")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.fruits_sprites = pygame.sprite.Group()
        self.boxes_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.points = 0
        self.lives = 3

    def generate_fruit(self):
        fruits = Fruit(self)
        self.all_sprites.add(fruits)
        self.fruits_sprites.add(fruits)

    def generate_boxes(self):
        box = Box(self)
        self.all_sprites.add(box)
        self.boxes_sprites.add(box)

    def run(self):
        running = True
        fruit_collection_animation = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()

            hitted_boxes = pygame.sprite.spritecollide(self.player, self.boxes_sprites, True)
            for _ in hitted_boxes:
                self.lives -= 1

                if self.lives == 0:
                    running = False

            hitted_fruits = pygame.sprite.spritecollide(self.player, self.fruits_sprites, True)
            for fruit in hitted_fruits:
                self.points += 1

                if fruit_collection_animation is None:
                    fruit_collection_animation = FruitCollectionAnimation(
                        self, fruit.rect.x, fruit.rect.y)
                    self.all_sprites.add(fruit_collection_animation)

            if fruit_collection_animation:
                fruit_collection_animation.update()
                fruit_collection_animation = None

            if random.randint(1, 100) == 1:
                self.generate_fruit()
            if random.randint(1, 50) == 1:
                self.generate_boxes()

            self.screen.fill(self.LIGHT_BLUE)
            self.all_sprites.draw(self.screen)

            font = pygame.font.SysFont(None, 30)

            points_text = font.render(f"Pontuação: {self.points}", True, self.BLACK)
            lives_text = font.render(f"Vidas: {self.lives}", True, self.BLACK)

            self.screen.blit(points_text, (10, 10))
            self.screen.blit(lives_text, (self.SCREEN_WIDTH - lives_text.get_width() - 10, 10))

            pygame.display.flip()

            self.clock.tick(self.FPS)


pygame.quit()
