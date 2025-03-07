import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Battle - Human Rights")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_ship_img = pygame.image.load("C:/Users/MD Saiful Islam/index.py/p/player_ship.png") 
enemy_ship_img = pygame.image.load("C:/Users/MD Saiful Islam/index.py/p/enemy_ship.png")    
player_x = screen_width // 2 - 25
player_y = screen_height - 60
player_speed = 5

enemy_speed = 2
enemies = []

bullet_speed = 7
bullets = []
enemy_bullets = []

score = 0

clock = pygame.time.Clock()

def move_player(x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= player_speed
    if keys[pygame.K_RIGHT] and x < screen_width - 50:
        x += player_speed
    return x, y

def create_enemy():
    enemy_x = random.randint(0, screen_width - 50)
    enemy_y = random.randint(-100, -40)
    enemies.append([enemy_x, enemy_y])

def move_enemies():
    global score
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemies.remove(enemy)
            score -= 1
            create_enemy()

        if random.randint(1, 100) < 2: 
            enemy_bullets.append([enemy[0] + 20, enemy[1] + 50])

def move_bullets():
    global score
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        for enemy in enemies[:]:
            if bullet[0] in range(enemy[0], enemy[0] + 50) and bullet[1] in range(enemy[1], enemy[1] + 50):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                create_enemy()

    for enemy_bullet in enemy_bullets[:]:
        enemy_bullet[1] += bullet_speed
        if enemy_bullet[1] > screen_height:
            enemy_bullets.remove(enemy_bullet)

        if player_x in range(enemy_bullet[0], enemy_bullet[0] + 50) and player_y in range(enemy_bullet[1], enemy_bullet[1] + 10):
            print("You were hit!")
            enemy_bullets.remove(enemy_bullet)
            score -= 1 

def game():
    global player_x, player_y, bullets, score, enemies, enemy_bullets
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    bullets.append([player_x + 20, player_y]) 


        player_x, player_y = move_player(player_x, player_y)

        move_enemies()

        move_bullets()

        score_text = pygame.font.SysFont('Arial', 30).render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        screen.blit(player_ship_img, (player_x, player_y)) 
        for enemy in enemies:
            screen.blit(enemy_ship_img, (enemy[0], enemy[1]))  

        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], 5, 10))

        for enemy_bullet in enemy_bullets:
            pygame.draw.rect(screen, RED, (enemy_bullet[0], enemy_bullet[1], 5, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

for _ in range(5):
    create_enemy()


game()