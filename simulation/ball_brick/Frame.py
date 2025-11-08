import pygame
import random
import time
import PIL
import pygame.tests
from simulation.ball_brick.Ball import Ball
from simulation.ball_brick.Brick import Brick
from PIL import Image

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")


# Set up font
font = pygame.font.Font(None, 50)  # None uses default font, 50 is size

filenames =r"C:\Users\kenzo\OneDrive\Pictures\oneshot.jpg"

class Game:



    def __init__(self):
        self.frame_rate = 60
        self.ball = Ball(r=10,x=400,y=300,vx=0,vy=0,color=(255,0,0))  # Create a Ball instance

        self.brick = Brick(xin=50,yin=300,w=30,h=300)
        self.brick2 = Brick(xin=750,yin=300,w=30,h=300)

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
                self.brick.setY(self.brick.getY() + -20)
                pass
            if keys[pygame.K_DOWN]:
                self.brick.setY(self.brick.getY() + 20)
                pass

            if keys[pygame.K_LEFT]:
                self.brick.setX(self.brick.getX() + -20)
                pass

            if keys[pygame.K_RIGHT]:
                self.brick.setX(self.brick.getX() + 20)
                pass
            if keys[pygame.K_SPACE]:
                self.ball.setVx(random.randint(-10,10))
                self.ball.setVy(random.randint(-10,10))
                pass
            if keys[pygame.K_r]:
                self.ball.setX(400)
                self.ball.setY(300)
                self.ball.setVx(random.randint(-10, 10))
                self.ball.setVy(random.randint(-10, 10))
                pass

            #Brick2
            if keys[pygame.K_w]:
                self.brick2.setY(self.brick2.getY() + -20)
                pass
            if keys[pygame.K_s]:
                self.brick2.setY(self.brick2.getY() + 20)
                pass

            if keys[pygame.K_a]:
                self.brick2.setX(self.brick2.getX() + -20)
                pass

            if keys[pygame.K_d]:
                self.brick2.setX(self.brick2.getX() + 20)
                pass
                

            display.fill((0, 0, 0))  # Clear display with black background


            self.ball.checkCollision(self.brick)

            self.ball.paint(display=display,brick=self.brick)  # Call the paint() method of the ball instance
            self.brick.paint(display=display)
            self.brick2.paint(display=display)

            if self.ball.getX() <= 2:
                self.scoreL += 1
            if self.ball.getX() >= 798:
                self.scoreR += 1


            # TODO Display score
            string = f"my score is {self.scoreL}"
            # print(string)
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
