# ============================================================
#  tile.py
#
#  OOP concept demonstrated: ENCAPSULATION
#  A Tile knows its value, its position on the grid, and how
#  to draw itself.  Nothing outside needs to know the details.
# ============================================================

import pygame
from typing import Tuple
from constants import (
    TILE_SIZE, GRID_PADDING, GRID_OFFSET_X, GRID_OFFSET_Y,
    TILE_COLORS, TILE_COLOR_DEFAULT,
    COLOR_TEXT_DARK, COLOR_TEXT_LIGHT,
    FONT_TILE_LARGE, FONT_TILE_MEDIUM, FONT_TILE_SMALL,
)


class Tile:
    """Represents a single tile on the 2048 board.

    Attributes
    ----------
    value : int      The numeric value shown on the tile (0 = empty).
    row   : int      Current grid row  (0-indexed from top).
    col   : int      Current grid column (0-indexed from left).
    x, y  : float    Pixel position of the tile's top-left corner
                     (floats so we can animate smoothly).
    """

    def __init__(self, value: int, row: int, col: int):
        self.value = value
        self.row   = row
        self.col   = col
        # Start the tile at the pixel position that corresponds to (row, col)
        self.x, self.y = self._target_pixel()

    # ── Helpers ────────────────────────────────────────────

    def _target_pixel(self) -> Tuple[float, float]:
        """Return the pixel (x, y) for the current logical (row, col)."""
        x = GRID_OFFSET_X + GRID_PADDING + self.col * (TILE_SIZE + GRID_PADDING)
        y = GRID_OFFSET_Y + GRID_PADDING + self.row * (TILE_SIZE + GRID_PADDING)
        return float(x), float(y)

    @property
    def target_x(self) -> float:
        return float(
            GRID_OFFSET_X + GRID_PADDING + self.col * (TILE_SIZE + GRID_PADDING)
        )

    @property
    def target_y(self) -> float:
        return float(
            GRID_OFFSET_Y + GRID_PADDING + self.row * (TILE_SIZE + GRID_PADDING)
        )

    # ── State queries ──────────────────────────────────────

    def is_at_target(self, tolerance: float = 1.0) -> bool:
        """True when the tile's pixel position matches its logical cell."""
        return (
            abs(self.x - self.target_x) <= tolerance
            and abs(self.y - self.target_y) <= tolerance
        )

    # ── Animation ──────────────────────────────────────────

    def snap_to_target(self):
        """Instantly place tile at its logical grid position."""
        self.x, self.y = self.target_x, self.target_y

    def move_towards_target(self, speed: float):
        """Slide one step toward the target position (call every frame)."""
        for attr, target in (("x", self.target_x), ("y", self.target_y)):
            current = getattr(self, attr)
            delta   = target - current
            if abs(delta) <= speed:
                setattr(self, attr, target)
            else:
                setattr(self, attr, current + speed * (1 if delta > 0 else -1))

    # ── Drawing ────────────────────────────────────────────

    def _get_font(self, screen: pygame.Surface) -> pygame.font.Font:
        """Choose font size based on the number of digits in value."""
        digits = len(str(self.value))
        if digits <= 3:
            size = FONT_TILE_LARGE
        elif digits == 4:
            size = FONT_TILE_MEDIUM
        else:
            size = FONT_TILE_SMALL
        return pygame.font.SysFont("Arial", size, bold=True)

    def draw(self, screen: pygame.Surface):
        """Render the tile (background rectangle + centred number)."""
        if self.value == 0:
            return

        # Background
        bg_color = TILE_COLORS.get(self.value, TILE_COLOR_DEFAULT)
        rect = pygame.Rect(int(self.x), int(self.y), TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, bg_color, rect, border_radius=6)

        # Text colour: dark on pale tiles, light on saturated tiles
        text_color = COLOR_TEXT_DARK if self.value <= 4 else COLOR_TEXT_LIGHT

        font   = self._get_font(screen)
        text   = font.render(str(self.value), True, text_color)
        text_x = int(self.x) + (TILE_SIZE - text.get_width())  // 2
        text_y = int(self.y) + (TILE_SIZE - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))
