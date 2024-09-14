import pygame
import random

# Initialize pygame
pygame.init()

# Set constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
CELL_PADDING = 10
FONT = pygame.font.SysFont('arial', 40)
BACKGROUND_COLOR = (187, 173, 160)
CELL_COLORS = {
    0: (205, 193, 180), 2: (238, 228, 218), 4: (237, 224, 200),
    8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
    64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
    512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)
}
TEXT_COLORS = {2: (119, 110, 101), 4: (119, 110, 101), 8: (249, 246, 242)}

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Helper functions
def start_game():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_random_number(grid)
    add_random_number(grid)
    return grid

def add_random_number(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

def draw_grid(grid):
    screen.fill(BACKGROUND_COLOR)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            color = CELL_COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (j * CELL_SIZE + CELL_PADDING, i * CELL_SIZE + CELL_PADDING, CELL_SIZE - 2 * CELL_PADDING, CELL_SIZE - 2 * CELL_PADDING))
            if value != 0:
                text_color = TEXT_COLORS.get(value, (255, 255, 255))
                text_surface = FONT.render(str(value), True, text_color)
                text_rect = text_surface.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)
    pygame.display.update()

def compress(grid):
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        pos = 0
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                pos += 1
    return new_grid

def merge(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    return grid

def reverse(grid):
    return [row[::-1] for row in grid]

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def move_left(grid):
    grid = compress(grid)
    grid = merge(grid)
    grid = compress(grid)
    return grid

def move_right(grid):
    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)
    return grid

def move_up(grid):
    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)
    return grid

def move_down(grid):
    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)
    return grid

def is_game_over(grid):
    if any(0 in row for row in grid):
        return False
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i][j + 1]:
                return False
            if grid[j][i] == grid[j + 1][i]:
                return False
    return True

# Main game loop
def main():
    grid = start_game()
    draw_grid(grid)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    grid = move_left(grid)
                elif event.key == pygame.K_RIGHT:
                    grid = move_right(grid)
                elif event.key == pygame.K_UP:
                    grid = move_up(grid)
                elif event.key == pygame.K_DOWN:
                    grid = move_down(grid)
                add_random_number(grid)
                draw_grid(grid)

                if is_game_over(grid):
                    pygame.quit()
                    print("Game Over!")
                    return

        clock.tick(10)

if __name__ == "__main__":
    main()
