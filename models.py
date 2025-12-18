import pygame

class Cell(pygame.sprite.Sprite):
    size = 10
    def __init__(self, col, row, cell_type):
        super().__init__()
        self.image = pygame.Surface((Cell.size, Cell.size))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = col * Cell.size
        self.rect.y = row * Cell.size


        # cell_type 0: dead, 1: alive
        if cell_type == 0:
            self.image.fill((0,0,0))
        elif cell_type == 1:
            self.image.fill((255,255,255))