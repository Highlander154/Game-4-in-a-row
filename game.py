import pygame, sys
from pygame.locals import *
from main import VER, VER_DATE

WIN_SIZE = [1280, 800]
WIN_WIDTH = WIN_SIZE[0]
WIN_HEIGHT = WIN_SIZE[1]
FPS = 60

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 0, 255]
BG_COLOR = BLACK

NUM_ROW = 4
NUM_COL = 4
EMPTY_SLOT = ' '

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption(f"in a row - v{VER} {VER_DATE}")
ICON = pygame.image.load('img/Number 4 Icon _ Red Orb Alphabet Iconset.png').convert_alpha()
pygame.display.set_icon(ICON)


def create_board(slot: str = ' ', width: int = 7, height: int = 6):
    row = [slot for _ in range(width)]  # create a row placeholder
    game_board = [row.copy() for _ in range(height)]  # create board with row placeholders
    return game_board


def render_board(game_board: list):
    font = pygame.font.SysFont('Consolas', 28, True)
    tile_size = (WIN_HEIGHT-200)//NUM_ROW
    radius = (tile_size*0.7)//2
    pygame.draw.rect(window, BLUE, (100, 100, tile_size*NUM_COL, WIN_HEIGHT-200), 0)

    for row in range(NUM_ROW):
        for col in range(NUM_COL):
            pygame.draw.circle(window, BG_COLOR, (100+col*tile_size+(tile_size//2), 100+row*tile_size+(tile_size//2)),
                               radius, 0)
    for col in range(NUM_COL):
        column_nr = font.render(f'{col+1}', True, WHITE)
        column_nr_rect = column_nr.get_rect(center=((100+col*tile_size+(tile_size//2)), 50))
        window.blit(column_nr, column_nr_rect)


def is_valid_move(game_board: list, col: int, empty_slot=' '):
    # check if user selected column still has at least 1 valid open slot (check if top slot is free)
    if game_board[0][col] == empty_slot:
        return True
    return False


board = create_board(slot=EMPTY_SLOT, width=NUM_COL, height=NUM_ROW)
print(board)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit('\nProgram terminated by user.')

        if event.type == KEYDOWN:
            # number keys trigger a coin drop in the corresponding column
            if event.key == K_1 and NUM_COL >= 1:
                print("Pressed '1'")
                col_idx = 0
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_2 and NUM_COL >= 2:
                print("Pressed '2'")
                col_idx = 1
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_3 and NUM_COL >= 3:
                print("Pressed '3'")
                col_idx = 2
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_4 and NUM_COL >= 4:
                print("Pressed '4'")
                col_idx = 3
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_5 and NUM_COL >= 5:
                print("Pressed '5'")
                col_idx = 4
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_6 and NUM_COL >= 6:
                print("Pressed '6'")
                col_idx = 5
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_7 and NUM_COL >= 7:
                print("Pressed '7'")
                col_idx = 6
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_8 and NUM_COL >= 8:
                print("Pressed '8'")
                col_idx = 7
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_9 and NUM_COL >= 9:
                print("Pressed '9'")
                col_idx = 8
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))
            if event.key == K_0 and NUM_COL == 10:
                print("Pressed '0'")
                col_idx = 9
                print("Valid move: ", is_valid_move(game_board=board, col=col_idx, empty_slot=EMPTY_SLOT))

    window.fill(BG_COLOR)

    # Game Logic
    render_board(board)

    pygame.display.update()
    clock.tick(FPS)
