import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Master")
clock = pygame.time.Clock()

# Colours
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
MINT_GREEN = (189, 255, 177)
DARK_BLUE = (26, 13, 171)
GOLD = (255, 215, 0)
SOFT_PINK = (255, 182, 50)
PROGRESS_GREEN = (50, 205, 50)

# Fonts
font = pygame.font.SysFont("Arial", 48)
small_font = pygame.font.SysFont("Arial", 30)
title_font = pygame.font.SysFont("Verdana", 60)
entry_font = pygame.font.SysFont("Arial", 36)

# Generate Math Question
def generate_question(difficulty):
    if difficulty == 1:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operator = random.choice(['+', '-'])
    elif difficulty == 2:
        num1, num2 = random.randint(1, 20), random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
    else:
        num1, num2 = random.randint(1, 50), random.randint(1, 50)
        operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = round(num1 / num2, 2)

    return f"What is {num1} {operator} {num2}?", answer, operator

# Display Text
def display_text(text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Give Hint
def give_hint(operator):
    hints = {
        '+': "Add the numbers together",
        '-': "Subtract the second number from the first",
        '*': "Multiply the numbers",
        '/': "Divide the first number by the second"
    }
    return hints.get(operator, "You're doing great! Keep going!")

# Progress Bar
def draw_progress_bar(progress):
    pygame.draw.rect(screen, (200, 200, 200), (20, HEIGHT - 40, WIDTH - 40, 20))
    pygame.draw.rect(screen, PROGRESS_GREEN, (20, HEIGHT - 40, (WIDTH - 40) * (progress / 100), 20))

# Ask for Name
def ask_for_name():
    user_name = ""
    input_active = True
    while input_active:
        screen.fill(LIGHT_BLUE)
        display_text("Enter Your Name:", title_font, DARK_BLUE, 20, 100)
        display_text(user_name, entry_font, DARK_BLUE, WIDTH // 2 - 100, HEIGHT // 2)
        pygame.draw.rect(screen, MINT_GREEN, pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 50, 240, 50), border_radius=15)
        display_text("Press Enter To Start", small_font, WHITE, WIDTH // 2 - 100, HEIGHT // 2 + 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_name != "":
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode
    return user_name

# Draw Hint Button
def draw_hint_button():
    button_rect = pygame.Rect(WIDTH - 160, HEIGHT - 80, 150, 50)
    pygame.draw.rect(screen, MINT_GREEN, button_rect, border_radius=15)
    display_text("Hint", small_font, WHITE, WIDTH - 140, HEIGHT - 65)
    return button_rect

# Intro Screen
def intro_screen():
    while True:
        screen.fill(LIGHT_BLUE)
        display_text("Welcome to Math Buddy!", title_font, DARK_BLUE, 50, 50)
        display_text("Test Your Math Skills And Become A Math Genius!", entry_font, WHITE, 100, 200)
        display_text("Press Any Key To Start Playing!", small_font, MINT_GREEN, 200, 300)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

# Main Game
def math_game(user_name):
    score = 0
    total_questions = 5
    current_question = 0
    difficulty = 1
    question, correct_answer, operator = generate_question(difficulty)
    answer_input = ""
    game_over = False
    hint = ""

    while not game_over:
        screen.fill(LIGHT_BLUE)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if float(answer_input) == correct_answer:
                            score += 1
                    except ValueError:
                        pass

                    answer_input = ""
                    current_question += 1
                    if current_question >= total_questions:
                        game_over = True
                    else:
                        question, correct_answer, operator = generate_question(difficulty)
                        hint = ""
                elif event.key == pygame.K_BACKSPACE:
                    answer_input = answer_input[:-1]
                else:
                    answer_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if draw_hint_button().collidepoint(event.pos):
                    hint = give_hint(operator)

        display_text("Math Buddy!", title_font, DARK_BLUE, 20, 50)
        display_text(question, font, DARK_BLUE, 20, 150)
        display_text(f"Your Answer: {answer_input}", font, WHITE, 20, 220)
        display_text(f"Score: {score}", font, GOLD, 20, 20)

        draw_hint_button()
        draw_progress_bar((current_question / total_questions) * 100)

        pygame.display.update()
        clock.tick(60)

    # Game Over Screen - This keeps the window open
    while True:
        screen.fill(LIGHT_BLUE)
        display_text("Game Over!", title_font, DARK_BLUE, WIDTH // 2 - 130, HEIGHT // 2 - 50)
        display_text(f"Final Score: {score}/{total_questions}", font, DARK_BLUE, WIDTH // 2 - 130, HEIGHT // 2 + 10)
        display_text("Press Q to Quit or R to Restart", small_font, WHITE, WIDTH // 2 - 130, HEIGHT // 2 + 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    math_game(user_name)  # Restart the game

# Start Game
if __name__ == "__main__":
    user_name = ask_for_name()
    intro_screen()
    math_game(user_name)