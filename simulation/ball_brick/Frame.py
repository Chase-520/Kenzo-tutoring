import pygame
import random
import time

import pygame.tests
from stimulation.ball_brick.Ball import Ball
from stimulation.ball_brick.Brick import Brick

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
        self.ball = Ball(r=10,x=400,y=300,vx=0,vy=0,color=(255,0,0))  # Create a Ball instance

        self.brick = Brick(xin=50,yin=300,w=30,h=300)

        self.scoreL = 0
        self.scoreR = 0


    def run(self):
        running = True
        clock = pygame.time.Clock()  # Control frame rate
        startTime = time.time()
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


            self.ball.checkCollision(self.brick)

            self.ball.paint(display=display,brick=self.brick)  # Call the paint() method of the ball instance
            self.brick.paint(display=display)

            # TODO Score check
            if(self.ball.getX()<10):
                self.scoreR +=1
            if(self.ball.getX()>789):
                self.scoreL +=1

            # TODO Display score
            string = f"my score is {self.scoreL}"
            print(string)
            leftScore = font.render(f"scoreL: {self.scoreL}", True, (255, 255, 255))  # White text
            display.blit(leftScore, (50, 50))  # Draw text at (100, 100)

            rightScore = font.render(f"scoreR: {self.scoreR}", True, (255, 255, 255))  # White text
            display.blit(rightScore, (550, 50))  # Draw text at (100, 100)

            timer = font.render(f"Time: {int(time.time()-startTime)}", True, (255, 255, 255))  # White text
            display.blit(timer, (300, 400))

            pygame.display.flip()  # Update display
            clock.tick(self.frame_rate)  # Control frame rate




# Create and run the game
my_game = Game()
my_game.run()

# Quit pygame
pygame.quit()
