import pygame
import random

class Ball:
    def __init__(self, x, y, radius=10, color=(random.randint(0,255), 0, 0)):
        self.x = x
        self.y = y
        self.vx = random.randint(-50,10)#random.randint(-5, 5)
        self.vy = random.randint(-50,10)#random.randint(-5, 5)
        self.gravity = 0.5
        self.radius = radius
        self.color = color

    def update(self, width, height):
        # apply gravity
        self.vy = self.vy + self.gravity
        # Bouncing logic
        if self.x >= 800:
            self.vx = -self.vx
        if self.y >= 600:
            self.vy = -self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        pass



    def check_collision(self, other):
        
        pass



    def draw(self, display):
        self.update(800,600)
        pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), self.radius)
