import pygame
import locale
import os
import math

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SEA_BLUE_COLOR = (0, 41, 58)
FPS = 60

lang = {"pl_PL": "Gra w statki",
        "en_EN": "Battleship"}
lang_code, _ = locale.getdefaultlocale()
pygame.display.set_caption(lang.get(lang_code, "Battleship"))
SHIP_4 = pygame.image.load(os.path.join('assets', 'ship_4.png'))
SHIP_4 = pygame.transform.scale(SHIP_4, (20, 120))
SHIP_3 = pygame.image.load(os.path.join('assets', 'ship_3.png'))
SHIP_3 = pygame.transform.scale(SHIP_3, (20, 90))
SHIP_2 = pygame.image.load(os.path.join('assets', 'ship_2.png'))
SHIP_2 = pygame.transform.scale(SHIP_2, (20, 60))
SHIP_1 = pygame.image.load(os.path.join('assets', 'ship_1.png'))
SHIP_1 = pygame.transform.scale(SHIP_1, (20, 30))
BOOM = pygame.image.load(os.path.join('assets', 'boom.png'))
BOOM = pygame.transform.scale(BOOM, (20, 30))

def rotate_ship(ship:pygame.Surface, angle:int=90) -> pygame.Surface:
    """Function that rotate ship"""
    return pygame.transform.rotate(surface=ship, angle=angle)

def draw_board():
    cellSize = 29
    board = pygame.Surface((cellSize * 10, cellSize * 10))
    board.fill(SEA_BLUE_COLOR)
    for x in range(0, 10):
        for y in range(0, 10):
            # pygame.draw.rect(board, SEA_BLUE_COLOR, (x * 30, y * 30, 2, 2))
            pygame.draw.rect(board, (255, 255, 255, 0), (x * 29, y * 29, 29, 29), width=1)
    return board

def get_mouse_position(x:int, y:int):
    cord_x = cord_y = 0
    if 20 <= x <= 310 and 20 <= y <= 320:
        if cord_x <=5:
            cord_x = math.ceil((x - 20) / 30 + 0.1)
            cord_y = math.ceil((y - 20) / 30 + 0.1)
            print(f'x: {x} -> {cord_x}', f'y: {y} -> {cord_y}')
        else:
            cord_x = math.ceil((x - 20) / 30 - 0.1)
            cord_y = math.ceil((y - 20) / 30 - 0.1)
            print(f'x: {x} -> {cord_x}', f'y: {y} -> {cord_y}')
    if 350 <= x <= 640:
        cord_x = math.ceil((x - 350) / 30 + 0.5)
        cord_y = math.ceil((y - 20) / 30 + 0.5)
        print(f'x: {x} -> {cord_x}', f'y: {y} -> {cord_y}')

def window_draw():
    WINDOW.fill(color=SEA_BLUE_COLOR)
    WINDOW.blit(draw_board(), (20, 20))
    WINDOW.blit(draw_board(), (350, 20))

    pygame.display.update()


def main():
    """Main loop of game"""
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                x, y = mouse_position
                get_mouse_position(x, y)
        window_draw()
    pygame.quit()

if __name__ == "__main__":
    main()