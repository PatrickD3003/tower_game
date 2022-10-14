from level import *

pygame.init()


class SoldierMelee(pygame.sprite.Sprite):

    def __init__(self, team, name, hp, dmg, attack_speed, attack_range, cost):
        super(SoldierMelee, self).__init__()
        w, h = pygame.display.get_surface().get_size()
        self.team = team
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.cost = cost

        self.attack_timer_sum = round(self.attack_speed / 11)
        self.attacking = False
        self.attacked_this_turn = True
        self.pattern = 0

        if self.name == "swordsman":
            self.width = w / 16
            self.height = h / 8
            self.img_walk = pygame.transform.scale(pygame.image.load("textures/d1.png"), (self.width, self.height))
            self.img_attack = [pygame.transform.scale(pygame.image.load("textures/a1.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a2.png"), (self.width, self.height)),
                                pygame.transform.scale(pygame.image.load("textures/a3.png"), (self.width, self.height)),]
            self.image = self.img_walk
            self.attack_animations_count = len(self.img_attack)


        self.rect = self.image.get_rect()
        self.rect.y = h - (self.image.get_height() + tile_size)

        if team == "1":
            self.rect.x = (tile_size * 2) - (self.image.get_width() / 2)
            self.rect.update(self.rect.x, self.rect.y, self.rect.x + self.attack_range, self.rect.y)
        elif team == "2":
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x = total_width - (tile_size * 2) - (self.image.get_width() / 2)
            self.rect.update(self.rect.x - self.attack_range, self.rect.y, self.rect.x + self.attack_range, self.rect.y)

    def set_scroll(self, scroll):
        self.scroll = scroll

    def move(self):
        if self.team == "1":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll, self.rect.y))
            self.rect.move_ip(4, 0)
            if self.rect.x > total_width:
                self.hp = 0
                self.kill()

        elif self.team == "2":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + self.scroll, self.rect.y))
            self.rect.move_ip(-4, 0)
            if self.rect.x < - (self.width + self.attack_range):
                self.hp = 0
                self.kill()

    def stop(self):
        if self.team == "1":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll, self.rect.y))
        elif self.team == "2":
            pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + self.scroll, self.rect.y))

    def attack(self):
        self.attack_timer_sum += 1

        if self.attack_timer_sum == self.attack_speed:
            self.pattern = 0
            self.attack_timer_sum = 0
            self.attacking = True

        if self.attacking:
            self.image = self.img_attack[self.pattern]
            self.animation_interval = 0.4 / self.attack_animations_count
            if self.pattern < self.attack_animations_count - 1:
                if self.attack_timer_sum == round(self.attack_speed * self.animation_interval * self.pattern):
                    self.pattern += 1
                if self.attack_timer_sum == round(self.attack_speed * self.animation_interval):
                    self.attacked_this_turn = False

            if self.team == "1":
                pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll, self.rect.y))
            elif self.team == "2":
                self.image = pygame.transform.flip(self.image, True, False)
                pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + self.scroll, self.rect.y))
            if self.attack_timer_sum == self.attack_speed * 0.3:
                self.pattern = 0
                self.attacking = False
                self.image = self.img_walk
                if self.team == "1":
                    pygame.display.get_surface().blit(self.image, (self.rect.x + self.scroll, self.rect.y))
                elif self.team == "2":
                    self.image = pygame.transform.flip(self.image, True, False)
                    pygame.display.get_surface().blit(self.image, (self.rect.x + self.attack_range + self.scroll, self.rect.y))


    def collision_handler(self, group):
        if pygame.sprite.spritecollideany(self, group):
            current_target = pygame.sprite.spritecollideany(self, group)
            if self.team == "1":
                range_calc = current_target.rect.x + current_target.attack_range - self.rect.x - self.width
            else:
                range_calc = self.rect.x - current_target.rect.x + self.attack_range - current_target.width

            if 0 < self.attack_range + self.width <= abs(range_calc):
                self.move()
            else:
                self.stop()
                self.attack()
                if self.attacked_this_turn is False:
                    self.attacked_this_turn = True
                    current_target.hp -= self.dmg
                    if current_target.hp <= 0:
                        current_target.kill()

        elif self.hp > 0:
            self.image = self.img_walk
            if self.team == "2":
                self.image = pygame.transform.flip(self.image, True, False)
            self.attacking = False
            self.pattern = 0
            self.attacked_this_turn = True
            self.attack_timer_sum = round(self.attack_speed / 11)
            self.move()
        elif self.hp <= 0:
            self.kill()




