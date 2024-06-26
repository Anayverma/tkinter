# Simulate bouncing ball using Pygame
import pygame
import sys

pygame.init()  # Initialize Pygame

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x =3
ball_speed_y =3

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off the walls
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > WIDTH:
        ball_speed_x *= -1
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y *= -1

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(FPS)
