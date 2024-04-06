import pygame


class PlayerSprites:
    IDLE_LEFT = 0
    IDLE_RIGHT = 1
    RUN_LEFT = 2
    RUN_RIGHT = 3


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.images = []
        self.index = 0
        self.scale = 2
        self.status = PlayerSprites.IDLE_RIGHT
        self.load_animations()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game.SCREEN_WIDTH // 2
        self.rect.bottom = self.game.SCREEN_HEIGHT
        self.lives = 3
        self.points = 0

    def load_animations(self):
        player_idle_sheet = pygame.image.load("sprites/characters/mask-dude/idle-32x32.png")
        player_run_sheet = pygame.image.load("sprites/characters/mask-dude/run-32x32.png")

        sheets = [player_idle_sheet, player_idle_sheet, player_run_sheet, player_run_sheet]

        for i in range(len(sheets)):
            image_temp = []
            for j in range(0, sheets[i].get_width(), 32):
                if i == PlayerSprites.IDLE_LEFT or i == PlayerSprites.RUN_LEFT:
                    image = pygame.transform.scale(pygame.transform.flip(sheets[i].subsurface(
                        (j, 0, 32, 32)), True, False), (32 * self.scale, 32 * self.scale))
                else:
                    image = pygame.transform.scale(sheets[i].subsurface(
                        (j, 0, 32, 32)), (32 * self.scale, 32 * self.scale))

                image_temp.append(image)
            self.images.append(image_temp)

        self.image = self.images[self.status][int(self.index)]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.status = PlayerSprites.RUN_LEFT
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.status = PlayerSprites.RUN_RIGHT
        else:
            if self.status == PlayerSprites.RUN_LEFT:
                self.status = PlayerSprites.IDLE_LEFT
            elif self.status == PlayerSprites.RUN_RIGHT:
                self.status = PlayerSprites.IDLE_RIGHT

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.game.SCREEN_WIDTH:
            self.rect.right = self.game.SCREEN_WIDTH

        self.index += 0.3
        if self.index >= len(self.images[self.status]):
            self.index = 0

        self.image = self.images[self.status][int(self.index)]
    
    def take_damage(self, damage=1):
        self.lives -= damage
    
    def is_alive(self):
        return self.lives != 0

    def add_points(self, points=1):
        self.points += points
