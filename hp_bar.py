import pygame

class HealthBar:
    def __init__(self, entity):
        self.entity_hp_max = entity.hp
        self.team = entity.team
        if entity.team == "1":
            self.x_pos = entity.rect.x
        else:
            self.x_pos = entity.rect.x + entity.width

        self.y_pos = entity.rect.y - 30
        self.bar_multiplier = entity.width / entity.hp

    def set_scroll(self, scroll):
        self.scroll = scroll

    def update_bar(self, entity):
        self.entity_hp_current = entity.hp
        self.width = self.bar_multiplier * self.entity_hp_current
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        team2_displacement = (self.entity_hp_max - self.entity_hp_current) * self.bar_multiplier
        if self.team == "1":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll, self.rect.y))
        else:
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll - team2_displacement - self.width, self.rect.y))

