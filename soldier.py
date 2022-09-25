import pygame
class Soldier:
    WIDTH, HEIGHT = 900, 500
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    def __init__(self, soldier_width, soldier_height, soldier_x, soldier_y, soldier_color):
        self.width = soldier_width
        self.height = soldier_height
        self.x = soldier_x
        self.y = soldier_y
        self.color = soldier_color
        self.create_soldier = pygame.Rect(self.x, self.y, self.width, self.height)
    
        
    def summon_soldier(self):
        pygame.draw.rect(self.WINDOW, self.color, self.create_soldier)

    def soldier_move(self, soldier_velocity):
        self.velocity = soldier_velocity
        self.create_soldier.x += self.velocity

        

    
    


