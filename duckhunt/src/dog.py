import pygame

class Dog:
    def __init__(self):
        self.active = True
        self.x = 0
        self.y = 500
        self.speed_x = 5
        self.speed_y = 0
        self.image = pygame.image.load(r"C:\Users\chase\OneDrive\Desktop\froggerassets\FroggerAssets\log.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.fill((139, 69, 19))  # Brown rectangle as dog
        self.pos = self.image.get_rect(topleft=(self.x, self.y))

    def appear(self, duck_x, duck_y):
        """Activate dog to pick up the duck"""
        self.active = True
        self.x = duck_x
        self.y = duck_y

    def move(self):
        """Dog moves to the left off screen when active"""
        if self.active:
            self.x -= self.speed
            if self.x < -100:  # Off screen
                self.active = False

    def catach(self, x,y):
        pass
    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))
