import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        super().__init__()
        self.row = row
        self.col = col
        self.color = color