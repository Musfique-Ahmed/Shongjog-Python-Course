# import pygame

# #Initialize Pygame
# pygame.init()

# ##Window
# screen = pygame.display.set_mode((500, 400)) #Screen size
# pygame.display.set_caption("My First Pygame") #Title

# # Game Loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # Quit
# pygame.quit()

# modify the sceen size and title according to your choice



import pygame

#initialize pygame
pygame.init()

##window
screen = pygame.display.set_mode((1000, 3000))
pygame.display.set_caption("My First Pygame")

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit
pygame.quit()
