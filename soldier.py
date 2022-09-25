import pygame

pygame.init()

class Soldier:

    def __init__(self, img, team, name):
        w, h = pygame.display.get_surface().get_size()
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.team = team
        self.name = name
        self.y = h - self.img.get_height()
        if team == "1":
            self.x = 100 - (self.img.get_width() / 2)
        elif team == "2":
            self.img = pygame.transform.flip(self.img, True, False)
            self.x = w - 100 - (self.img.get_width() / 2)

    def move(self):
        if self.team == "1":
            self.x += 2
        elif self.team == "2":
            self.x -= 2
        return self.x, self.y

