# ============================================================
#  renderer.py
#
#  OOP concept demonstrated: SINGLE RESPONSIBILITY PRINCIPLE
#  The Renderer's one job is drawing things on the screen.
#  It knows nothing about game rules — it just receives a
#  Board and a Game object and paints whatever it's told to.
# ============================================================

import pygame
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    GRID_SIZE, GRID_PADDING, GRID_OFFSET_X, GRID_OFFSET_Y, TILE_SIZE,
    COLOR_BG, COLOR_GRID_BG, COLOR_EMPTY_CELL,
    COLOR_TEXT_DARK, COLOR_TEXT_LIGHT, COLOR_TITLE,
    COLOR_SCORE_BG, COLOR_SCORE_TEXT, COLOR_OVERLAY,
    FONT_UI, FONT_TITLE, FONT_MSG,
)


class Renderer:
    """Draws the entire game every frame.

    Usage
    -----
    renderer = Renderer(screen)
    renderer.draw(board, score, best_score, state)
    """

    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        # Pre-load fonts once (expensive to recreate each frame)
        self._font_title  = pygame.font.SysFont("Arial", FONT_TITLE,  bold=True)
        self._font_ui     = pygame.font.SysFont("Arial", FONT_UI,     bold=True)
        self._font_msg    = pygame.font.SysFont("Arial", FONT_MSG,    bold=True)
        self._font_hint   = pygame.font.SysFont("Arial", 18)

    # ── Public entry point ─────────────────────────────────

    def draw(self, board, score: int, best_score: int, state: str):
        """Render a complete frame.

        Parameters
        ----------
        board      : Board   Current board (provides .tiles)
        score      : int
        best_score : int
        state      : str     'playing' | 'won' | 'game_over'
        """
        self._draw_background()
        self._draw_header(score, best_score)
        self._draw_grid()
        self._draw_tiles(board.tiles)

        if state == "won":
            self._draw_overlay("You Win! 🎉", "Press R to restart")
        elif state == "game_over":
            self._draw_overlay("Game Over!", "Press R to restart")

        pygame.display.flip()

    # ── Private drawing helpers ────────────────────────────

    def _draw_background(self):
        self._screen.fill(COLOR_BG)

    def _draw_header(self, score: int, best_score: int):
        """Title on the left, score boxes on the right."""
        # Title
        title_surf = self._font_title.render("2048", True, COLOR_TITLE)
        self._screen.blit(title_surf, (GRID_OFFSET_X, 18))

        # Score boxes
        self._draw_score_box("SCORE", score,      WINDOW_WIDTH - 220, 20)
        self._draw_score_box("BEST",  best_score, WINDOW_WIDTH - 110, 20)

        # Keyboard hint
        hint = self._font_hint.render(
            "Arrow keys / WASD  •  R = restart", True, (150, 140, 130)
        )
        self._screen.blit(hint, (GRID_OFFSET_X, GRID_OFFSET_Y - 26))

    def _draw_score_box(self, label: str, value: int, x: int, y: int):
        box_w, box_h = 100, 55
        rect = pygame.Rect(x, y, box_w, box_h)
        pygame.draw.rect(self._screen, COLOR_SCORE_BG, rect, border_radius=6)

        lbl  = self._font_hint.render(label, True, (238, 228, 218))
        val  = self._font_ui.render(str(value), True, COLOR_SCORE_TEXT)

        self._screen.blit(lbl, (x + (box_w - lbl.get_width()) // 2, y + 6))
        self._screen.blit(val, (x + (box_w - val.get_width()) // 2, y + 24))

    def _draw_grid(self):
        """Draw the grey grid background and empty cell slots."""
        grid_px = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * GRID_PADDING
        grid_rect = pygame.Rect(GRID_OFFSET_X, GRID_OFFSET_Y, grid_px, grid_px)
        pygame.draw.rect(self._screen, COLOR_GRID_BG, grid_rect, border_radius=8)

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x = GRID_OFFSET_X + GRID_PADDING + c * (TILE_SIZE + GRID_PADDING)
                y = GRID_OFFSET_Y + GRID_PADDING + r * (TILE_SIZE + GRID_PADDING)
                pygame.draw.rect(
                    self._screen, COLOR_EMPTY_CELL,
                    (x, y, TILE_SIZE, TILE_SIZE), border_radius=6
                )

    def _draw_tiles(self, tiles):
        """Tell each tile to draw itself at its current pixel position."""
        for tile in tiles:
            tile.draw(self._screen)

    def _draw_overlay(self, headline: str, sub: str):
        """Semi-transparent overlay with centred message."""
        # Dark semi-transparent surface
        overlay = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA
        )
        overlay.fill(COLOR_OVERLAY)
        self._screen.blit(overlay, (0, 0))

        # Headline
        h_surf = self._font_msg.render(headline, True, (255, 255, 255))
        hx = (WINDOW_WIDTH - h_surf.get_width())  // 2
        hy = (WINDOW_HEIGHT - h_surf.get_height()) // 2 - 20
        self._screen.blit(h_surf, (hx, hy))

        # Sub-text
        s_surf = self._font_ui.render(sub, True, (220, 220, 220))
        sx = (WINDOW_WIDTH  - s_surf.get_width())  // 2
        sy = hy + h_surf.get_height() + 10
        self._screen.blit(s_surf, (sx, sy))
