import pygame
from soldier import *
import math

pygame.init()

mob1 = pygame.sprite.Group()
mob2 = pygame.sprite.Group()

width, height = 1200, 600
fps = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tower Game")

# basic colors rgb black white
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def set_background(texture):
    ground_height = 100
    ground_length = width * 2
    img = pygame.image.load(texture)
    img = pygame.transform.scale(img, (width, height))
    return img


background = set_background("textures/purple_sky.jpg")

scroll = 0
tiles = math.ceil(width / background.get_width()) + 1

"""
def update_ground(scroll):
    x, y = pygame.display.get_surface().get_size()
    pygame.display.get_surface().fill(WHITE)

    i = 0
    while i < tiles:
        screen.blit(background, (background.get_width() * i + scroll, y - 100))
        i += 1
    scroll -= 6

    if abs(scroll) > background.get_width():
        scroll = 0

    pygame.display.update()
"""

def main():
    running = True
    clock = pygame.time.Clock()
    spawn = False
    team1 = []
    team2 = []
    attacking = []

    #update_ground(scroll)

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # summon left side soldier
                    spawn = True
                    first = Soldier("1", "ogre")
                    team1.append(first)
                    mob1.add(first)
                if event.key == pygame.K_2:  # summon left side soldier
                    spawn = True
                    second = Soldier("2", "ogre")
                    team2.append(second)
                    mob2.add(second)

        screen.blit(background, (0, 0))

        if team1 != []:
            for mob in team1:
                mob.move(True)
                if pygame.sprite.spritecollideany(mob, mob2):
                    mob.move(False)
                    transfer = team1.pop(team1.index(mob))
                    attacking.append(transfer)
                    continue

        if team2 != []:
            for mob in team2:
                mob.move(True)
                if pygame.sprite.spritecollideany(mob, mob1):
                    mob.move(False)
                    transfer = team2.pop(team2.index(mob))
                    attacking.append(transfer)
                    continue

        if attacking != []:
            for mob in attacking:
                if mob.team == 1:
                    if pygame.sprite.spritecollideany(mob, mob2):
                        mob.move(False)
                        mob.attack()
                else:
                    if pygame.sprite.spritecollideany(mob, mob1):
                        mob.move(False)
                        mob.attack()


        pygame.display.flip()


if __name__ == '__main__':
    main()
