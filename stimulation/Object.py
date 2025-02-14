import pygame
import random
class Ball:

    def __init__(self, r:int,x:int,y:int,vx:int,vy:int,color:tuple):
        self.radius : int = r
        self.x :int = x
        self.y :int= y
        self.vx :int= vx  # Change in x direction
        self.vy :int = vy  # Change in y direction
        self.color :tuple= color

    def get_Vx(self):
        return self.vx
    
    def paint(self, display: pygame.display): # screen is the pygame screen object
        # Update ball position
        self.x += self.vx
        self.y += self.vy


        # Draw ball
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

