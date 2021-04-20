from data.scripts.player import Player, player_group
from data.scripts.utilities import Camera
from data.scripts.tile import tile_side, tiles_group
from data.scripts.tilemap import generate_terrain


class Game:
    def __init__(self, screen_width, screen_height, screen):
        radius_world, self.world_stone_map = generate_terrain()
        self.player = Player(tile_side * radius_world,
                             tile_side * radius_world,
                             (screen_width, screen_height))
        tiles_group.add(self.player)
        self.camera = Camera(screen_width, screen_height)
        self.screen = screen

    def update(self, delta_time):

        self.player.update(delta_time)
        self.camera.update(self.player)

        for sprite in tiles_group:
            self.camera.apply(sprite)

        tiles_group.draw(self.screen)
        player_group.draw(self.screen)
