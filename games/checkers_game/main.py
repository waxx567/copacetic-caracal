import pygame
from checkers.constants import WIDTH, HEIGHT

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        pass

main()