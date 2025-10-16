import pygame
import random
import os

class Car(pygame.sprite.Sprite):
    def __init__(self, y, speed):
        super().__init__()
        self.image = pygame.image.load(os.path.join(ASSET_DIR, 'cars.png')).convert_alpha()
        self.rect = self.image.get_rect(
            topleft=(random.choice([-100, WIDTH + 100]), y)
        )
        self.speed = speed if self.rect.x < 0 else -speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()