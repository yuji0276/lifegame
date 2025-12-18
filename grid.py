import pygame

# --- 設定 ---
TILE_SIZE = 60  # 1マスの大きさ (60x60px)
MARGIN_X = 50   # 画面左端からの余白
MARGIN_Y = 50   # 画面上端からの余白

# --- クラス定義 ---
class Block(pygame.sprite.Sprite):
    def __init__(self, col, row): # 引数でグリッド座標(col, row)を受け取る
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((100, 100, 100)) # グレーの壁
        self.rect = self.image.get_rect()
        
        # ★ここで「グリッド座標」を「スクリーン座標」に変換してセット
        self.rect.x = MARGIN_X + (col * TILE_SIZE)
        self.rect.y = MARGIN_Y + (row * TILE_SIZE)

class Player(pygame.sprite.Sprite):
    def __init__(self, col, row):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((0, 255, 100)) # 緑のプレイヤー
        self.rect = self.image.get_rect()
        
        # 同じ変換式を使用
        self.rect.x = MARGIN_X + (col * TILE_SIZE)
        self.rect.y = MARGIN_Y + (row * TILE_SIZE)

# --- マップデータ ---
# W=壁, P=プレイヤー, .=床(何もしない)
MAP_LAYOUT = [
    "WWWWWWWW",
    "W......W",
    "W..P...W",
    "W...W..W",
    "WWWWWWWW"
]

# --- メイン処理 ---
pygame.init()
screen = pygame.display.set_mode((600, 400))

all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group() # 壁だけを入れるグループ（当たり判定用）

# ★マップデータの読み込みとインスタンス化★
for row_idx, row_data in enumerate(MAP_LAYOUT):     # 行のループ (0, 1, 2...)
    for col_idx, char in enumerate(row_data):       # 列のループ (文字を取り出す)
        
        if char == "W":
            wall = Block(col_idx, row_idx) # グリッド座標を渡す
            all_sprites.add(wall)
            walls.add(wall)
        
        elif char == "P":
            player = Player(col_idx, row_idx)
            all_sprites.add(player)

# --- ゲームループ ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    all_sprites.draw(screen) # 全員描画
    
    # 補助線（グリッド線）を描いて確認
    for r in range(len(MAP_LAYOUT) + 1):
        y = MARGIN_Y + r * TILE_SIZE
        pygame.draw.line(screen, (50, 50, 50), (0, y), (600, y))
    for c in range(len(MAP_LAYOUT[0]) + 1):
        x = MARGIN_X + c * TILE_SIZE
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 400))

    pygame.display.flip()

pygame.quit()