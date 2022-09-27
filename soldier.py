import pygame

pygame.init()

class Soldier(pygame.sprite.Sprite):

    def __init__(self, team, name):
        super(Soldier, self).__init__()
        w, h = pygame.display.get_surface().get_size()
        self.team = team
        self.name = name
        self.attack_timer_sum = 0
        self.animation_timer_sum = 0
        self.attacking = False

        if self.name == "ogre":
            self.width = w / 16
            self.height = h / 8
            self.img_default = pygame.transform.scale(pygame.image.load("textures/d1.png"), (self.width, self.height))
            self.img_attacks = [pygame.transform.scale(pygame.image.load("textures/a1.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a2.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a3.png"), (self.width, self.height)),]
            self.img = self.img_default
            self.attack_speed = 120
            self.hp = 100
            self.dmg = 25

        self.rect = self.img.get_rect()

        self.rect.y = h - (self.img.get_height() + 80)
        if team == "1":
            self.rect.x = 100 - (self.img.get_width() / 2)
        elif team == "2":
            self.img = pygame.transform.flip(self.img, True, False)
            self.rect.x = w - 100 - (self.img.get_width() / 2)

    def move(self, go):
        if go:
            if self.team == "1":
                pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))
                self.rect.move_ip(4, 0)
            elif self.team == "2":
                pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))
                self.rect.move_ip(-4, 0)
        else:
            if self.team == "1":
                pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))
            elif self.team == "2":
                pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))



    def attack(self):

        self.attack_timer = pygame.time.Clock()
        self.attack_timer_sum += 1
        print(self.attack_timer_sum)

        if self.attack_timer_sum == self.attack_speed:
            self.pattern = 0
            self.attack_timer_sum = 0
            self.attacking = True

        if self.attacking:
            self.img = self.img_attacks[self.pattern]
            if self.attack_timer_sum == round(self.attack_speed * 0.1):
                self.pattern += 1
            if self.attack_timer_sum == round(self.attack_speed * 0.2):
                self.pattern += 1
            if self.team == "1":
                pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))
            elif self.team == "2":
                self.img = pygame.transform.flip(self.img, True, False)
                pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))
            if self.attack_timer_sum == self.attack_speed * 0.3:
                self.pattern = 0
                self.attacking = False
                self.img = self.img_default
                if self.team == "1":
                    pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))
                elif self.team == "2":
                    self.img = pygame.transform.flip(self.img, True, False)
                    pygame.display.get_surface().blit(self.img, (self.rect.x, self.rect.y))



