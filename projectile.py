import pygame

class Projectile(pygame.sprite.Sprite):

    gravity = 5
    def __init__(self, img, width, height, velocity):
        super(Projectile, self).__init__()
        self.x_velocity = velocity
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def summon(self, unit):
        self.unit = unit
        self.team = unit.team
        self.dmg = unit.dmg
        if self.team == "1":
            self.rect.x = self.unit.rect.x + self.unit.image.get_width()
        else:
            self.rect.x = self.unit.rect.x

        self.rect.y = self.unit.rect.y - 10

    def projectile_move(self, distance):
        time_taken = distance / self.x_velocity
        self.y_velocity = 4
        pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        self.rect.move_ip(self.x_velocity, self.y_velocity)
        self.y_velocity -= Projectile.gravity

    def set_scroll(self, scroll):
        self.scroll = scroll

Arrow = Projectile("textures/sprite_textures/Arrow.png", 20, 5, 5)