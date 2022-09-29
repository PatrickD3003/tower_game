import pygame
import os
from tower import Tower
from soldier import Soldier

# initialize pygame
pygame.init()

right_exist = False
left_exist = False
# initial setups
WIDTH, HEIGHT = 1200, 500
FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Game")

ROTATE = True  # right team
NO_ROTATE = False  # left team

# basic colors rgb black white
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

velocity = 2

left_tower = Tower(NO_ROTATE)
right_tower = Tower(ROTATE)

left_group = pygame.sprite.Group()
right_group = pygame.sprite.Group()

def draw_window(left_group, right_group): 
    left_tower.draw_tower()
    right_tower.draw_tower()

    for entity in left_group:
        entity.summon_soldier()
    
    for entity in right_group:
        entity.summon_soldier()
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    left_soldiers_barrack = []
    right_soldiers_barrack = []
    flag1 = True
    flag2 = True
    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)
        #pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_1:  # summon left side soldier
                    left_soldier = Soldier(NO_ROTATE)
                    left_soldiers_barrack.append(left_soldier)
                    left_group.add(left_soldier)

                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(ROTATE)
                    right_soldiers_barrack.append(right_soldier)
                    right_group.add(right_soldier)
        
        draw_window(left_soldiers_barrack, right_soldiers_barrack)
        # move(left_soldiers_barrack, right_soldiers_barrack)

        if left_soldiers_barrack != []:
            for entity in left_soldiers_barrack:
                if entity.alive == True:
                    entity.move_soldier()
                elif entity.alive == False:
                    entity.stop_soldier()
                entity.collide(right_group, right_soldiers_barrack)
                continue
        if right_soldiers_barrack != []:
            for entity in right_soldiers_barrack:
                if entity.alive == True:
                    entity.move_soldier()
                elif entity.alive == False:
                    entity.stop_soldier()
                entity.collide(left_group, left_soldiers_barrack)
                continue
    main()

if __name__ == "__main__":
    main()
