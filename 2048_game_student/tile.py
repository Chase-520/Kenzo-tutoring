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
        """Return True when this tile's pixel position (self.x, self.y)
        is close enough to its target pixel position (self.target_x, self.target_y).

        Use the tolerance parameter to allow a small margin of error
        so the animation does not jitter forever.

        HINT: Use abs() to check the distance on each axis.
        Both x AND y must be within tolerance for this to return True.
        """
        # TODO: implement this method
        # Placeholder keeps the game runnable until you implement it
        return True

    # ── Animation ──────────────────────────────────────────

    def snap_to_target(self):
        """Instantly place tile at its logical grid position."""
        self.x, self.y = self.target_x, self.target_y

    def move_towards_target(self, speed: float):
        """Slide this tile one step closer to its target pixel position.

        Called every frame while the tile is animating.
        'speed' is the maximum number of pixels to move per frame.

        HINT: Do this independently for both self.x and self.y:
          1. delta = target - current
          2. If abs(delta) <= speed  -->  snap directly to target (avoid overshooting)
          3. Otherwise               -->  move 'speed' pixels toward target
                                         use (1 if delta > 0 else -1) to get the sign
        """
        # TODO: implement this method
        # Placeholder snaps instantly so the game is still playable
        self.snap_to_target()

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

        self.x,self.y = self._target_pixel()
        font   = self._get_font(screen)
        text   = font.render(str(self.value), True, text_color)
        text_x = int(self.x) + (TILE_SIZE - text.get_width())  // 2
        text_y = int(self.y) + (TILE_SIZE - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))