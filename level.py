import pygame

level_map = [
"                              ",
"                              ",
"                              ",
"                              ",
"                              ",
"                              ",
"T                            T",
"T                            T",
"T                            T",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

# 10 x 30

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

total_width = len(level_map[0]) * 64

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Level:
    def __init__(self, surface):
        self.display_surface = surface
        self.setup_level(level_map)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
