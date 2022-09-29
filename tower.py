import pygame
import os
class Tower(pygame.sprite.Sprite):

    def __init__(self, tower_rotate, window):
        super().__init__()
        self.window = window
        self.width, self.height = 200, 200 
        self.tower_image_import = pygame.image.load(os.path.join("buildings", "castle.png"))
        self.tower_image = pygame.transform.scale(self.tower_image_import, (self.width, self.height))
        self.rect = self.tower_image.get_rect()
        self.rect.y = self.window.get_height() - self.tower_image.get_height()
        if tower_rotate == True:  # if tower di kanan
            self.rect.x = self.window.get_width() - self.tower_image.get_width() - 20
        elif tower_rotate == False:
            self.rect.x = 20
        
    
    def draw_tower(self):
        self.window.blit(self.tower_image, (self.rect.x, self.rect.y))
