# ============================================================
#  game.py
#
#  OOP concept demonstrated: COMPOSITION & STATE MACHINE
#  Game is composed of smaller objects (Board, Renderer,
#  InputHandler) and delegates each responsibility to them.
#  It also acts as a simple state machine:
#      playing  -->  won  or  game_over
#                    |             |
#               (press R)  -->  playing
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
    _board      : Board          Game logic & tile data.
    _renderer   : Renderer       Draws everything on screen.
    _input      : InputHandler   Maps keys -> actions.
    _state      : str            'playing' | 'won' | 'game_over'
    _best       : int            Best score across resets (session only).
    _animating  : bool           True while tiles are still sliding.
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

        self._state     = "playing"
        self._best      = 0
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

            # Draw the current frame
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
        """Apply a move only if the game is live and no animation is running.

        Steps:
          1. Guard: do nothing if self._state != 'playing' or self._animating is True.
          2. Call self._board.move(direction) and store the result in 'moved'.
          3. If moved is True:
               - Set self._animating = True  (tiles need to slide to new positions)
               - Call self._update_best_score()
               - Call self._check_state()    (did the player win or lose?)
        """
        # TODO: implement this method
        self._board.move(direction)
        print(direction)
        pass

    def _update_animation(self):
        """Step every tile closer to its target; clear the flag when all tiles arrive.

        Steps:
          1. If self._animating is False, return immediately (nothing to do).
          2. Assume all_settled = True.
          3. For each tile in self._board.tiles:
               - Call tile.move_towards_target(SLIDE_SPEED)
               - If tile.is_at_target() is False, set all_settled = False
          4. If all_settled is True, set self._animating = False.
        """
        # TODO: implement this method
        if not self._animating:
            return False
        for tile in self._board.tiles:
            tile.move_towards_target(SLIDE_SPEED)
            
        pass

    def _check_state(self):
        """Transition _state to 'won' or 'game_over' when conditions are met.

        HINT: Ask self._board whether the game is won or over.
        Priority: check is_won() first, then is_game_over().
        """
        # TODO: implement this method
        pass

    def _update_best_score(self):
        """Update self._best if the current score exceeds it.

        HINT: Compare self._board.score with self._best.
        """
        # TODO: implement this method
        pass

    def _restart(self):
        """Reset the board and return to the 'playing' state.

        HINT: Call self._board.reset(), reset self._state and self._animating.
        """
        # TODO: implement this method
        pass