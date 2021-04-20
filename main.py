import pygame
import sys

from data.scripts.tile import tiles_group, tile_images, Tile, tile_side
from data.scripts.tile import unpassable_tiles_group, ores_group
from data.scripts.tilemap import config, generate_terrain, world_stone_map
from data.scripts.mechanism import Mechanism
from data.scripts.item import Item
from data.scripts.player import Player, player_group


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


if True: # __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    x, y, width, height = screen.get_rect()
    print(width, height)
    clock = pygame.time.Clock()

    radius_world = generate_terrain(config['world_gen'])
    t = Player(radius_world * tile_side,
               radius_world * tile_side,
               (width, height))

    camera = Camera()

    time = 0
    a = 20
    c = 0
    tiles_group.add(t)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                t.new_mouse_pos(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    t.keys['w'] = True
                if event.key == pygame.K_s:
                    t.keys['s'] = True
                if event.key == pygame.K_a:
                    t.keys['a'] = True
                if event.key == pygame.K_d:
                    t.keys['d'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    t.keys['w'] = False
                if event.key == pygame.K_s:
                    t.keys['s'] = False
                if event.key == pygame.K_a:
                    t.keys['a'] = False
                if event.key == pygame.K_d:
                    t.keys['d'] = False

        screen.fill((0, 0, 0))

        time += clock.tick()
        if time >= a * c:
            c += 1
            t.update()

        camera.update(t)
        for sprite in tiles_group:
            camera.apply(sprite)

        tiles_group.draw(screen)

        player_group.draw(screen)

        pygame.display.flip()
