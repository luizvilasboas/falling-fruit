import pygame
import random
from core.text import Text
import config
from player import Player
from object import Object

pygame.init()


def main():
    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Come Ponto")
    clock = pygame.time.Clock()

    score = 0
    score_pos_x = 60
    score_pos_y = 10

    all_sprites = pygame.sprite.Group()
    points = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.randint(0, 100) < 5:
            point_type = random.choice(["normal", "health", "damage"])
            if point_type == "normal":
                new_point = Object(config.WHITE, 1)
            elif point_type == "health":
                new_point = Object(config.GREEN, 0)
            elif point_type == "damage":
                new_point = Object(config.BLUE, -1)
            all_sprites.add(new_point)
            points.add(new_point)

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, points, True)
        for hit in hits:
            score += hit.score
            if hit.score < 0:
                player.health += hit.score
                if player.health <= 0:
                    running = False

        screen.fill(config.LIGTH_BLUE)

        all_sprites.draw(screen)
        Text.draw(screen, "Pontuação: " + str(score),
                  config.FONT_SIZE, score_pos_x, score_pos_y, config.WHITE)
        Text.draw(screen, "Vida: " + str(player.health), config.FONT_SIZE,
                  score_pos_x, score_pos_y + config.FONT_SIZE + 5, config.WHITE)

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
