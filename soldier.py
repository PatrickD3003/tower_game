import pygame
import os
WIDTH, HEIGHT = 1200, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# sementara pake ini dulu
tower_width = 100
tower_height = 200
class Soldier:
    width, height = 40, 40
    def __init__(self, soldier_x, soldier_y, soldier_width, soldier_height, soldier_rotate):
        self.width, self.height = soldier_width, soldier_height
        self.x, self.y = soldier_x, soldier_y 
        self.rotate = soldier_rotate
        self.image_soldier_import = pygame.image.load(os.path.join("characters", "ogre_sprite.png"))
        self.image_soldier = pygame.transform.scale(self.image_soldier_import, (self.width, self.height))

        if self.rotate == True:  # kalo misalkan kubu sebelah kanan
            self.image_soldier = pygame.transform.flip(self.image_soldier, True, False)

            
    def summon_soldier(self):
        WINDOW.blit(self.image_soldier, (self.x, self.y))

    def soldier_move(self):
        self.velocity = 2
        if self.rotate == True:
            self.velocity *= -1
        else:
            self.velocity *= 1
        self.hitbox.x += self.velocity

    def create_hitbox(self):
        pygame.Rect(self.x, self.y, self.width, self.height)



        

    
    


