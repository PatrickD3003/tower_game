import pygame
from level import *

pygame.init()

class Soldier(pygame.sprite.Sprite):

    def __init__(self, team, name, hp, dmg, attack_speed, attack_range):
        super(Soldier, self).__init__()
        w, h = pygame.display.get_surface().get_size()
        self.team = team
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attack_speed = attack_speed
        self.attack_range = attack_range

        self.attack_timer_sum = 20
        self.pattern = 0
        self.attacking = False
        self.attacked_this_turn = True

        if self.name == "swordsman":
            self.width = w / 16
            self.height = h / 8
            self.img_default = pygame.transform.scale(pygame.image.load("textures/d1.png"), (self.width, self.height))
            self.img_attacks = [pygame.transform.scale(pygame.image.load("textures/a1.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a2.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a3.png"), (self.width, self.height)),]
            self.image = self.img_default

        if self.name == "archer":
            self.width = w / 16
            self.height = h / 8
            self.img_default = pygame.transform.scale(pygame.image.load("textures/d1.png"), (self.width, self.height))
            self.img_attacks = [pygame.transform.scale(pygame.image.load("textures/a1.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a2.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a3.png"),
                                                       (self.width, self.height)), ]

            self.image = self.img_default

        self.rect = self.image.get_rect()

        self.rect.y = h - (self.image.get_height() + tile_size)

        if team == "1":
            self.rect.x = (tile_size * 2) - (self.image.get_width() / 2)
            self.rect.update(self.rect.x, self.rect.y, self.rect.x + self.attack_range, self.rect.y)
        elif team == "2":
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x = total_width - (tile_size * 2) - (self.image.get_width() / 2)
            self.rect.update(self.rect.x - self.attack_range, self.rect.y, self.rect.x + self.attack_range, self.rect.y)



    def move(self, scroll):
        if self.team == "1":
            pygame.display.get_surface().blit(self.image, (self.rect.x + scroll, self.rect.y))
            self.rect.move_ip(4, 0)
        elif self.team == "2":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + scroll, self.rect.y))
            self.rect.move_ip(-4, 0)


    def stop(self, scroll):
        if self.team == "1":
            pygame.display.get_surface().blit(self.image, (self.rect.x + scroll, self.rect.y))
        elif self.team == "2":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + scroll, self.rect.y))

    def attack(self, scroll):

        self.attack_timer_sum += 1

        if self.attack_timer_sum == self.attack_speed:
            self.pattern = 0
            self.attack_timer_sum = 0
            self.attacking = True

        if self.attacking:
            self.image = self.img_attacks[self.pattern]
            if self.attack_timer_sum == round(self.attack_speed * 0.1):
                self.pattern += 1
            if self.attack_timer_sum == round(self.attack_speed * 0.2):
                self.attacked_this_turn = False
                self.pattern += 1
            if self.team == "1":
                pygame.display.get_surface().blit(self.image, (self.rect.x + scroll, self.rect.y))
            elif self.team == "2":
                self.image = pygame.transform.flip(self.image, True, False)
                pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + scroll, self.rect.y))
            if self.attack_timer_sum == self.attack_speed * 0.3:
                self.pattern = 0
                self.attacking = False
                self.image = self.img_default
                if self.team == "1":
                    pygame.display.get_surface().blit(self.image, (self.rect.x + scroll, self.rect.y))
                elif self.team == "2":
                    self.image = pygame.transform.flip(self.image, True, False)
                    pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + scroll, self.rect.y))




    def attack_handler_melee(self, group, scroll):

        if pygame.sprite.spritecollideany(self, group):
            current_target = pygame.sprite.spritecollideany(self, group)
            if self.team == "1":
                range_calc = current_target.rect.x + current_target.attack_range - self.rect.x
            else:
                range_calc = self.rect.x - current_target.rect.x + self.attack_range
                print(range_calc)

            if self.attack_range + self.width <= range_calc:
                self.move(scroll)
            else:
                self.stop(scroll)
                self.attack(scroll)
                if self.attacked_this_turn is False:
                    self.attacked_this_turn = True
                    current_target.hp -= self.dmg
                    if current_target.hp <= 0:
                        current_target.kill()

        elif self.hp > 0:
            self.image = self.img_default
            if self.team == "2":
                self.image = pygame.transform.flip(self.image, True, False)
            self.attacking = False
            self.pattern = 0
            self.attacked_this_turn = True
            self.attack_timer_sum = 20
            self.move(scroll)
        elif self.hp <= 0:
            self.kill()




