import pygame
import config
from core.sheet import SpriteSheet


class PlayerSprites:
    IDLE_LEFT = 0
    IDLE_RIGHT = 1
    RUN_LEFT = 2
    RUN_RIGHT = 3


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = config.SCREEN_WIDTH // 2
        self.rect.bottom = config.SCREEN_HEIGHT - 32
        self.health = 3

        player_idle_sheet = pygame.image.load(
            "sprites/characters/ninja-frog/idle-32x32.png").convert_alpha()
        player_run_sheet = pygame.image.load(
            "sprites/characters/ninja-frog/run-32x32.png").convert_alpha()

        sprites_sheet = [SpriteSheet(player_idle_sheet), SpriteSheet(player_idle_sheet), SpriteSheet(
            player_run_sheet), SpriteSheet(player_run_sheet)]

        self.player_animation_list = []
        player_animations = [11, 11, 12, 12]
        self.player_animation_action = 0

        for i, animation in enumerate(player_animations):
            temp_image_list = []

            for x in range(animation):
                if i == PlayerSprites.IDLE_LEFT or i == PlayerSprites.RUN_LEFT:
                    temp_image_list.append(pygame.transform.flip(
                        sprites_sheet[i].get_image(x, 32, 32, 2, config.BLACK), flip_x=True, flip_y=False))
                else:
                    temp_image_list.append(
                        sprites_sheet[i].get_image(x, 32, 32, 2, config.BLACK))

            self.player_animation_list.append(temp_image_list)

        self.player_animation_frame = 0
        self.player_animation_cooldown = 50
        self.player_animation_last_update = pygame.time.get_ticks()
        self.player_run_cooldown = 5
        self.player_run_counter = 0
        self.player_run_frame = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.player_animation_action = PlayerSprites.RUN_LEFT
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.player_animation_action = PlayerSprites.RUN_RIGHT
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if self.player_animation_action == PlayerSprites.RUN_LEFT:
                self.player_animation_action = PlayerSprites.IDLE_LEFT
            elif self.player_animation_action == PlayerSprites.RUN_RIGHT:
                self.player_animation_action = PlayerSprites.IDLE_RIGHT

        self.rect.x = max(
            0, min(self.rect.x, config.SCREEN_WIDTH - self.rect.width))

        current_time = pygame.time.get_ticks()

        if current_time - self.player_animation_last_update >= self.player_animation_cooldown:
            self.player_animation_frame += 1
            self.player_animation_last_update = current_time

            if self.player_animation_frame >= len(self.player_animation_list[self.player_animation_action]):
                self.player_animation_frame = 0

            self.image = self.player_animation_list[self.player_animation_action][self.player_animation_frame]

        if self.player_run_counter > self.player_run_cooldown:
            self.player_run_counter = 0
            self.player_run_frame += 1

            if self.player_run_frame >= len(self.player_animation_list[self.player_animation_action]):
                self.player_run_frame = 0

            self.image = self.player_animation_list[self.player_animation_action][self.player_run_frame]
