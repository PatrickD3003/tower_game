import pygame

class Projectile(pygame.sprite.Sprite):

    gravity = 5
    def __init__(self, img, width, height, velocity):
        super(Projectile, self).__init__()
        self.xv = velocity[0]
        self.yv = velocity[1]
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image

    def summon(self, unit):
        self.unit = unit
        self.team = unit.team
        self.dmg = unit.dmg
        if self.team == "1":
            self.rect.x = self.unit.rect.x + self.unit.rect.get_width()
        else:
            self.rect.x = self.unit.rect.x

        self.rect.y = self.unit.rect.y - 10

    def move(self, x=0, y=0):

