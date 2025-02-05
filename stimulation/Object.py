import pygame
import random
class Ball:

    def __init__(self):
        self.radius = 20
        self.x = 0
        self.y = 0
        self.vx = 5  # Change in x direction
        self.vy = 5  # Change in y direction
        self.color = (255, 0, 0)

    def get_Vx(self):
        return self.vx
    def paint(self, display: pygame.display): # screen is the pygame screen object
        # Update ball position
        self.x += self.vx
        self.y += self.vy

        # Draw ball
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)
