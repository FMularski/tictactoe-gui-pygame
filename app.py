import pygame
import random

pygame.init()

win_size = {'x': 1000, 'y': 800}
window = pygame.display.set_mode((win_size['x'], win_size['y']))
pygame.display.set_caption('Tic Tac Toe')

clock = pygame.time.Clock()
fps = 60

background = pygame.image.load('./img/bg.png')
font = pygame.font.Font(pygame.font.get_default_font(), 24)


class Tile:
    size = 200
    border = pygame.image.load('./img/border.png')
    border = pygame.transform.scale(border, (size, size))
    body = pygame.image.load('./img/tile-gray.png')
    body = pygame.transform.scale(body, (size, size))
    x_img = pygame.image.load('./img/x.png')
    x_img = pygame.transform.scale(x_img, (size, size))
    o_img = pygame.image.load('./img/o.png')
    o_img = pygame.transform.scale(o_img, (size, size))

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sign = None

    def draw(self):
        window.blit(self.body, (self.x, self.y))
        if self.sign:
            window.blit(self.sign, (self.x, self.y))
        window.blit(self.border, (self.x, self.y))

    def detect_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (((mouse_x >= self.x) and (mouse_x <= self.x + Tile.size)) and
                ((mouse_y >= self.y) and (mouse_y <= self.y + Tile.size)))

    def set_sign(self, sign):
        self.sign = sign


class Frame:
    frame = pygame.image.load('./img/frame.png')
    frame = pygame.transform.scale(frame, (600, 200))
    x_margin = 25
    y_margin = 25
    x_pos = Tile.size + x_margin
    y_pos = Tile.size * 3

    text_color = 52, 187, 191
    text = font.render('Welcome to Tic Tac Toe!', True, text_color)
    text_x = x_pos + x_margin
    text_y = y_pos + y_margin

    @staticmethod
    def draw():
        pygame.draw.rect(window, (255, 255, 255), (Frame.x_pos, Frame.y_pos,
                                                   Tile.size * 3 - Frame.x_margin * 2, Tile.size))
        window.blit(Frame.frame, (Tile.size, Tile.size * 3))
        window.blit(Frame.text, (Frame.text_x, Frame.text_y))

    @staticmethod
    def set_text(text):
        Frame.text = font.render(text, True, Frame.text_color)


def player_move():
    global players_turn

    for tile_row in tiles:
        for tile in tile_row:
            if tile.detect_mouse():
                if tile.sign:
                    Frame.set_text('Position occupied.')
                else:
                    tile.set_sign(Tile.o_img)
                    players_turn = False


def cpu_move():
    global players_turn

    # ...
    players_turn = True


tiles = [[Tile(Tile.size + i * Tile.size, j * Tile.size) for j in range(3)] for i in range(3)]
frame = Frame()


def check_win(sign):
    return ((tiles[0][0].sign == sign and tiles[0][1].sign == sign and tiles[0][2].sign == sign) or
            (tiles[1][0].sign == sign and tiles[1][1].sign == sign and tiles[1][2].sign == sign) or
            (tiles[2][0].sign == sign and tiles[2][1].sign == sign and tiles[2][2].sign == sign) or

            (tiles[0][0].sign == sign and tiles[1][0].sign == sign and tiles[2][0].sign == sign) or
            (tiles[0][1].sign == sign and tiles[1][1].sign == sign and tiles[2][1].sign == sign) or
            (tiles[0][2].sign == sign and tiles[1][2].sign == sign and tiles[2][2].sign == sign) or

            (tiles[0][0].sign == sign and tiles[1][1].sign == sign and tiles[2][2].sign == sign) or
            (tiles[0][2].sign == sign and tiles[1][1].sign == sign and tiles[2][0].sign == sign))


players_turn = True  # bool(random.getrandbits(1))


def display_window():
    global players_turn

    window.blit(background, (0, 0))

    for row_of_tiles in tiles:
        for tile in row_of_tiles:
            tile.draw()

    frame.set_text('Player\'s turn' if players_turn else 'CPU turn')
    frame.draw()

    pygame.display.update()


run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if players_turn:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_move()
        else:
            cpu_move()

    if check_win(Tile.o_img if players_turn else Tile.x_img):
        print('game over')

    display_window()

pygame.quit()
