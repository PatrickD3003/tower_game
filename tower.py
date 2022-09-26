import pygame
import os
class Tower:
    WIDTH, HEIGHT = 1200, 500
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    def __init__(self, tower_rotate):
        self.width, self.height = 200, 200 
        self.tower_image_import = pygame.image.load(os.path.join("buildings", "castle.png"))
        self.tower_image = pygame.transform.scale(self.tower_image_import, (self.width, self.height))
        self.y_pos = self.HEIGHT - self.tower_image.get_height()
        

        if tower_rotate == True:  # if tower di kanan
            self.x_pos = self.WIDTH - self.tower_image.get_width() - 20
        else:
            self.x_pos = 20
    
    def draw_tower(self):
        self.WINDOW.blit(self.tower_image, (self.x_pos, self.y_pos))
        


