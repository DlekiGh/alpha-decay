import pygame

from data.scripts.utilities import load_image
from data.scripts.tile import unpassable_tiles_group
from math import atan2, degrees


player_group = pygame.sprite.Group()
player_speed = 10
diagonal_speed = player_speed / (2 ** 0.5)

class Player(pygame.sprite.Sprite):
    image_main = load_image('player.png')
    image_arm = load_image('player arm.png')

    def __init__(self, x, y, screeenRes):
        super().__init__(player_group)
        self.image = Player.image_main.copy()
        self.width, self.height = screeenRes
        self.rect = pygame.rect.Rect(x, y, 128, 128)
        self.keys = {'w': False, 'a': False, 's': False, 'd': False}
        self.mouse_pos = (0, 0)

    def new_mouse_pos(self, pos):
        self.mouse_pos = pos

    def get_delta_pos(self):
        w, a, s, d = self.keys['w'], self.keys['a'], self.keys['s'], self.keys['d']
        delta_y, delta_x = 0, 0
        if w and s:
            a = False
            w = False
        if a and d:
            a = False
            d = False
        if w:
            delta_y -= player_speed
        if a:
            delta_x -= player_speed
        if s:
            delta_y += player_speed
        if d:
            delta_x += player_speed
        if w and a:
            delta_y, delta_x = -diagonal_speed, -diagonal_speed
        if w and d:
            delta_y, delta_x = -diagonal_speed, diagonal_speed
        if a and s:
            delta_y, delta_x = diagonal_speed, -diagonal_speed
        if s and d:
            delta_y, delta_x = diagonal_speed, diagonal_speed
        return delta_x, delta_y

    def update_pos(self):
        old_pos = (self.rect.x, self.rect.y)
        delta_x, delta_y = self.get_delta_pos()
        self.rect = self.rect.move(delta_x, 0)
        if pygame.sprite.spritecollideany(self, unpassable_tiles_group):
            self.rect.x, self.rect.y = old_pos
        old_pos = (self.rect.x, self.rect.y)
        self.rect = self.rect.move(0, delta_y)
        if pygame.sprite.spritecollideany(self, unpassable_tiles_group):
            self.rect.x, self.rect.y = old_pos

    def update(self):
        self.update_pos()
        x, y = self.mouse_pos
        x -= self.width // 2
        y -= self.height // 2
        at = degrees(atan2(x, y))
        transformed = pygame.transform.rotate(Player.image_main.copy(), at)
        rect = transformed.get_rect()
        self.image.fill((40, 40, 40))
        self.image.set_colorkey((40, 40, 40))
        self.image.blit(transformed,
                        (0, 0),
                        ((rect.width - 126) / 2,
                         (rect.height - 132) / 2,
                         134, 134))
