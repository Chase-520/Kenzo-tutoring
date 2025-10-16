import pygame
import random
from duck import Duck
from gun import Gun
from dog import Dog

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

def check_collision(obj1, obj2):
    """Return True if two objects collide based on their bounding boxes."""
    return obj1.pos.colliderect(obj2.pos)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Duck Hunt with Dog")
        self.clock = pygame.time.Clock()
        self.ducks = [Duck(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, 5)) for _ in range(5)]
        self.gun = Gun()
        self.dog = Dog()
        self.running = True 

    def run(self):
        while self.running:
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for duck in self.ducks:
                        if duck.alive and (abs(duck.x-x)<50) and (abs(duck.y-y)<50):
                            duck.alive = False
                            self.dog.appear(duck.x, duck.y)

            # Move and draw ducks
            for duck in self.ducks:
                pos = duck.pos
                # check x bouncing
                if pos.x > 800 or pos.x<30:
                    duck.speed_x *= -1
                
                # check y bouncing
                if pos.y <0 or pos.y >550:
                    duck.speed_y *= -1

                duck.update()
                duck.draw(self.screen)

            # Check for collisions: dog vs ducks
            # for duck in self.ducks:
            #     if check_collision(duck,self.dog):
            #         print("collides")


            # # Move and draw dog
            # self.dog.move()
            # self.dog.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
