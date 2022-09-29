import pygame
from tower import Tower
from soldier import Soldier


def main():
    pygame.init()
    # initial setups
    WIDTH, HEIGHT = 1200, 500
    FPS = 60
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Game")
    ROTATE = True  # right team
    NO_ROTATE = False  # left team

    # basic colors rgb black white
    WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

    run = True
    clock = pygame.time.Clock()

    left_group = pygame.sprite.Group()
    right_group = pygame.sprite.Group()

    left_soldiers_barrack = []
    right_soldiers_barrack = []

    left_tower = Tower(NO_ROTATE, WINDOW)
    right_tower = Tower(ROTATE, WINDOW)

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
                    left_soldier = Soldier(NO_ROTATE, WINDOW)
                    left_soldiers_barrack.append(left_soldier)
                    left_group.add(left_soldier)

                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(ROTATE, WINDOW)
                    right_soldiers_barrack.append(right_soldier)
                    right_group.add(right_soldier)
                
                if event.key == pygame.K_r:
                    main()
        
        # draw_window(left_tower, right_tower)
        left_tower.draw_tower()
        right_tower.draw_tower()
        right_group.add(right_tower)
        left_group.add(left_tower)

        for entity in left_soldiers_barrack:
            entity.summon_soldier()
            if entity.collide == False:
                entity.move_soldier()
            elif entity.collide == True:
                entity.stop_soldier()
                
            entity.collision_detector(right_group)
            continue

        for entity in right_soldiers_barrack:
            entity.summon_soldier()
            if entity.collide == False:
                entity.move_soldier()
            elif entity.collide == True:
                entity.stop_soldier()
            entity.collision_detector(left_group)
            continue
            
        pygame.display.update()


if __name__ == "__main__":
    main()
