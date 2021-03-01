import pygame
from data.scripts.utilities import load_image


item_images = {
    'circuit': load_image('circuit.png'),
    'copper': load_image('copper.png'),
    'copper_wire': load_image('copper wire.png'),
    'gears_iron': load_image('gears_iron.png'),
    'gears_osmium': load_image('gears_osmium.png'),
    'gears_steel': load_image('gears_steel.png'),
    'iron': load_image('iron.png'),
    'iron_plate': load_image('iron plate.png'),
    'iron_rod': load_image('iron rod.png'),
    'mecha_case_t1': load_image('mecha_case_T1.png'),
    'mecha_case_t2': load_image('mecha_case_T2.png'),
    'mecha_case_t3': load_image('mecha_case_T3.png'),
    'osmium_plate': load_image('osmium plate.png'),
    'osmium_rod': load_image('osmium rod.png'),
    'steel_plate': load_image('steel plate.png'),
    'steel_rod': load_image('steel rod.png'),
    'stone': load_image('stone.png'),
    'uranium': load_image('uranium.png'),
    'nuclear_fuel_t1': load_image('nuclear_fuel_T1.png'),
    'nuclear_fuel_t2': load_image('nuclear_fuel_T2.png'),
    'nuclear_fuel_t3': load_image('nuclear_fuel_T3.png')
}


recipes = {
    'iron_plate': {'where': {'furnace_t1', 'furnace_t2', 'furnace_t3'},
                   'ingredients': (('iron', 2),),
                   'fuel': (('coal', 2),)},
    'copper_wire': {'where': {'furnace_t1', 'furnace_t2', 'furnace_t3'},
                    'ingredients': (('copper', 2),),
                    'fuel': (('coal', 2),)}
}


items_group = pygame.sprite.Group()


class Item(pygame.sprite.Sprite):
    def __init__(self, item_type):
        super().__init__(items_group)
        self.image = item_images[item_type]
        # self.rect = self.rect.move((-1000, -1000)) TODO whatever the problem i have here
        self.crafting_recipe = recipes[item_type]

    def get_crafting_recipe(self):
        return self.crafting_recipe

class ItemStack(Item):
    def __init__(self, item_type, amount=1):
        super().__init__(item_type)
        self.amount = amount

    def get_amount(self):
        return self.amount
