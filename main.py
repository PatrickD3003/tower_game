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

# basic colors rgb black white
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create tower object
# left side tower
L_TOWER_WIDTH = 100
L_TOWER_HEIGHT = 200
L_TOWER_X = 20
L_TOWER_Y = HEIGHT - L_TOWER_HEIGHT
left_tower = Tower(L_TOWER_WIDTH, L_TOWER_HEIGHT, L_TOWER_X, L_TOWER_Y, RED)
# right side tower
R_TOWER_WIDTH = 100
R_TOWER_HEIGHT = 200
R_TOWER_X = WIDTH - R_TOWER_WIDTH - 20
R_TOWER_Y = HEIGHT - R_TOWER_HEIGHT
right_tower = Tower(R_TOWER_WIDTH, R_TOWER_HEIGHT, R_TOWER_X, R_TOWER_Y, RED)

# create soldier object
# left side soldier
L_SOLDIER_WIDTH = 40
L_SOLDIER_HEIGHT = 40
L_SOLDIER_X = 20 + L_TOWER_WIDTH
L_SOLDIER_Y = HEIGHT - L_SOLDIER_HEIGHT
L_SOLDIER_COLOR = GREEN
L_SOLDIER_VELOCITY = 5
L_SOLDIER_ROTATE = False

# right side soldier
R_SOLDIER_WIDTH = 40
R_SOLDIER_HEIGHT = 40
R_SOLDIER_X = WIDTH - 20 - R_TOWER_WIDTH - R_SOLDIER_WIDTH
R_SOLDIER_Y = HEIGHT - R_SOLDIER_HEIGHT
R_SOLDIER_COLOR = BLUE
R_SOLDIER_VELOCITY = -5
R_SOLDIER_ROTATE = True




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
            left_soldier.x += L_SOLDIER_VELOCITY

        for right_soldier in right_soldiers_barrack:
            right_soldier.x += R_SOLDIER_VELOCITY

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
                    left_soldier = Soldier(L_SOLDIER_WIDTH, L_SOLDIER_HEIGHT, L_SOLDIER_X, L_SOLDIER_Y, L_SOLDIER_COLOR, L_SOLDIER_ROTATE)
                    left_soldiers_barrack.append(left_soldier)
                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(R_SOLDIER_WIDTH, R_SOLDIER_HEIGHT, R_SOLDIER_X, R_SOLDIER_Y, R_SOLDIER_COLOR, R_SOLDIER_ROTATE)
                    right_soldiers_barrack.append(right_soldier)

        handle_movement(left_soldiers_barrack, right_soldiers_barrack)
        draw_window(left_soldiers_barrack, right_soldiers_barrack)


    main()

if __name__ == "__main__":
    main()