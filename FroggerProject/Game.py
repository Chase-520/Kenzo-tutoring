import pygame
import random
import os
from Car import Car
from Frog import Frog

# Constants
WIDTH, HEIGHT = 600, 700
FPS = 60

ASSET_DIR = r"C:\Users\chase\OneDrive\Desktop\froggerassets\FroggerAssets"



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frogger")
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = pygame.image.load(os.path.join(r"C:\Users\chase\OneDrive\Desktop\froggerassets\FroggerAssets", 'tiles.png')).convert()
        self.frog = Frog()
        self.frog_group = pygame.sprite.GroupSingle(self.frog)
        self.cars = pygame.sprite.Group()
        self.font = pygame.font.SysFont(None, 36)
        self.score = 0
        self.car_spawn_timer = 0

    def spawn_car(self):
        lane_y = random.choice([150, 220, 290, 360, 430])
        speed = random.randint(5, 10)
        self.cars.add(Car(lane_y, speed))

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)
            self._handle_events()
            self._update()
            self._draw()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        keys = pygame.key.get_pressed()
        self.frog.update(keys)

        self.car_spawn_timer += 1
        if self.car_spawn_timer > 40:
            self.spawn_car()
            self.car_spawn_timer = 0

        self.cars.update()

        if pygame.sprite.spritecollideany(self.frog, self.cars):
            self.frog.reset_position()

        if self.frog.rect.top <= 0:
            self.score += 1
            self.frog.reset_position()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.cars.draw(self.screen)
        self.frog_group.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

if __name__ == "__main__":
    Game().run()
    pygame.quit()
