from screen import *
from soldier import *
from level import *
from tower import Tower
import math

pygame.init()

left_group = pygame.sprite.Group()
right_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

fps = 60

game_screen = Screen("Game Screen", screen_width, screen_height)
game_screen.set_background("textures/forest.png")
game_screen.use_screen()

menu_screen = Screen("Menu Screen", screen_width, screen_height)

# basic colors rgb black white
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

level_ = Level(game_screen)

left_tower = Tower("1")
right_tower = Tower("2")
left_group.add(left_tower)
right_group.add(right_tower)

def main():
    running = True
    clock = pygame.time.Clock()
    left_team = []
    right_team = []
    scroll = 0
    escape_pressed = False

    while running:
        clock.tick(fps)

        scroll = game_screen.set_scroll(level_)

        if escape_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        escape_pressed = False
                        menu_screen.end_screen()
                        game_screen.use_screen()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_pressed == False:
                        escape_pressed = True
                        game_screen.end_screen()
                        menu_screen.use_screen()
                    else:
                        escape_pressed = False
                        menu_screen.end_screen()
                        game_screen.use_screen()

                if event.key == pygame.K_1:  # summon left side soldier
                    new_left = SoldierMelee("1", "swordsman", 100, 25, 100, 0)
                    left_team.append(new_left)
                    left_group.add(new_left)
                    all_sprites.add(new_left)
                if event.key == pygame.K_2:  # summon left side soldier
                    new_right = SoldierMelee("2", "swordsman", 100, 25, 100, 0)
                    right_team.append(new_right)
                    right_group.add(new_right)
                    all_sprites.add(new_right)


        if left_team != []:
            for mob in left_team:
                if mob.hp > 0:
                    mob.set_scroll(scroll)
                    mob.collision_handler(right_group)

        if right_team != []:
            for mob in right_team:
                if mob.hp > 0:
                    mob.set_scroll(scroll)
                    mob.collision_handler(left_group)

        left_tower.check_hp()
        right_tower.check_hp()
        left_tower.draw_tower(scroll)
        right_tower.draw_tower(scroll)

        menu_screen.update_screen()

        level_.run()
        pygame.display.update()

if __name__ == '__main__':
    main()
