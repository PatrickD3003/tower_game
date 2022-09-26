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


def draw_window(left_soldiers_barrack, right_soldiers_barrack): 
    left_tower.draw_tower()
    right_tower.draw_tower()

    for left_soldier in left_soldiers_barrack:
        left_soldier.summon_soldier()
    
    for right_soldier in right_soldiers_barrack:
        right_soldier.summon_soldier()
    pygame.display.update()


def handle_movement(left_soldiers_barrack, right_soldiers_barrack, left_hitbox, right_hitbox):
    
    for left_soldier in left_soldiers_barrack:
        left_soldier.x += velocity
        if right_soldiers_barrack != []:
            left_rect = left_soldier.create_hitbox()
            if right_hitbox.colliderect(left_rect):  # kalo collide dua rectangle
                print("left collide with right")
                left_soldiers_barrack.remove(left_soldier)
            else:
                print("no collision")

    
    for right_soldier in right_soldiers_barrack:
        right_soldier.x -= velocity   
        if left_soldiers_barrack != []:
            right_rect = right_soldier.create_hitbox()
            if left_hitbox.colliderect(right_rect):
                print("right collide with left")
                right_soldiers_barrack.remove(right_soldier)
                

            else:
                print("no collision")
                   

def main():
    run = True
    clock = pygame.time.Clock()
    left_soldiers_barrack = []
    right_soldiers_barrack = []

    tower_width, tower_height = 100, 200
    
    soldier_width, soldier_height = 40, 40
    soldier_y = HEIGHT - soldier_height
    left_soldier_x = 20 + tower_width
    right_soldier_x = WIDTH - 20 - tower_width - soldier_width
    
    left_hitbox = pygame.Rect(left_soldier_x, soldier_y, soldier_width, soldier_height)
    right_hitbox = pygame.Rect(right_soldier_x, soldier_y, soldier_width, soldier_height)
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
                    left_soldier = Soldier(left_hitbox.x, left_hitbox.y, soldier_width, soldier_height, NO_ROTATE)
                    left_soldiers_barrack.append(left_soldier)
                    

                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(right_hitbox.x, right_hitbox.y, soldier_width, soldier_height, ROTATE)
                    right_soldiers_barrack.append(right_soldier)

        handle_movement(left_soldiers_barrack, right_soldiers_barrack, left_hitbox, right_hitbox)
        draw_window(left_soldiers_barrack, right_soldiers_barrack)
        


    main()

if __name__ == "__main__":
    main()
