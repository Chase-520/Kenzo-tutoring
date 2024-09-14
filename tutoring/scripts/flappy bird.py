import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game Variables
GRAVITY = 0.25
FLAP_STRENGTH = -6.5
PIPE_SPEED = 4
PIPE_GAP = 200

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load and scale images
bird_image = pygame.image.load('../database/image/cbt1-bird.png')
bird_width = int(SCREEN_WIDTH * 0.2)
bird_height = int(bird_width * bird_image.get_height() / bird_image.get_width())
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))

background_image = pygame.image.load('../database/image/bg.jpg')

pipe_image = pygame.image.load('../database/image/cbt1-pipe.png')
pipe_width = int(SCREEN_WIDTH * 0.2)
pipe_height = int(pipe_width * pipe_image.get_height() / pipe_image.get_width())
pipe_image = pygame.transform.scale(pipe_image, (pipe_width, pipe_height))


# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.image = bird_image
        self.vel_y = 0
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y
        self.rect.y = self.y

    def flap(self):
        self.vel_y = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.image_top = pygame.transform.flip(pipe_image, False, True)
        self.image_bottom = pipe_image
        self.rect_top = self.image_top.get_rect(topleft=(self.x, self.height - PIPE_GAP))
        self.rect_bottom = self.image_bottom.get_rect(topleft=(self.x, self.height + PIPE_GAP))

    def update(self):
        self.x -= PIPE_SPEED
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

    def draw(self, screen):
        screen.blit(self.image_top, self.rect_top.topleft)
        screen.blit(self.image_bottom, self.rect_bottom.topleft)


# Main game function
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + 200)]
    score = 0
    running = True
    pygame.time.wait(1000)  # Wait for 1 second before starting
    while running:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit the game")
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()
        bird.draw(screen)

        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe(SCREEN_WIDTH + 200))

        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)

        # Remove off-screen pipes
        if pipes[0].x < -pipe_image.get_width():
            pipes.pop(0)

        # Check for collisions
        for pipe in pipes:
            if bird.rect.colliderect(pipe.rect_top) or bird.rect.colliderect(pipe.rect_bottom):
                print("Collision with pipe!")
                running = False

        # Check if bird hits the ground
        if bird.y >= SCREEN_HEIGHT - bird_image.get_height():
            print("Bird hit the ground!")
            running = False

        # Check if bird goes above the screen
        if bird.y < 0:
            print("Bird went above the screen!")
            running = False

        # Update the display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
