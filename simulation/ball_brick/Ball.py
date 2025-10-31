import pygame
import random
class Ball:

    def __init__(self, r:int,x:int,y:int,vx:int,vy:int,color:tuple):
        self.radius : int = r
        self.x :int = x
        self.y :int= y
        self.vx :int= vx  # Change in x direction
        self.vy :int = vy  # Change in y direction
        self.color :tuple= color # (r,g,b)

    def getRadius(self) ->int:
        return self.radius
    def setRadius(self, r:int):
        self.radius = r
    def getX(self) ->int:
        return self.x
    def setX(self, x:int):
        self.x = x
    def getVx(self) ->int:
        return self.vx
    def setVx(self, vx:int):
        self.vx=vx
    def getVy(self) ->int:
        return self.vy
    def setVy(self, vy:int):
        self.vy = vy

    def paint(self, display: pygame.display, brick): # screen is the pygame screen object
        # Update ball position
        self.x += self.vx
        self.y += self.vy

        # bouncing logic
        if(___ or ___):
            self.vx *= -1

        if(___ or ___<0):
            self.vy = -self.vy


        # Draw ball
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def checkCollision(self, brick):
        if(self.getX()<brick.getX()+brick.getWidth() and (self.y>brick.getY() and self.y<brick.getY()+brick.getHeight())):
            # print(self.vx)
            # print(brick.x)
            self.setVx(-self.getVx())

