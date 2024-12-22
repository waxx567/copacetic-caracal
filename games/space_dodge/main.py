import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

SHOT_WIDTH = 10
SHOT_HEIGHT = 20

PLAYER_VELOCITY = 5
SHOT_VELOCITY = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, shots):
    WIN.blit(BG, (0, 0))

    time_label = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_label, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for shot in shots:
        pygame.draw.rect(WIN, "white", shot)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    shot_add_increment = 2000
    shot_counter = 0

    shots = []

    hit = False

    while run:
        shot_counter += clock.tick(60)
        elapsed_time = time.time() - start_time

        if shot_counter >= shot_add_increment:
            for _ in range(3):
                shot_x = random.randint(0, WIDTH - SHOT_WIDTH)
                shot = pygame.Rect(shot_x, -SHOT_HEIGHT, SHOT_WIDTH, SHOT_HEIGHT)
                shots.append(shot)

            shot_add_increment = max(200, shot_add_increment - 50)
            shot_counter = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for shot in shots[:]:
            shot.y += SHOT_VELOCITY
            if shot.y > HEIGHT:
                shots.remove(shot)
            elif shot.y + shot.height >= player.y and shot.colliderect(player):
                shots.remove(shot)
                hit = True
                break

        if hit:
            lost_label = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, HEIGHT / 2 - lost_label.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, shots)

    pygame.quit()


if __name__ == "__main__":
    main()