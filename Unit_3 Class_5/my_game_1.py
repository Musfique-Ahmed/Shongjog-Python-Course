# import pygame
# import random

# pygame.init()

# screen = pygame.display.set_mode((1000, 500))
# pygame.display.set_caption("Catcht The Ball") #Title

# # Colors
# WHITE = (255,255,255)
# RED = (255,0,0)
# BLUE = (0,0,255)
# GREEN = (0, 255, 0)

# player_x, player_y = 400, 450
# ball_x, ball_y = random.randint(50, 950), 0
# speed = 5

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_x>0:
#         player_x -= 5
#     if keys[pygame.K_RIGHT] and player_x<800:
#         player_x += 5

#     ball_y += speed
#     if ball_y > 500:
#         ball_x, ball_y = random.randint(50, 950), 0
    
#     screen.fill(WHITE)
#     pygame.draw.rect(screen, GREEN, (player_x, player_y, 200, 50))
#     pygame.draw.circle(screen, RED, (ball_x, ball_y), 10)

#     pygame.display.update()


# pygame.quit()


import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Catch The Ball")  # Title

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

player_x, player_y = 400, 450
ball_x, ball_y = random.randint(50, 950), 0
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < 800:
        player_x += 5

    ball_y += speed
    if ball_y > 500:
        ball_x, ball_y = random.randint(50, 950), 0

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_x, player_y, 200, 50))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), 10)

    pygame.display.update()

pygame.quit()