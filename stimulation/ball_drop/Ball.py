import pygame
import random

class Ball:
    def __init__(self, x, y, radius=10, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.vx = 0#random.randint(-5, 5)
        self.vy = 0#random.randint(-5, 5)
        self.gravity = 0.5
        self.radius = radius
        self.color = color

    def update(self, width, height):
        # Apply gravity
        self.vy += self.gravity
        
        # Update position
        self.x += self.vx
        self.y += self.vy

        # Bouncing logic for walls
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.vx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.vy *= -0.9  # Dampen bounce to simulate energy loss
            self.y = max(self.radius, min(self.y, height - self.radius))

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
