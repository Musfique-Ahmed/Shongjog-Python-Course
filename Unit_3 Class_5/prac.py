import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball OR DIE")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5
player_width = 80
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 8

running = True
while running:
    pygame.time.delay(30)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < WIDTH - player_width:
        player_x += player_speed

    ball_y += ball_speed
    if ball_y + ball_radius >= player_y and player_x < ball_x < player_x + player_width:
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0  

    if ball_y > HEIGHT:
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0  

    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)  
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.display.update()  

pygame.quit()
