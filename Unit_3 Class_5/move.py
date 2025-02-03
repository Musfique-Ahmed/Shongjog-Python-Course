import pygame

#Initialize Pygame
pygame.init()

##Window
screen = pygame.display.set_mode((1000, 800)) #Screen size
pygame.display.set_caption("My Shapes") #Title

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0, 255, 0)

x, y = 200, 300

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), 30)

    pygame.display.update()

# Quit
pygame.quit()
