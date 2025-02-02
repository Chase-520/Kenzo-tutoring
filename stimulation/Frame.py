import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")

# Define ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_dx = 5  # Change in x direction
ball_dy = 5  # Change in y direction
ball_color = (255, 0, 0)

# Clock to control frame rate
clock = pygame.time.Clock()

# Game loop
running = True

"""
Our most important part starts here!!!
"""
while running:
    screen.fill((0, 0, 0))  # Clear screen with black background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Collision detection with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy = -ball_dy

    # Draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
