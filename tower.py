import pygame
import os
from level import  *


class Tower(pygame.sprite.Sprite):

    def __init__(self, team):
        super(Tower, self).__init__()
        WIDTH, HEIGHT = pygame.display.get_surface().get_size()
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.team = team
        self.width, self.height = WIDTH / 6, HEIGHT / 3
        self.tower_image_import = pygame.image.load(os.path.join("textures", "castle.png"))
        self.image = pygame.transform.scale(self.tower_image_import, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.hp = 400

        self.rect.y = HEIGHT - (self.image.get_height() + tile_size)
        if team == "1":
            self.attack_range = 0
            self.rect.x = round(tile_size * 1.7) - (self.image.get_width() / 2)
        elif team == "2":
            self.attack_range = 0
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x = total_width - round(tile_size * 1.7) - (self.image.get_width() / 2)

    def draw_tower(self, scroll):
        if self.hp > 0:
            pygame.display.get_surface().blit(self.image, (self.rect.x + scroll, self.rect.y))

