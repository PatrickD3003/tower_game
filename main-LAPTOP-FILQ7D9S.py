from screen import *
from soldier import *
from level import *
from tower import Tower
from hp_bar import *
from point_bar import *
import math

pygame.init()

left_group = pygame.sprite.Group()
right_group = pygame.sprite.Group()
hp_bars = pygame.sprite.Group()
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

left_tower_hp = HealthBar(left_tower)
right_tower_hp = HealthBar(right_tower)

left_points = PointBar("1")
right_points = PointBar("2")


def main():
    running = True
    clock = pygame.time.Clock()
    left_team = []
    right_team = []
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

            menu_screen.update_screen()
            pygame.display.update()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not escape_pressed:
                        escape_pressed = True
                        game_screen.end_screen()
                        menu_screen.use_screen()
                    else:
                        escape_pressed = False
                        menu_screen.end_screen()
                        game_screen.use_screen()

                if event.key == pygame.K_1:  # summon left side soldier
                    if left_points.game_points >= 1:
                        new_left = SoldierMelee("1", "swordsman", 100, 25, 100, 0, 1)
                        left_team.append(new_left)
                        left_group.add(new_left)
                        all_sprites.add(new_left)
                        left_points.game_points -= 1
                    else:
                        print("not enough")
                if event.key == pygame.K_2:  # summon left side soldier
                    if right_points.game_points >= 1:
                        new_right = SoldierMelee("2", "swordsman", 100, 25, 100, 0, 1)
                        right_team.append(new_right)
                        right_group.add(new_right)
                        all_sprites.add(new_right)
                        right_points.game_points -= 1
                    else:
                        print("not enough")


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

        left_tower.draw_tower(scroll)
        right_tower.draw_tower(scroll)

        left_tower_hp.set_scroll(scroll)
        right_tower_hp.set_scroll(scroll)

        left_tower_hp.update_bar(left_tower)
        right_tower_hp.update_bar(right_tower)

        left_points.add_points()
        right_points.add_points()

        menu_screen.update_screen()

        level_.run()
        pygame.display.update()

if __name__ == '__main__':
    main()
