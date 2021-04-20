import pygame
import json

from random import randint
from data.scripts.tile import Tile, tile_side, ores_group
from math import sqrt


with open('data/config.json') as config_file:
    config = json.load(config_file)
config = config['world_gen']


radius_world = 0
world_stone_map = []


def dist_from_center(x, y):
    x += tile_side // 2
    y += tile_side // 2
    return sqrt((x - radius_world * tile_side) ** 2 + (y - radius_world * tile_side) ** 2)


box_to_check = pygame.sprite.Sprite()
def generate_ore(mn, mx, n, ore):
    for _ in range(n):
        x = randint(0, radius_world * 2 - 1)
        y = randint(0, radius_world * 2 - 1)
        while True:
            dist = dist_from_center(x * tile_side, y * tile_side)
            box_to_check.rect = pygame.rect.Rect(x * tile_side + tile_side // 2,
                                                 y * tile_side + tile_side // 2, 1, 1)
            if mn * tile_side <= dist <= mx * tile_side and\
                    not pygame.sprite.spritecollideany(box_to_check, ores_group):
                Tile(ore, x * tile_side, y * tile_side)
                break
            x = randint(0, radius_world * 2 - 1)
            y = randint(0, radius_world * 2 - 1)


def generate_terrain():
    global radius_world, world_stone_map
    radius_world = config['t0_width'] + config['t1_width'] + \
                   config['t2_width'] + config['t3_width']
    world_stone_map = [[0] * (radius_world * 2) for _ in range(radius_world * 2)]
    mul_t0_width = config['t0_width'] * tile_side
    mul_t1_width = (config['t0_width'] + config['t1_width']) * tile_side
    mul_t2_width = (config['t0_width'] + config['t1_width'] +
                    config['t2_width']) * tile_side
    mul_t3_width = radius_world * tile_side
    for i in range(radius_world * 2):
        for j in range(radius_world * 2):
            dist = dist_from_center(i * tile_side, j * tile_side)
            if dist <= mul_t0_width:
                world_stone_map[i][j] = Tile('stone_t1_floor', i * tile_side, j * tile_side)
            elif dist <= mul_t1_width:
                world_stone_map[i][j] = Tile('stone_t1', i * tile_side, j * tile_side)
            elif dist <= mul_t2_width:
                world_stone_map[i][j] = Tile('stone_t2', i * tile_side, j * tile_side)
            else:
                world_stone_map[i][j] = Tile('stone_t3', i * tile_side, j * tile_side)
    for ore in config['ores']:
        generate_ore(*config['ores'][ore], ore=ore)
    print('Done')
    return radius_world, world_stone_map
