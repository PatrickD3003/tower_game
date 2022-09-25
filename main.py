import pygame
from soldier import Soldier

pygame.init()

width, height = 900, 500
fps = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tower Game")

# basic colors rgb black white
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# untuk sementara background warnanya white
screen.fill(WHITE)
pygame.display.flip()

def move(soldier):
    x, y = soldier.move()
    screen.blit(soldier.img, (x, y))
    pass

def main():
    running = True
    clock = pygame.time.Clock()
    spawn = False
    soldiers = []

    while running:
        clock.tick(fps)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # summon left side soldier
                    spawn = True
                    first = Soldier("ogre sprite.png", "1", "ogre")
                    soldiers.append(first)
                if event.key == pygame.K_2:  # summon left side soldier
                    spawn = True
                    second = Soldier("ogre sprite.png", "2", "ogre")
                    soldiers.append(second)

        if spawn:
            for soldier in soldiers:
                move(soldier)

        pygame.display.update()

if __name__ == '__main__':
    main()