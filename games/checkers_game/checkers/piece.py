import pygame
from .constants import RED, WHITE, SQUARE_SIZE

class Piece(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        super().__init__()
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2