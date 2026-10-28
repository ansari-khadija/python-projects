
import pygame
import random

pygame.init()

# ------------------------------------------
# 1. CREATE THE GAME WINDOW
# ------------------------------------------

WIDTH = 800
HEIGHT = 600

CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.SysFont("arial", 48, bold=True)
font = pygame.font.SysFont("arial", 28, bold=True)
small_font = pygame.font.SysFont("arial", 18)

# Colors
BACKGROUND = (20, 28, 38)
GRID_COLOR = (29, 39, 50)
GREEN = (70, 220, 100)
DARK_GREEN = (35, 160, 70)
RED = (255, 80, 80)
WHITE = (255, 255, 255)
GOLD = (255, 210, 70)

# ------------------------------------------
# 2. CREATE THE SNAKE
# ------------------------------------------

def reset_game():

    global snake, direction, next_direction
    global food, score, game_over, won, move_timer

    # Each tuple represents one grid cell (x, y).
    snake = [
        (10, 10),
        (9, 10),
        (8, 10)
    ]

    # Initial direction: moving right.
    direction = (1, 0)
    next_direction = direction

    score = 0
    game_over = False
    won = False
    move_timer = 0

    # Create the first food.
    food = create_food()


# ------------------------------------------
# 3. CREATE FOOD AT A RANDOM POSITION
# ------------------------------------------

def create_food():

    # Find all grid cells not occupied by the snake.
    empty_cells = [
        (x, y)
        for x in range(WIDTH // CELL_SIZE)
        for y in range(HEIGHT // CELL_SIZE)
        if (x, y) not in snake
    ]

    # Return None if the snake fills the entire grid.
    if not empty_cells:
        return None

    return random.choice(empty_cells)


# ------------------------------------------
# 4. DRAW THE BACKGROUND GRID
# ------------------------------------------

def draw_grid():

    screen.fill(BACKGROUND)

    # Vertical grid lines.
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen, GRID_COLOR,
            (x, 0), (x, HEIGHT)
        )

    # Horizontal grid lines.
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen, GRID_COLOR,
            (0, y), (WIDTH, y)
        )


# ------------------------------------------
# 5. DRAW THE SNAKE
# ------------------------------------------

def draw_snake():

    for index, segment in enumerate(snake):

        x, y = segment

        rect = pygame.Rect(
            x * CELL_SIZE + 1,
            y * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2
        )

        # Make the head a brighter green.
        color = GREEN if index == 0 else DARK_GREEN

        pygame.draw.rect(
            screen, color, rect,
            border_radius=5
        )


# ------------------------------------------
# 6. DRAW THE FOOD
# ------------------------------------------

def draw_food():

    if food is None:
        return

    x, y = food

    center = (
        x * CELL_SIZE + CELL_SIZE // 2,
        y * CELL_SIZE + CELL_SIZE // 2
    )

    pygame.draw.circle(
        screen, RED, center, CELL_SIZE // 2 - 2
    )


# ------------------------------------------
# 7. DISPLAY THE SCORE
# ------------------------------------------

def draw_score():

    score_text = font.render(
        f"Score: {score}", True, GOLD
    )

    screen.blit(score_text, (15, 12))

    controls = small_font.render(
        "Move: Arrows / WASD",
        True, WHITE
    )

    screen.blit(
        controls,
        (WIDTH - controls.get_width() - 15, 20)
    )


# ------------------------------------------
# 8. DRAW THE GAME OVER SCREEN
# ------------------------------------------

def draw_game_over():

    # Transparent dark overlay.
    overlay = pygame.Surface(
        (WIDTH, HEIGHT), pygame.SRCALPHA
    )

    overlay.fill((0, 0, 0, 190))
    screen.blit(overlay, (0, 0))

    if won:
        message = "YOU WIN!"
        color = GOLD
    else:
        message = "GAME OVER"
        color = RED

    title = title_font.render(
        message, True, color
    )

    score_message = font.render(
        f"Final Score: {score}", True, WHITE
    )

    restart_message = small_font.render(
        "Press R to restart or ESC to quit",
        True, WHITE
    )

    screen.blit(
        title,
        title.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 65)
        )
    )

    screen.blit(
        score_message,
        score_message.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )
    )

    screen.blit(
        restart_message,
        restart_message.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 55)
        )
    )


# ------------------------------------------
# 9. INITIALIZE THE GAME
# ------------------------------------------

reset_game()

running = True

# Snake movement speed in cells per second.
MOVE_DELAY = 120  # milliseconds between moves

# ------------------------------------------
# 10. MAIN GAME LOOP
# ------------------------------------------

while running:

    # Measure time for smooth, controlled movement.
    elapsed = clock.tick(60)
    move_timer += elapsed

    # --------------------------------------
    # HANDLE EVENTS
    # --------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            # Restart after losing or winning.
            if event.key == pygame.K_r and (game_over or won):
                reset_game()

            # Change direction only during gameplay.
            if not game_over and not won:

                if event.key in (pygame.K_UP, pygame.K_w):
                    if direction != (0, 1):
                        next_direction = (0, -1)

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    if direction != (0, -1):
                        next_direction = (0, 1)

                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if direction != (1, 0):
                        next_direction = (-1, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if direction != (-1, 0):
                        next_direction = (1, 0)

    # --------------------------------------
    # MOVE THE SNAKE
    # --------------------------------------

    if not game_over and not won:

        if move_timer >= MOVE_DELAY:

            move_timer = 0

            direction = next_direction

            head_x, head_y = snake[0]
            dx, dy = direction

            new_head = (
                head_x + dx,
                head_y + dy
            )

            # Check whether the snake hits a wall.
            if (
                new_head[0] < 0
                or new_head[0] >= WIDTH // CELL_SIZE
                or new_head[1] < 0
                or new_head[1] >= HEIGHT // CELL_SIZE
            ):
                game_over = True

            else:

                # If eating food, the snake grows.
                eating = new_head == food

                # The tail moves away unless food is eaten.
                body_to_check = (
                    snake if eating else snake[:-1]
                )

                # Check collision with the snake's body.
                if new_head in body_to_check:
                    game_over = True

                else:

                    # Add the new head.
                    snake.insert(0, new_head)

                    if eating:

                        score += 1

                        # SOUND TUTORIAL — ADD LATER AT HOME:
                        #
                        # 1. Create a folder called "sounds"
                        #    beside this Python file.
                        #
                        # 2. Put collect.wav in that folder.
                        #
                        # 3. After pygame.init(), initialize audio:
                        #    pygame.mixer.init()
                        #
                        # 4. Load the sound:
                        #    from pathlib import Path
                        #    SOUND_DIR = Path(__file__).resolve().parent / "sounds"
                        #    collect_sound = pygame.mixer.Sound(
                        #        str(SOUND_DIR / "collect.wav")
                        #    )
                        #
                        # 5. Here, after score += 1, add:
                        #    collect_sound.play()
                        #
                        # Sound() loads an effect.
                        # play() plays it when food is eaten.

                        food = create_food()

                        # Win if every cell is occupied.
                        if food is None:
                            won = True

                    else:

                        # Remove the tail to keep the same length.
                        snake.pop()

    # --------------------------------------
    # DRAW EVERYTHING
    # --------------------------------------

    draw_grid()
    draw_food()
    draw_snake()
    draw_score()

    if game_over or won:
        draw_game_over()

    pygame.display.flip()

pygame.quit()
