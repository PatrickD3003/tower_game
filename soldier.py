import pygame
import os
WIDTH, HEIGHT = 1200, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# sementara pake ini dulu
tower_width = 100
tower_height = 200
dx = 0
dy = 0

class Soldier(pygame.sprite.Sprite):
    width, height = 40, 40

    def __init__(self, soldier_rotate):
        super().__init__()
        self.width, self.height = 40, 40
        self.rotate = soldier_rotate
        self.image_soldier_import = pygame.image.load(os.path.join("characters", "ogre_sprite.png"))
        self.image_soldier = pygame.transform.scale(self.image_soldier_import, (self.width, self.height))
        self.rect = self.image_soldier.get_rect()
        self.rect.y = HEIGHT - self.height
        self.alive = True
        if self.rotate == True:  # kalo misalkan kubu sebelah kanan
            self.image_soldier = pygame.transform.flip(self.image_soldier, True, False)
            self.rect.x = WIDTH - 20 - tower_width - self.width
        else:
            self.rect.x = 20 + tower_width
 
    def summon_soldier(self):
        WINDOW.blit(self.image_soldier, (self.rect.x, self.rect.y))

    
    def move_soldier(self):
        if self.rotate == True:
            dx, dy = -5, 0
        else:
            dx, dy = 5, 0
        self.rect.move_ip(dx, dy)
    
    def stop_soldier(self):
        dx = 0
        dy = 0
        self.rect.move_ip(dx, dy)


    def collide(self, enemy_group, enemy_barrack):
        self.enemy_group = enemy_group
        self.enemy_barrack = enemy_barrack

        if self.enemy_barrack != []:
            if pygame.sprite.spritecollideany(self, enemy_barrack):
                self.alive = False
            else:
                self.alive = True
        else:
            return True
        






        

    
    

