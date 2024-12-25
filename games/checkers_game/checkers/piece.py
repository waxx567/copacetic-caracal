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