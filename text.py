import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

clouds = [
    [50, 80],
    [180, 140],
    [300, 60]
]

def reset_game():
    bird_x = 100
    bird_y = 300
    bird_velocity = 0
    gravity = 0.5

    pipe_x = 400
    pipe_height = random.randint(150, 400)
    pipe_gap = 150

    score = 0
    game_over = False

    return bird_x, bird_y, bird_velocity, gravity, pipe_x, pipe_height, pipe_gap, score, game_over

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, (x, y, 40, 20))
    pygame.draw.ellipse(screen, WHITE, (x + 15, y - 10, 40, 25))
    pygame.draw.ellipse(screen, WHITE, (x + 30, y, 40, 20))

bird_x, bird_y, bird_velocity, gravity, pipe_x, pipe_height, pipe_gap, score, game_over = reset_game()

running = True
while running:
    screen.fill(BLACK)

    
    for cloud in clouds:
        draw_cloud(cloud[0], cloud[1])
        if not game_over:
            cloud[0] -= 1

        if cloud[0] < -80:
            cloud[0] = WIDTH
            cloud[1] = random.randint(30, 200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -8
            else:
                if event.key == pygame.K_r:
                    bird_x, bird_y, bird_velocity, gravity, pipe_x, pipe_height, pipe_gap, score, game_over = reset_game()

    if not game_over:
        
        bird_velocity += gravity
        bird_y += bird_velocity

    
        pipe_x -= 3

        if pipe_x < -50:
            pipe_x = 400
            pipe_height = random.randint(150, 400)
            score += 1

    
        if bird_y < 0 or bird_y > HEIGHT:
            game_over = True

    
        if bird_x > pipe_x and bird_x < pipe_x + 50:
            if bird_y < pipe_height or bird_y > pipe_height + pipe_gap:
                game_over = True

    
    pygame.draw.circle(screen, RED, (bird_x, int(bird_y)), 15)


    pygame.draw.rect(screen, GREEN, (pipe_x, 0, 50, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, 50, HEIGHT))

    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))


    if game_over:
        over_text = big_font.render("GAME OVER", True, WHITE)
        restart_text = small_font.render("Press R to Restart", True, WHITE)

        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()