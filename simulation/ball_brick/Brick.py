import pygame
import random

class Brick:
    def __init__(self,xin:int,yin:int,w:int,h:int):
        self.x :int= xin
        self.y :int= yin

        self.width  :int= w
        self.height :int= h

    def getX(self) ->int:
        return self.x

    def setX(self,xin:int):
        self.x = xin
    def getY(self):
        return self.y
    def setY(self, yin):
        self.y = yin
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def paint(self, display: pygame.display): # screen is the pygame screen object
        # Draw ball
        pygame.draw.rect(display, (random.randint(1,255) , random.randint(1,255), random.randint(1,255)), (self.x, self.y, self.width, self.height))

