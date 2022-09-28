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
        WINDOW.blit(entity.image_soldier, (entity.rect.x, entity.rect.y))
    
    for entity in right_group:
        WINDOW.blit(entity.image_soldier, (entity.rect.x, entity.rect.y))
    pygame.display.update()


def move(left, right):
    for entity in left:
        entity.soldier_move(True)
    
    for entity in right:
        entity.soldier_move(True)

def collide(left_group, right_group, left_barrack, right_barrack):
    if left_barrack != []:
        for entity in right_barrack:
            if pygame.sprite.spritecollideany(entity, left_group):
                print("COLLIDE")
            else:
                pass
    if right_barrack != []:
        for entity in left_barrack:
            if pygame.sprite.spritecollideany(entity, right_group):
                print("COLLIDE THIS SIDE ALSO")
            else:
                pass



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
                    left_group.add(left_soldier)

                    

                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(ROTATE)
                    right_soldiers_barrack.append(right_soldier)
                    right_group.add(right_soldier)

        

        move(left_soldiers_barrack, right_soldiers_barrack)
        draw_window(left_group, right_group)
        
        if left_soldiers_barrack != []:
            left_soldier.collide(right_group, right_soldiers_barrack)
            continue
        if right_soldiers_barrack != []:
            right_soldier.collide(left_group, left_soldiers_barrack)
            continue

        


    main()

if __name__ == "__main__":
    main()
