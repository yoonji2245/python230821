import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 640
screen_height = 480
ball_speed = [5, -5]
paddle_speed = 5
block_rows = 5
block_cols = 8

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")

# Create the paddle
paddle_width = 100
paddle_height = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)

# Create blocks
block_width = 75
block_height = 20
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height + 50, block_width, block_height)
        blocks.append(block)

# Initialize game variables
ball_dx, ball_dy = ball_speed
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed

    # Update ball position
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_dy > 0:
        ball_dy = -ball_dy

    # Ball collision with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_dy = -ball_dy

    # Check if ball falls out of the screen
    if ball.bottom >= screen_height:
        game_over = True

    # Clear the screen
    screen.fill(black)

    # Draw paddle, ball, and blocks
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, blue, ball)
    for block in blocks:
        pygame.draw.rect(screen, random.choice([green, red]), block)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
