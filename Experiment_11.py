# Simulate elliptical orbits in Pygame.
import pygame
import math

pygame.init()  # Initialize Pygame

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
c1 = (0, 0, 0)
c2 = (0, 255, 232)

# Function to calculate the position of an object in an elliptical orbit
def calculate_position(a, b, angle):
    x = a * math.cos(angle)
    y = b * math.sin(angle)
    return int(x), int(y)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elliptical Orbit Simulation")
clock = pygame.time.Clock()

# Elliptical orbit parameters
semimajor_axis = 200
semiminor_axis = 100
angular_speed = 1  # Adjust this value to change the speed of the orbit
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Calculate the position of the object in the elliptical orbit
    obj_x, obj_y = calculate_position(semimajor_axis, semiminor_axis, angle)
    # Clear the screen
    screen.fill(c1)
    # Draw the elliptical orbit
    pygame.draw.ellipse(screen, c2, (WIDTH // 2 - semimajor_axis, HEIGHT // 2 - semiminor_axis,
                                     2 * semimajor_axis, 2 * semiminor_axis), 1)
    # Draw the object in the elliptical orbit
    pygame.draw.circle(screen, c2, (WIDTH // 2 + obj_x, HEIGHT // 2 + obj_y), 10)

    # Update the angle for the next frame
    angle += angular_speed
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
