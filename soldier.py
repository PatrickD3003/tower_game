import pygame
import os

# sementara pake ini dulu
tower_width = 100
tower_height = 200

class Soldier(pygame.sprite.Sprite):
    
    def __init__(self, soldier_rotate, window):
        super().__init__()
        # input variable
        self.window = window
        self.rotate = soldier_rotate
        self.width, self.height = 40, 40    
        # flags
        self.alive = True
        self.collide = False
        # object creation
        self.image_soldier_import = pygame.image.load(os.path.join("characters", "ogre_sprite.png"))
        self.image_soldier = pygame.transform.scale(self.image_soldier_import, (self.width, self.height))
        self.rect = self.image_soldier.get_rect()

        self.rect.y = self.window.get_height() - self.height
        if self.rotate == True:  # kalo misalkan kubu sebelah kanan
            self.image_soldier = pygame.transform.flip(self.image_soldier, True, False)
            self.rect.x = self.window.get_width() - 20 - tower_width - self.width
        else:
            self.rect.x = 20 + tower_width
 
    def summon_soldier(self):
        self.window.blit(self.image_soldier, (self.rect.x, self.rect.y))

    def move_soldier(self):
        dx, dy = 5, 0
        if self.rotate == True:
            dx *= -1
        else:
            dx *= 1
        self.rect.move_ip(dx, dy)
    
    def stop_soldier(self):
        dx = 0
        dy = 0
        self.rect.move_ip(dx, dy)

    def collision_detector(self, enemy_group):
        self.enemy_group = enemy_group
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.collide = True
        else:
            self.collide = False


        






        

    
    
