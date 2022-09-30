import pygame

class PointBar:
    def __init__(self, team):
        w, h = pygame.display.get_surface().get_size()
        self.team = team
        self.current_points = 0
        self.game_points = 0  # 1 game point is 100 points
        self.bar_multiplier = 0.5

        if self.team == "1":
            self.x_pos = w / 20
        else:
            self.x_pos = w - w / 20

        self.y_pos = h / 10

    def add_points(self):
        if self.current_points == 100:
            self.current_points -= 100
            self.game_points += 1

        self.current_points += 1
        self.width = (self.bar_multiplier * self.current_points) + (self.bar_multiplier * self.game_points * 100)
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        team2_displacement = (self.bar_multiplier * self.current_points) + (self.bar_multiplier * self.game_points * 100)
        if self.team == "1":
            pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        else:
            pygame.display.get_surface().blit(self.image, (self.rect.x - team2_displacement, self.rect.y))

