# ============================================================
#  game.py
#
#  OOP concept demonstrated: COMPOSITION & STATE MACHINE
#  Game is composed of smaller objects (Board, Renderer,
#  InputHandler) and delegates each responsibility to them.
#  It also acts as a simple state machine:
#      playing  →  won  or  game_over
#                  ↓             ↓
#              (press R) →  playing
# ============================================================

import pygame
from board         import Board
from renderer      import Renderer
from input_handler import InputHandler
from constants     import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FPS, SLIDE_SPEED


class Game:
    """Top-level game object.  Creates the window and runs the main loop.

    Attributes (private)
    --------------------
    _board   : Board          Game logic & tile data.
    _renderer: Renderer       Draws everything on screen.
    _input   : InputHandler   Maps keys → actions.
    _state   : str            'playing' | 'won' | 'game_over'
    _best    : int            Best score across resets (session only).
    """

    def __init__(self):
        pygame.init()
        self._screen   = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self._clock    = pygame.time.Clock()

        # Compose the game from its parts
        self._board    = Board()
        self._renderer = Renderer(self._screen)
        self._input    = InputHandler()

        self._state    = "playing"
        self._best     = 0
        self._animating = False   # True while tiles are sliding

    # ── Public entry point ─────────────────────────────────

    def run(self):
        """Start and run the game loop until the player quits."""
        running = True
        while running:
            action = self._input.get_action()

            if action == "quit":
                running = False

            elif action == "restart":
                self._restart()

            elif action in ("up", "down", "left", "right"):
                self._handle_move(action)

            # Animate tiles sliding toward their targets every frame
            self._update_animation()

            # Draw
            self._renderer.draw(
                self._board,
                self._board.score,
                self._best,
                self._state,
            )

            self._clock.tick(FPS)

        pygame.quit()

    # ── Private helpers ────────────────────────────────────

    def _handle_move(self, direction: str):
        """Apply a move if the game is live and animation has finished."""
        if self._state != "playing" or self._animating:
            return

        moved = self._board.move(direction)
        if moved:
            self._animating = True
            self._update_best_score()
            self._check_state()

    def _update_animation(self):
        """Step every tile closer to its target; clear flag when done."""
        if not self._animating:
            return

        all_settled = True
        for tile in self._board.tiles:
            tile.move_towards_target(SLIDE_SPEED)
            if not tile.is_at_target():
                all_settled = False

        if all_settled:
            self._animating = False

    def _check_state(self):
        """Transition to 'won' or 'game_over' if conditions are met."""
        if self._board.is_won():
            self._state = "won"
        elif self._board.is_game_over():
            self._state = "game_over"

    def _update_best_score(self):
        if self._board.score > self._best:
            self._best = self._board.score

    def _restart(self):
        self._board.reset()
        self._state     = "playing"
        self._animating = False
