import pygame
class Soldier:
    soldiers = []
    def __init__(self, soldier_width, soldier_height, soldier_x, soldier_y, soldier_velocity, attack_damage, soldier_health):
        self.width = soldier_width
        self.height = soldier_height
        self.x = soldier_x
        self.y = soldier_y
        self.velocity = soldier_velocity
        self.attack = attack_damage
        self.health = soldier_health
        self.create_soldier = pygame.Rect(self.x, self.y, self.width, self.height)

    def summon_soldier(self):
        

    
    


