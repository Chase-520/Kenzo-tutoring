from bullet import Bullet

class Gun:
    def __init__(self):
        self.bullets = []

    def shoot(self, x, y):
        bullet = Bullet(x, y)
        self.bullets.append(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
