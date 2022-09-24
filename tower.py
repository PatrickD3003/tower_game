import pygame
class Tower:
    WIDTH, HEIGHT = 900, 500
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    def __init__(self, tower_width, tower_height, tower_location_x, tower_location_y, tower_color):
        self.width = tower_width
        self.height = tower_height
        self.x = tower_location_x
        self.y = tower_location_y
        self.color = tower_color
        self.create_tower = pygame.Rect(self.x, self.y, self.width, self.height)

    
    def draw_tower(self):
        return pygame.draw.rect(self.WINDOW, self.color, self.create_tower)

        


