import pygame
import sys

from data.scripts.gameclass import Game


if True: # __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    x, y, width, height = screen.get_rect()

    clock = pygame.time.Clock()

    game = Game(width, height, screen)
    player = game.player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                player.new_mouse_pos(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.keys['w'] = True
                if event.key == pygame.K_s:
                    player.keys['s'] = True
                if event.key == pygame.K_a:
                    player.keys['a'] = True
                if event.key == pygame.K_d:
                    player.keys['d'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.keys['w'] = False
                if event.key == pygame.K_s:
                    player.keys['s'] = False
                if event.key == pygame.K_a:
                    player.keys['a'] = False
                if event.key == pygame.K_d:
                    player.keys['d'] = False

        screen.fill((0, 0, 0))

        delta_time = clock.tick()
        game.update(delta_time)

        pygame.display.flip()
