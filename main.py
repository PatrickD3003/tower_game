import pygame
from tower import Tower

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

# untuk sementara background warnanya white
WINDOW.fill(WHITE)
pygame.display.flip()

# create tower object
TOWER_HEALTH = 100

# left side tower
L_TOWER_WIDTH = 100
L_TOWER_HEIGHT = 200
L_TOWER_X = 20
L_TOWER_Y = HEIGHT - L_TOWER_HEIGHT
# right side tower
R_TOWER_WIDTH = 100
R_TOWER_HEIGHT = 200
R_TOWER_X = WIDTH - R_TOWER_WIDTH - 20
R_TOWER_Y = HEIGHT - R_TOWER_HEIGHT


left_tower = Tower(TOWER_HEALTH, L_TOWER_WIDTH, L_TOWER_HEIGHT, L_TOWER_X, L_TOWER_Y, RED)
right_tower = Tower(TOWER_HEALTH, R_TOWER_WIDTH, R_TOWER_HEIGHT, R_TOWER_X, R_TOWER_Y, RED)
def draw_window(): 
    left_tower.draw_tower()
    right_tower.draw_tower()
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()


main()
