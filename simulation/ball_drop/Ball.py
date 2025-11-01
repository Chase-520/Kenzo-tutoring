import pygame
import random

class Ball:
    def __init__(self, x, y, radius=10, color=(random.randint(0,255), 0, 0)):
        self.x = x
        self.y = y
        self.vx = random.randint(-5,5)#random.randint(-5, 5)
        self.vy = random.randint(-5,5)#random.randint(-5, 5)
        self.gravity = random.randint(-5,5)
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
        if self.x <= 0:
            self.vx = -self.vx
        if self.y <= 0:
            self.vx = -self.vx

        if self.x >= 800:
            self.x = 800
        if self.x <= 0:
            self.x = 0
        if self.y >= 600:
            self.y = 600
        if self.y <= 0:
            self.y = 50
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        pass



    def check_collision(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance <= self.radius + other.radius:
            # Simple elastic collision response
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

    def draw(self, display):
        self.update(800,600)
        pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), self.radius)
