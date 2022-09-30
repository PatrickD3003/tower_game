import pygame

class HealthBar:
    def __init__(self, entity):
        self.entity_hp = entity.hp
        if entity.team == "1":
            self.x_pos = entity.rect.x
        else:
            self.x_pos = entity.rect.x + entity.width

        self.y_pos = entity.rect.y - 30
        self.bar_multiplier = entity.width / entity.hp

    def set_scroll(self, scroll):
        self.scroll = scroll

    def update_bar(self):
        self.width = self.bar_multiplier * self.entity_hp
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll, self.rect.y))

