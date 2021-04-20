import pygame
from data.scripts.utilities import load_image
from data.scripts.mechanism import Mechanism


tile_side = 128
tiles_group = pygame.sprite.Group()
unpassable_tiles_group = pygame.sprite.Group()
mechanism_group = pygame.sprite.Group()
ores_group = pygame.sprite.Group()

player_image = load_image('player.png')

tile_meta_types = {
    'stones': {'stone_t1', 'stone_t2', 'stone_t3'},
    'mechanisms': {'furnace_t1', 'furnace_t2', 'furnace_t3',
                   'researcher_t1', 'researcher_t3', 'reactor'},
    'ores': {'osmium_ore', 'uranium_ore', 'coal_ore', 'copper_ore', 'iron_ore'},
    'floors': {'stone_t1_floor', 'stone_t2_floor', 'stone_t3_floor'}
}

unpassable_meta_types = {'mechanisms', 'stones'}

tile_images = {
    'stone_t1': load_image('stone_T1.png'),
    'stone_t2': load_image('stone_T2.png'),
    'stone_t3': load_image('stone_T3.png'),
    'stone_t1_floor': load_image('stone_T1_floor.png'),
    'stone_t2_floor': load_image('stone_T2_floor.png'),
    'stone_t3_floor': load_image('stone_T3_floor.png'),
    'stone_unbreakable': load_image('stone_unbreakable.png'),
    'furnace_off_t1': load_image('furnace_off_T1.png'),
    'furnace_off_t2': load_image('furnace_off_T2.png'),
    'furnace_off_t3': load_image('furnace_off_T3.png'),
    'furnace_on_t1': load_image('furnace_on_T1.png'),
    'furnace_on_t2': load_image('furnace_on_T2.png'),
    'furnace_on_t3': load_image('furnace_on_T3.png'),
    'mecha_case_t1': load_image('mecha_case_T1.png'),
    'mecha_case_t2': load_image('mecha_case_T2.png'),
    'mecha_case_t3': load_image('mecha_case_T3.png'),
    'research_off_t1': load_image('research_off_T1.png'),
    'research_off_t3': load_image('research_off_T3.png'),
    'research_on_t1': load_image('research_on_T1.png'),
    'research_on_t3': load_image('research_on_T3.png'),
    'nuclear_reactor_off': load_image('nuclear_reactor_off.png'),
    'nuclear_reactor_on': load_image('nuclear_reactor_on.png'),
    'coal_ore': load_image('coal_ore.png'),
    'copper_ore': load_image('copper ore.png'),
    'iron_ore': load_image('iron ore.png'),
    'uranium_ore': load_image('uranium ore.png'),
    'osmium_ore': load_image('osmium ore.png'),
    'err': load_image('404.png')
}


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, x, y, w=tile_side, h=tile_side):
        super().__init__(tiles_group)

        self.tile_type = tile_type

        self.tile_meta_type = 'else'
        self.init_meta_type()

        if self.tile_meta_type == 'mechanisms':
            self.mecha = Mechanism(tile_type)
            self.image = tile_images[tile_type.replace('_', '_off_')]
            mechanism_group.add(self)
        elif self.tile_meta_type == 'ores':
            self.image = tile_images[tile_type]
            ores_group.add(self)
            pass  # TODO make ores work
        elif self.tile_meta_type == 'stones':
            self.image = tile_images[tile_type]
            pass  # TODO make stones work
        elif self.tile_meta_type == 'floors':
            self.image = tile_images[tile_type]
            pass  # TODO make floors work
        else:
            self.image = tile_images['err']

        self.rect = pygame.rect.Rect(x, y, tile_side, tile_side)

    def init_meta_type(self):
        for tile_meta_type in tile_meta_types:
            if self.tile_type in tile_meta_types[tile_meta_type]:
                self.tile_meta_type = tile_meta_type
                if tile_meta_type in unpassable_meta_types:
                    unpassable_tiles_group.add(self)
                break

    def update(self, time):
        pass # TODO think abt this shit
