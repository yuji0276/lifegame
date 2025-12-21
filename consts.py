import pygame

# 画面（ウィンドウ）の設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Life Game")

# FPS制御用
clock = pygame.time.Clock()
running = True

# マップデータ
ROWS = 100
COLS = 100
MAP_LAYOUT = [[0 for _ in range(COLS)] for _ in range(ROWS)]
NEXT_LAYOUT = [[0 for _ in range(COLS)] for _ in range(ROWS)]
NEIBOR_OFFSETS = [
    (-1,0), #上
    (1,0),  #下
    (0,-1), #左
    (0,1),  #右
    (-1,-1), #左上
    (-1,1), #右上
    (1,-1), #左下
    (1,1), #右下
]