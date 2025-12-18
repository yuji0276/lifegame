import pygame
from models import Cell
from consts import screen, running, clock, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_LAYOUT, NEIBOR_OFFSETS, NEXT_LAYOUT
import copy
all_sprites = pygame.sprite.Group()

# マップデータの読み込みとインスタンス化
# 背景を灰色で塗りつぶす
screen.fill((113,115,117))
# グループ内の全てのセルを描画する
for row_idx, row_data in enumerate(MAP_LAYOUT):
    for col_idx, cell_type in enumerate(row_data):
        cell = Cell(col_idx, row_idx, cell_type)
        all_sprites.add(cell)
all_sprites.draw(screen)

# ゲームループ
while running:
    # イベント処理（閉じるボタンが押されたか）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 世代交代
    for row_idx, row_data in enumerate(MAP_LAYOUT):
        for col_idx, cell_type in enumerate(row_data):
            count = 0
            #隣接するセルの探索
            for row_offset, col_offset in NEIBOR_OFFSETS:
                neighbor_row = row_idx + row_offset
                neighbor_col = col_idx + col_offset
                neighbor_cell_type = 0
                #境界チェック
                if 0 <= neighbor_row < len(MAP_LAYOUT) and 0 <= neighbor_col < len(MAP_LAYOUT[0]):
                    neighbor_cell_type = MAP_LAYOUT[neighbor_row][neighbor_col]
                else:
                    continue
                if neighbor_cell_type == 1:
                    count += 1
            if NEXT_LAYOUT[row_idx][col_idx] == 1:
                if count == 2 or count == 3:
                    NEXT_LAYOUT[row_idx][col_idx] = 1
                else:
                    NEXT_LAYOUT[row_idx][col_idx] = 0
            else:
                if count == 3:
                    NEXT_LAYOUT[row_idx][col_idx] = 1
                else:
                    NEXT_LAYOUT[row_idx][col_idx] = 0
    # 世代交代
    MAP_LAYOUT = copy.deepcopy(NEXT_LAYOUT)
    # 画面を更新して変更を反映
    all_sprites.empty()

    # グループ内の全てのセルを描画する
    for row_idx, row_data in enumerate(MAP_LAYOUT):
        for col_idx, cell_type in enumerate(row_data):
            cell = Cell(col_idx, row_idx, cell_type)
            all_sprites.add(cell)
    all_sprites.draw(screen)
    for r in range(len(MAP_LAYOUT)):
        y = r * Cell.size
        pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))
    for c in range(len(MAP_LAYOUT[0])):
        x = c * Cell.size
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x,SCREEN_HEIGHT))
    pygame.display.flip()
    # フレームレートの制御
    clock.tick(2)
# ゲーム終了処理
pygame.quit()
