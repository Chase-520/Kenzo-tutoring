import pygame
import random
class Brick:

    def __init__(self, x:int,y:int,w:int,h:int):
        self.width : int = w
        self.height :int = h
        self.x :int = x
        self.y :int= y


    def paint(self, display: pygame.display): # screen is the pygame screen object
        # Update ball position


        # Draw ball
        pygame.draw.rect(display, (0, 0, 255), (self.x, self.y, self.width, self.height))

