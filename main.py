import pygame
import sys

from data.scripts.tile import tiles_group, tile_images, Tile
from data.scripts.mechanism import Mechanism
from data.scripts.item import Item


if True: # __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_rect()[:2]
    clock = pygame.time.Clock()

    t = Tile('furnace_t1', 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        tiles_group.draw(screen)
        if clock.tick(1000) == 1:
            t.mecha.is_on = True
            t.update(clock.tick())

        pygame.display.flip()
