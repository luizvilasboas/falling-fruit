import pygame
import random
from player import Player
from box import Box
from fruit import Fruit
from core.box import Box as BoxUI
from core.text import Text as TextUI

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
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND_SPEED = 0.2

    def __init__(self):
        self.background = pygame.image.load(random.choice(["sprites/background/blue.png", "sprites/background/brown.png", "sprites/background/gray.png", "sprites/background/green.png", "sprites/background/pink.png", "sprites/background/purple.png", "sprites/background/yellow.png"]))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.fruits_sprites = pygame.sprite.Group()
        self.boxes_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.points = 0
        self.lives = 3
        self.y_position = 0

    def generate_fruit(self):
        if random.randint(1, 100) == 1:
            fruits = Fruit(self)
            self.all_sprites.add(fruits)
            self.fruits_sprites.add(fruits)

    def generate_boxes(self):
        if random.randint(1, 50) == 1:
            box = Box(self)
            self.all_sprites.add(box)
            self.boxes_sprites.add(box)

    def clicked_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        return True

    def collided(self, object_1, object_2):
        return pygame.sprite.spritecollide(object_1, object_2, True)

    def animate_fruit_collection(self, fruit):
        fruit_collection_animation = FruitCollectionAnimation(self, fruit.rect.x, fruit.rect.y)
        self.all_sprites.add(fruit_collection_animation)
        return fruit_collection_animation

    def move_background(self):
        background_width, background_height = self.background.get_rect().size

        self.y_position -= self.BACKGROUND_SPEED
        if self.y_position < -background_height:
            self.y_position = 0
            
        self.screen.fill((0, 0, 0))

        for x in range(0, self.SCREEN_WIDTH, background_width):
            for y in range(int(self.y_position), self.SCREEN_HEIGHT, background_height):
                self.screen.blit(self.background, (x, y))

    def draw_ui(self):
        import pygame
import random
from player import Player
from box import Box
from fruit import Fruit
from core.box import Box as BoxUI
from core.text import Text as TextUI

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
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND_SPEED = 0.2

    def __init__(self):
        self.background = pygame.image.load(random.choice(["sprites/background/blue.png", "sprites/background/brown.png", "sprites/background/gray.png", "sprites/background/green.png", "sprites/background/pink.png", "sprites/background/purple.png", "sprites/background/yellow.png"]))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.fruits_sprites = pygame.sprite.Group()
        self.boxes_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.points = 0
        self.lives = 3
        self.y_position = 0

    def generate_fruit(self):
        if random.randint(1, 100) == 1:
            fruits = Fruit(self)
            self.all_sprites.add(fruits)
            self.fruits_sprites.add(fruits)

    def generate_boxes(self):
        if random.randint(1, 50) == 1:
            box = Box(self)
            self.all_sprites.add(box)
            self.boxes_sprites.add(box)

    def clicked_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        return True

    def collided(self, object_1, object_2):
        return pygame.sprite.spritecollide(object_1, object_2, True)

    def animate_fruit_collection(self, fruit):
        fruit_collection_animation = FruitCollectionAnimation(self, fruit.rect.x, fruit.rect.y)
        self.all_sprites.add(fruit_collection_animation)
        return fruit_collection_animation

    def move_background(self):
        background_width, background_height = self.background.get_rect().size

        self.y_position -= self.BACKGROUND_SPEED
        if self.y_position < -background_height:
            self.y_position = 0
            
        self.screen.fill((0, 0, 0))

        for x in range(0, self.SCREEN_WIDTH, background_width):
            for y in range(int(self.y_position), self.SCREEN_HEIGHT, background_height):
                self.screen.blit(self.background, (x, y))

    def draw_ui(self):
        font = pygame.font.Font("font/pixelify-sans-variable-font.ttf", 30)

        points_text = font.render(f"Pontuação: {self.player.points}", 30, self.BLACK)
        lives_text = font.render(f"Vidas: {self.player.lives}", 30, self.BLACK)

        BoxUI.draw(self.screen, self.BLACK, self.WHITE, 0, 0, points_text.get_width() + 25, points_text.get_height() + 25)
        self.screen.blit(points_text, (10, 10))
        BoxUI.draw(self.screen, self.BLACK, self.WHITE, self.SCREEN_WIDTH - lives_text.get_width() - 20, 0, self.SCREEN_WIDTH, lives_text.get_height() + 25)
        self.screen.blit(lives_text, (self.SCREEN_WIDTH - lives_text.get_width() - 10, 10))

    def run(self):
        pygame.init()
        pygame.display.set_caption("Falling Fruit")

        running = True
        fruit_collection_animation = None
        while running:
            if not self.clicked_exit():
                running = False

            hitted_boxes = self.collided(self.player, self.boxes_sprites)
            for _ in hitted_boxes:
                self.player.take_damage()

                if not self.player.is_alive():
                    running = False

            hitted_fruits = self.collided(self.player, self.fruits_sprites)
            for fruit in hitted_fruits:
                self.player.add_points()

                if fruit_collection_animation is None:
                    fruit_collection_animation = self.animate_fruit_collection(fruit)

            if fruit_collection_animation:
                fruit_collection_animation.update()
                fruit_collection_animation = None

            self.generate_fruit()
            self.generate_boxes()
            self.move_background()
            self.draw_ui()

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()


    def run(self):
        pygame.init()
        pygame.display.set_caption("Falling Fruit")

        running = True
        fruit_collection_animation = None
        while running:
            if not self.clicked_exit():
                running = False

            self.all_sprites.update()

            hitted_boxes = self.collided(self.player, self.boxes_sprites)
            for _ in hitted_boxes:
                self.player.take_damage()

                if not self.player.is_alive():
                    running = False

            hitted_fruits = self.collided(self.player, self.fruits_sprites)
            for fruit in hitted_fruits:
                self.player.add_points()

                if fruit_collection_animation is None:
                    fruit_collection_animation = self.animate_fruit_collection(fruit)

            if fruit_collection_animation:
                fruit_collection_animation.update()
                fruit_collection_animation = None

            self.generate_fruit()
            self.generate_boxes()
            self.move_background()
            self.draw_ui()

            self.all_sprites.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
