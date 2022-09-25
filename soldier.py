import pygame
import os
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
class Soldier:
    def __init__(self, soldier_width, soldier_height, soldier_x, soldier_y, soldier_color, soldier_rotate):
        self.width = soldier_width
        self.height = soldier_height
        self.x = soldier_x
        self.y = soldier_y
        self.color = soldier_color
        self.rotate = soldier_rotate
        self.create_soldier = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image_soldier_import = pygame.image.load(os.path.join("characters", "ogre_sprite.png"))
        if self.rotate == True:
            self.image_soldier = pygame.transform.flip(pygame.transform.scale(self.image_soldier_import, (self.width, self.height)), True, False)
        else:
            self.image_soldier = pygame.transform.scale(self.image_soldier_import, (self.width, self.height))
        
    def summon_soldier(self):
        WINDOW.blit(self.image_soldier, (self.x, self.y))

    def soldier_move(self, soldier_velocity):
        self.velocity = soldier_velocity
        self.create_soldier.x += self.velocity

        

    
    


