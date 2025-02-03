import pygame

#Initialize Pygame
pygame.init()
WHITE = (255,255,255)

##Window
screen = pygame.display.set_mode((500, 400)) #Screen size
pygame.display.set_caption("My First Pygame") #Title

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space key pressed!")


    screen.fill(WHITE)
    pygame.display.update()

# Quit
pygame.quit()