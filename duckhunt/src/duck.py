import pygame
import random

class Duck:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load(r"C:\Users\chase\OneDrive\Desktop\froggerassets\FroggerAssets\log.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pos = self.image.get_rect(topleft=(x, y))
        self.speed_x = speed
        self.speed_y = speed
        self.alive = True
        self.show_bbox = True

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.pos.topleft)
            if self.show_bbox:
                pygame.draw.rect(screen, (0, 255, 0), self.pos, 2)
