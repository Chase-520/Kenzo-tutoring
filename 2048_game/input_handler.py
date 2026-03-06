# ============================================================
#  input_handler.py
#
#  OOP concept demonstrated: SEPARATION OF CONCERNS
#  InputHandler translates raw pygame events into simple,
#  game-meaningful strings ("up", "restart", "quit").
#  The Game class never touches pygame.KEYDOWN directly.
# ============================================================

from typing import Optional
import pygame


class InputHandler:
    """Converts pygame keyboard events into game actions.

    Usage
    -----
    handler = InputHandler()
    action = handler.get_action()   # call once per frame
    # action is one of: 'up' 'down' 'left' 'right' 'restart' 'quit' None
    """

    # Maps every supported key to its game action
    _KEY_MAP: dict[int, str] = {
        # Arrow keys
        pygame.K_UP    : "up",
        pygame.K_DOWN  : "down",
        pygame.K_LEFT  : "left",
        pygame.K_RIGHT : "right",
        # WASD
        pygame.K_w     : "up",
        pygame.K_s     : "down",
        pygame.K_a     : "left",
        pygame.K_d     : "right",
        # Control
        pygame.K_r     : "restart",
        pygame.K_ESCAPE: "quit",
    }

    def get_action(self) -> Optional[str]:
        """Process the pygame event queue and return one action (or None).

        Only the first relevant key in the queue is returned; the rest
        are processed next frame.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                action = self._KEY_MAP.get(event.key)
                if action:
                    return action
        return None
