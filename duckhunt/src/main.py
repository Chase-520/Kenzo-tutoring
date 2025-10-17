import pygame
import random
from player import Player

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

def collided(pointer, obj):
    """Return True if two objects collide based on their bounding boxes."""
    x,y = pointer
    frame, pos = obj.update(input=None)
    rect = frame.get_rect(center=(pos[0], pos[1]))
    return rect.collidepoint(x, y)

def update_draw(screen, obj, input=None):
    frame, pos = obj.update(input=None)
    rect = frame.get_rect(center=(pos[0], pos[1]))
    screen.blit(frame,rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Duck Hunt with Dog")
        self.clock = pygame.time.Clock()
        self.duck = Player()
        self.running = True 

    def run(self):
        while self.running:
            dt = self.clock.tick(30)
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if collided([x,y],self.duck):
                        self.duck.change_state()
                    
            

            
            update_draw(self.screen, self.duck)
            pygame.display.flip()
            

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
