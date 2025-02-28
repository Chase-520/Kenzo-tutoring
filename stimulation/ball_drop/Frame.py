import pygame
import random

import pygame.tests


# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")


# Set up font
font = pygame.font.Font(None, 50)  # None uses default font, 50 is size



class Game:
    def __init__(self):
        self.frame_rate = 60



    def run(self):
        running = True
        clock = pygame.time.Clock()  # Control frame rate

        while running:
            """
            key board interaction
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    Key = str(pygame.key.name(event.key))
                    print(f"Key: {Key}, Code: {event.key}")
                    print(f"Key {Key} pressed")

                elif event.type == pygame.KEYUP:
                    Key = str(pygame.key.name(event.key))
                    print(f"Key {Key} released")
                    print("\n")
            # Handle continuous key press using get_pressed()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                # Move brick up
                cur_y = self.brick.getY()
                self.brick.setY(cur_y - 13)

            if keys[pygame.K_DOWN]:
                # Move brick down
                cur_y = self.brick.getY()
                self.brick.setY(cur_y + 13)

            if keys[pygame.K_LEFT]:
                # Move brick left (you can add logic for left movement if needed)
                cur_x = self.brick.getX()
                self.brick.setX(cur_x - 13)  # Example: move 13 pixels left

            if keys[pygame.K_RIGHT]:
                # Move brick right (you can add logic for right movement if needed)
                cur_x = self.brick.getX()
                self.brick.setX(cur_x + 13)  # Example: move 13 pixels right

            if keys[pygame.K_SPACE]:
                # Set random velocity for the ball when space is pressed
                self.ball.setVx(random.randint(2, 30))
                self.ball.setVy(random.randint(2, 30))
                

            display.fill((0, 0, 0))  # Clear display with black background

            pygame.display.flip()  # Update display
            clock.tick(self.frame_rate)  # Control frame rate




# Create and run the game
my_game = Game()
my_game.run()

# Quit pygame
pygame.quit()
