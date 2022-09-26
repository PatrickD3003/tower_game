import pygame
import os
from tower import Tower
from soldier import Soldier

# initialize pygame
pygame.init()

# initial setups
WIDTH, HEIGHT = 900, 500
FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Game")
ROTATE = True
NO_ROTATE = False
# basic colors rgb black white
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

left_tower = Tower(NO_ROTATE)
# right side tower
right_tower = Tower(ROTATE)


def draw_window(left_soldiers_barrack, right_soldiers_barrack): 
    left_tower.draw_tower()
    right_tower.draw_tower()

    for left_soldier in left_soldiers_barrack:
        left_soldier.summon_soldier()
    
    for right_soldier in right_soldiers_barrack:
        right_soldier.summon_soldier()
    pygame.display.update()


def handle_movement(left_soldiers_barrack, right_soldiers_barrack):
        for left_soldier in left_soldiers_barrack:
            left_soldier.soldier_move()

        for right_soldier in right_soldiers_barrack:
            right_soldier.soldier_move()

def main():
    run = True
    clock = pygame.time.Clock()
    left_soldiers_barrack = []
    right_soldiers_barrack = []
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
                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(ROTATE)
                    right_soldiers_barrack.append(right_soldier)

        handle_movement(left_soldiers_barrack, right_soldiers_barrack)
        draw_window(left_soldiers_barrack, right_soldiers_barrack)


    main()

if __name__ == "__main__":
    main()