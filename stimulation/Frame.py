import pygame
import random
from stimulation.Ball import Ball
from stimulation.Brick import Brick
# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")
class Game:
    def __init__(self):
        self.frame_rate = 60
        self.ball = Ball(r=10,x=400,y=300,vx=0,vy=0,color=(255,0,0))  # Create a Ball instance
        self.brick = Brick(x=100,y=300,w=20,h=50)

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

                    if(Key=="up"):
                        # self.ball.setVy(self.ball.getVy()-3)
                        self.brick.y -= 10

                    if(Key=="down"):
                        # self.ball.setVy(self.ball.getVy()+3)
                        self.brick.y += 10
                    if (Key == "left"):
                        self.ball.setVx(self.ball.getVx()-3)
                    if (Key == "right"):
                        self.ball.setVx(self.ball.getVx()+3)


                elif event.type == pygame.KEYUP:
                    print(f"Key {pygame.key.name(event.key)} released")
                    print("\n")
                

            display.fill((0, 0, 0))  # Clear display with black background

            self.ball.paint(display=display)  # Call the paint() method of the ball instance
            self.brick.paint(display=display)
            pygame.display.flip()  # Update display
            clock.tick(self.frame_rate)  # Control frame rate




# Create and run the game
my_game = Game()
my_game.run()

# Quit pygame
pygame.quit()
