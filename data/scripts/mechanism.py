from data.scripts.item import Item, ItemStack


crafts_of_mechas = {
    'furnace_t1': {'iron_plate', 'copper_wire'}
}


crafting_recipes = {
    'iron_plate': Item('iron_plate').get_crafting_recipe(),
    'copper_wire': Item('copper_wire').get_crafting_recipe(),
}


class Mechanism:
    def __init__(self, mecha_type):
        self.crafts = crafts_of_mechas[mecha_type]
        self.is_on = False
        self.ingredient_slot = None
        self.fuel_slot = None
        self.done_slot = None
        self.time_left = 0

    def update(self, time_step):
        if self.is_on:
            self.time_left -= time_step
            if self.time_left <= 0:
                pass  # TODO Finish crafting
        if self.ingredient_slot is None or\
            self.fuel_slot is None:
            return
        for craft in self.crafts:
            craft = crafting_recipes[craft]
            if self.tile.tile_type in craft['where'] and\
                self.ingredient_slot.get_amount() >= craft['ingredients'][0] and\
                self.fuel_slot.get_amount() >= craft['fuel'][0]:
                    pass  # TODO craft
