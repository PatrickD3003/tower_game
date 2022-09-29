from level import *
from math import ceil
import pygame

class Screen():

    def __init__(self, name, x, y):
        self.name = name
        self.width = x
        self.height = y
        self.used = False
        self.bg_exist = False
        self.scroll = 0
        self.scrolling_screen = False

    def use_screen(self):
        pygame.display.set_caption(self.name)
        self.used = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def end_screen(self):
        self.used = False

    def set_background(self, texture):
        self.bg_image = pygame.image.load(texture)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.width, self.height))
        self.tiles = ceil(self.width / self.bg_image.get_width()) + 1
        self.bg_exist = True

    def set_scroll(self, level):
        self.scrolling_screen = True
        for i in range(-5, self.tiles):
            self.screen.blit(self.bg_image, (i * self.width + self.scroll, 0))

        mx, my = pygame.mouse.get_pos()

        if 1 < mx <= self.width * 0.1: #left
            if self.scroll <= -2:
                self.scroll += 4
                level.world_shift = 4
            else:
                level.world_shift = 0
        elif self.width - 1 > mx >= self.width * 0.9: #right
            if self.scroll >= -720:
                self.scroll -= 4
                level.world_shift = -4
            else:
                level.world_shift = 0
        else:
            level.world_shift = 0

        return self.scroll

    def update_screen(self):
        if self.used == True and self.scrolling_screen is False:
            if self.bg_exist:
                self.screen.blit(self.bg_image, (0, 0))
            else:
                self.screen.fill((0, 0, 0))

