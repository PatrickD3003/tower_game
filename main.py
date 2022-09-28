from soldier import *
from level import *
from tower import Tower
import math

pygame.init()

mob1 = pygame.sprite.Group()
mob2 = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

width, height = screen_width, screen_height
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
    image = pygame.image.load(texture)
    image = pygame.transform.scale(image, (width, height))
    return image


background = set_background("textures/forest.png")
background.convert()
background_width = background.get_width()

level_ = Level(screen)

left_tower = Tower("1")
right_tower = Tower("2")


def main():
    running = True
    clock = pygame.time.Clock()
    team1 = []
    team2 = []
    scroll = 0
    tiles = math.ceil(width / background.get_width()) + 1

    while running:
        clock.tick(fps)

        for i in range(-5, tiles):
            screen.blit(background, (i * background_width + scroll, 0))

        mx, my = pygame.mouse.get_pos()

        if 1 < mx <= width * 0.1: #left
            print(scroll)
            if scroll <= -2:
                scroll += 4
                level_.world_shift = 4
            else:
                level_.world_shift = 0
        elif width - 1 > mx >= width * 0.9: #right
            print(scroll)
            if scroll >= -720:
                scroll -= 4
                level_.world_shift = -4
            else:
                level_.world_shift = 0
        else:
            level_.world_shift = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # summon left side soldier
                    first = Soldier("1", "swordsman", 100, 25, 100)
                    team1.append(first)
                    mob1.add(first)
                    all_sprites.add(first)
                if event.key == pygame.K_2:  # summon left side soldier
                    second = Soldier("2", "swordsman", 100, 25, 100)
                    team2.append(second)
                    mob2.add(second)
                    all_sprites.add(second)


        if team1 != []:
            for mob in team1:
                if mob.hp > 0:
                    mob.attack_handler_melee(mob2, scroll)

        if team2 != []:
            for mob in team2:
                if mob.hp > 0:
                    mob.attack_handler_melee(mob1, scroll)

        left_tower.draw_tower(scroll)
        right_tower.draw_tower(scroll)

        level_.run()
        pygame.display.update()

if __name__ == '__main__':
    main()
