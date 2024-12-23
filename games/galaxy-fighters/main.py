import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")

WHITE = (255, 255, 255)

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            red.x -= 10
        if keys_pressed[pygame.K_RIGHT]:
            red.x += 10
        if keys_pressed[pygame.K_UP]:
            red.y -= 10
        if keys_pressed[pygame.K_DOWN]:
            red.y += 10
        if keys_pressed[pygame.K_a]:
            yellow.x -= 10
        if keys_pressed[pygame.K_d]:
            yellow.x += 10
        if keys_pressed[pygame.K_w]:
            yellow.y -= 10
        if keys_pressed[pygame.K_s]:
            yellow.y += 10
            
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()