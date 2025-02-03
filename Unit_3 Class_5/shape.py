import pygame

#Initialize Pygame
pygame.init()

##Window
screen = pygame.display.set_mode((500, 400)) #Screen size
pygame.display.set_caption("My Shapes") #Title

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0, 255, 0)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (200, 200, 50, 100))#(parameters of top left corner, length, hight)
    pygame.draw.circle(screen, BLUE, (100, 100), 30)#(parameter of center), radious

    pygame.draw.polygon(screen, GREEN, [(400,200), (200,300), (400,300)])
    # pygame.draw.line()

    pygame.display.update()

# Quit
pygame.quit()

# Draw a triangle -> polygon
# draw a line 