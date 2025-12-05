import pygame
import random
from duck import Duck
from gifLoader import GIF

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

def collided(pointer, obj):
    """Return True if two objects collide based on their bounding boxes."""
    x,y = pointer
    frame, pos = obj.update()
    rect = frame.get_rect(center=(pos[0], pos[1]))
    return rect.collidepoint(x, y)

def update_draw(screen, obj):
    frame, pos = obj.update()
    rect = frame.get_rect(center=(pos[0], pos[1]))
    screen.blit(frame,rect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Duck Hunt with Dog")
        self.clock = pygame.time.Clock()
        self.duck = Duck()
        self.running = True 
        self.bg = GIF(r"duckhunt\img\pixelBG.png")

    def draw_text(self,msg:str,x:int,y:int,size:int,color:tuple=(255,255,255)):
        # Create a font object
        font = pygame.font.SysFont(None, size)   # None = default font, 48 = size
        # Render text to a surface
        text_surface = font.render(msg, True, color)  # white
        self.screen.blit(text_surface, (x, y))  # draw text at (x, y)

    def run(self):
        while self.running:
            
            dt = self.clock.tick(30)
            self.screen.fill(WHITE)


            rect = self.bg.get_frame().get_rect(center=self.screen.get_rect().center)
            self.screen.blit(self.bg.get_frame(),rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if collided([x,y],self.duck):
                        self.duck.update("hit")
                    
            
            update_draw(self.screen, self.duck)

            # update text
            self.draw_text(msg="Hi, I'm Chase",x=300, y=300, size=48,color=(0,125,255))

            # display everything
            pygame.display.flip()
            


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
