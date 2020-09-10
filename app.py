import pygame
# import random

pygame.init()

win_size = {'x': 1000, 'y': 800}
window = pygame.display.set_mode((win_size['x'], win_size['y']))
pygame.display.set_caption('Tic Tac Toe')

clock = pygame.time.Clock()
fps = 60

background = pygame.image.load('./img/bg.png')


class Frame:
    frame = pygame.image.load('./img/frame.png')
    frame = pygame.transform.scale(frame, (600, 200))
    x_margin = 25

    @staticmethod
    def draw():
        pygame.draw.rect(window, (255, 255, 255), (Tile.size + Frame.x_margin, Tile.size * 3,
                                                   Tile.size * 3 - Frame.x_margin * 2, Tile.size))
        window.blit(Frame.frame, (Tile.size, Tile.size * 3))


class Tile:
    size = 200
    border = pygame.image.load('./img/border.png')
    border = pygame.transform.scale(border, (size, size))
    body = pygame.image.load('./img/tile-gray.png')
    body = pygame.transform.scale(body, (size, size))
    x_img = pygame.image.load('./img/x.png')
    x_img = pygame.transform.scale(x_img, (size, size))
    y_img = pygame.image.load('./img/o.png')
    y_img = pygame.transform.scale(y_img, (size, size))

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sign = None

    def draw(self):
        window.blit(self.body, (self.x, self.y))
        if self.sign:
            window.blit(self.sign, (self.x, self.y))
        window.blit(self.border, (self.x, self.y))

        if self.detect_mouse():
            print(self.x, self.y)

    def detect_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (((mouse_x >= self.x) and (mouse_x <= self.x + Tile.size)) and
                ((mouse_y >= self.y) and (mouse_y <= self.y + Tile.size)))


tiles = [[Tile(Tile.size + i * Tile.size, j * Tile.size) for j in range(3)] for i in range(3)]
frame = Frame()


def display_window():
    window.blit(background, (0, 0))

    for row_of_tiles in tiles:
        for tile in row_of_tiles:
            tile.draw()

    frame.draw()

    pygame.display.update()


run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print('click')

    display_window()

pygame.quit()
