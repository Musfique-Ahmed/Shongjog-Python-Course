import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1200, 800  # Increased window size
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Minecraft Clone")

WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
BLACK = (0, 0, 0)
BROWN = (101, 67, 33)
GREEN = (50, 205, 50)
GRAY = (128, 128, 128)
YELLOW = (255, 215, 0)

gravity = 0.5
jump_force = -9

player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (TILE_SIZE, TILE_SIZE * 2))

grass_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
grass_image.fill((34, 139, 34))

dirt_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
dirt_image.fill((139, 69, 19))

stone_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
stone_image.fill(GRAY)

log_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
log_image.fill(BROWN)

leaf_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
leaf_image.fill(GREEN)

door_closed_image = pygame.Surface((TILE_SIZE, TILE_SIZE * 2))
door_closed_image.fill(YELLOW)

door_open_image = pygame.Surface((TILE_SIZE, TILE_SIZE * 2))
door_open_image.fill((255, 255, 0))

items = {"Grass": grass_image, "Dirt": dirt_image, "Stone": stone_image, "Log": log_image, "Leaf": leaf_image, "Door": door_closed_image}
current_item = "Grass"
inventory_open = False

doors = []

def generate_chunk(offset_x, previous_height):
    chunk_width = WIDTH // TILE_SIZE  # Updated for wider window
    chunk_data = [[0 for _ in range(chunk_width)] for _ in range(HEIGHT // TILE_SIZE)]
    current_height = previous_height
    tree_positions = sorted(random.sample(range(chunk_width), k=random.randint(1, 2)))
    for col in range(chunk_width):
        change = random.choice([0, 1, -1])
        current_height = max(8, min(current_height + change, 12))
        for row in range(HEIGHT // TILE_SIZE):
            if row == current_height:
                chunk_data[row][col] = 1
                if col in tree_positions:
                    generate_tree(chunk_data, col, current_height)
            elif current_height < row <= current_height + 3:
                chunk_data[row][col] = 2
            elif row > current_height + 3:
                chunk_data[row][col] = 3
    return chunk_data, current_height

def generate_tree(world_data, x, ground_y):
    tree_height = random.randint(3, 4)
    for i in range(tree_height):
        world_data[ground_y - i][x] = 4
    for lx in range(x - 1, x + 2):
        for ly in range(ground_y - tree_height, ground_y - tree_height - 2, -1):
            if 0 <= lx < len(world_data[0]) and 0 <= ly < len(world_data):
                world_data[ly][lx] = 5

def draw_world(world_data, offset_x):
    blocks = []
    for row_index, row in enumerate(world_data):
        for col_index, tile in enumerate(row):
            x = (col_index - offset_x) * TILE_SIZE
            y = row_index * TILE_SIZE
            if tile == 1:
                screen.blit(grass_image, (x, y))
                blocks.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 2:
                screen.blit(dirt_image, (x, y))
                blocks.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 3:
                screen.blit(stone_image, (x, y))
                blocks.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 4:
                screen.blit(log_image, (x, y))
                blocks.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 5:
                screen.blit(leaf_image, (x, y))
                blocks.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 6:
                screen.blit(door_closed_image, (x, y - TILE_SIZE))
                doors.append(pygame.Rect(x, y - TILE_SIZE, TILE_SIZE, TILE_SIZE * 2))
    return blocks

def handle_mouse(world_data, offset_x, player_rect):
    mouse_pos = pygame.mouse.get_pos()
    grid_x = (mouse_pos[0] // TILE_SIZE) + offset_x
    grid_y = mouse_pos[1] // TILE_SIZE
    if 0 <= grid_x < len(world_data[0]) and 0 <= grid_y < len(world_data):
        if pygame.mouse.get_pressed()[2]:
            if not pygame.Rect(grid_x * TILE_SIZE, grid_y * TILE_SIZE, TILE_SIZE, TILE_SIZE).colliderect(player_rect):
                if current_item == "Grass":
                    world_data[grid_y][grid_x] = 1
                elif current_item == "Dirt":
                    world_data[grid_y][grid_x] = 2
                elif current_item == "Stone":
                    world_data[grid_y][grid_x] = 3
                elif current_item == "Log":
                    world_data[grid_y][grid_x] = 4
                elif current_item == "Leaf":
                    world_data[grid_y][grid_x] = 5
                elif current_item == "Door":
                    if grid_y - 1 >= 0:
                        world_data[grid_y][grid_x] = 6
                        world_data[grid_y - 1][grid_x] = 0
        elif pygame.mouse.get_pressed()[0]:
            world_data[grid_y][grid_x] = 0

def handle_interact(world_data, offset_x, player_rect):
    for door in doors:
        if player_rect.colliderect(door):
            index_x = (door.x // TILE_SIZE) + offset_x
            index_y = door.y // TILE_SIZE + 1
            if world_data[index_y][index_x] == 6:
                world_data[index_y][index_x] = 0
            else:
                world_data[index_y][index_x] = 6

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.spawn_x = x
        self.spawn_y = y
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y = 0
        self.on_ground = False

    def respawn(self):
        self.rect.topleft = (self.spawn_x, self.spawn_y)
        self.vel_y = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = jump_force
            self.on_ground = False

    def update(self, blocks):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keys[pygame.K_a]:
            dx = -5
        if keys[pygame.K_d]:
            dx = 5
        if keys[pygame.K_SPACE]:
            self.jump()
        if keys[pygame.K_r]:
            handle_interact(world_data, offset_x, self.rect)
        self.vel_y += gravity
        dy += self.vel_y
        for block in blocks:
            if block.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            if block.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y > 0:
                    dy = block.top - self.rect.bottom
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    dy = block.bottom - self.rect.top
                    self.vel_y = 0
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.top > HEIGHT:
            self.respawn()

def main():
    global current_item, inventory_open, world_data, offset_x
    clock = pygame.time.Clock()
    player = Player(100, HEIGHT // 2)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    offset_x = 0
    previous_height = 10
    world_data, previous_height = generate_chunk(offset_x, previous_height)
    while True:
        screen.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    inventory_open = not inventory_open
                elif event.key == pygame.K_1:
                    current_item = "Grass"
                elif event.key == pygame.K_2:
                    current_item = "Dirt"
                elif event.key == pygame.K_3:
                    current_item = "Stone"
                elif event.key == pygame.K_4:
                    current_item = "Log"
                elif event.key == pygame.K_5:
                    current_item = "Leaf"
                elif event.key == pygame.K_6:
                    current_item = "Door"
        handle_mouse(world_data, offset_x, player.rect)
        if player.rect.x > WIDTH - TILE_SIZE:
            offset_x += WIDTH // TILE_SIZE
            new_chunk, previous_height = generate_chunk(offset_x, previous_height)
            for i in range(len(world_data)):
                world_data[i].extend(new_chunk[i])
            player.rect.x = TILE_SIZE
        blocks = draw_world(world_data, offset_x)
        player.update(blocks)
        player_group.draw(screen)
        pygame.display.update()
        clock.tick(75)

if __name__ == "__main__":
    main()