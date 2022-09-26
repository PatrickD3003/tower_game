import pygame
import os
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# sementara pake ini dulu
tower_width = 100
tower_height = 200
class Soldier:
    width, height = 40, 40
    def __init__(self, soldier_rotate):
        self.width, self.height = 40, 40
        self.rotate = soldier_rotate
        self.image_soldier_import = pygame.image.load(os.path.join("characters", "ogre_sprite.png"))
        self.image_soldier = pygame.transform.scale(self.image_soldier_import, (self.width, self.height))
        self.y_pos = HEIGHT - self.image_soldier.get_height()
        
        if self.rotate == True:  # kalo misalkan kubu sebelah kanan
            self.x_pos = WIDTH - 20 - tower_width - self.width
            self.image_soldier = pygame.transform.flip(self.image_soldier, True, False)
        else:
            self.x_pos = 20 + tower_width  # kalo misalkan kubu sebelah kiri
            
    def summon_soldier(self):
        WINDOW.blit(self.image_soldier, (self.x_pos, self.y_pos))

    def soldier_move(self):
        if self.rotate == True:
            self.velocity = -5
        else:
            self.velocity = 5

        self.x_pos += self.velocity

        

    
    


