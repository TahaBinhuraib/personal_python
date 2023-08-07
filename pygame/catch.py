import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BALL_COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

clock = pygame.time.Clock()


def draw_paddle(x):
    pygame.draw.rect(screen, WHITE, (x, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT))


def draw_ball(x, y, color):
    pygame.draw.circle(screen, color, (x, y), BALL_RADIUS)


def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))


def draw_menu():
    font = pygame.font.Font(None, 48)
    text1 = font.render("Catch the Ball!", True, WHITE)
    text2 = font.render("Press SPACE to start", True, WHITE)
    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 3))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2))

    pygame.display.update()


def game_loop():
    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    ball_x, ball_y = random.randint(0, WIDTH), 0
    score = 0

    in_menu = True
    ball_color = random.choice(BALL_COLORS)  # Initialize ball color outside

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    in_menu = False

        screen.fill(BLACK)

        draw_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= 5
        if keys[pygame.K_RIGHT]:
            paddle_x += 5

        # keep the paddle within the screen boundaries
        paddle_x = max(0, min(paddle_x, WIDTH - PADDLE_WIDTH))

        # I want to make this dynamic
        ball_y += 5

        # Check if the ball hit
        if ball_y + BALL_RADIUS >= HEIGHT - PADDLE_HEIGHT and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
            ball_x, ball_y = random.randint(0, WIDTH), 0
            score += 1

            ball_color = random.choice(BALL_COLORS)

        # Check if the ball touches the bottom of the screen
        if ball_y + BALL_RADIUS >= HEIGHT:
            print("Game Over HAHA! Your Score:", score)
            pygame.quit()
            return

        screen.fill(BLACK)

        draw_paddle(paddle_x)
        draw_ball(ball_x, ball_y, ball_color)

        draw_score(score)

        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
