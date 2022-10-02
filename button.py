import pygame


class Button():
    def __init__(self, color, width, height, text=''):
        self.color = color
        self.width = width
        self.height = height
        self.text = text


    def draw(self, surface, x, y, font_color, font_size, bold, outline=None):
        self.x = x
        self.y = y

        if outline:
            pygame.draw.rect(surface, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('FFF Forward', font_size, bold=bold)
            text = font.render(self.text, 1, font_color)
            surface.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2 + 2)))


    def is_clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False