# ============================================================
#  board.py
#
#  OOP concept demonstrated: ABSTRACTION
#  The Board hides all the complexity of sliding, merging,
#  and spawning tiles behind a clean public interface.
#  The rest of the code just calls  board.move("left")  and
#  never needs to know how that works internally.
# ============================================================

import random
from typing import Optional
from tile import Tile
from constants import GRID_SIZE


class Board:
    """Manages the 4×4 grid of Tile objects and all game logic.

    Public interface
    ----------------
    move(direction)  → bool   Slide tiles; returns True if anything moved.
    is_game_over()   → bool
    is_won()         → bool
    reset()                   Start a brand-new game.
    tiles            property: flat list of all non-empty Tile objects.
    score            property: current score.
    """

    WIN_VALUE = 2048

    def __init__(self):
        # _grid[row][col] holds a Tile or None
        self._grid: list[list[Optional[Tile]]] = []
        self._score  = 0
        self._reset_grid()
        self._spawn_tile()
        self._spawn_tile()

    # ── Public properties ──────────────────────────────────

    @property
    def score(self) -> int:
        return self._score

    @property
    def tiles(self) -> list[Tile]:
        """All live Tile objects (non-empty cells)."""
        return [
            self._grid[r][c]
            for r in range(GRID_SIZE)
            for c in range(GRID_SIZE)
            if self._grid[r][c] is not None
        ]

    # ── Public methods ─────────────────────────────────────

    def reset(self):
        """Restart the game from scratch."""
        self._score = 0
        self._reset_grid()
        self._spawn_tile()
        self._spawn_tile()

    def move(self, direction: str) -> bool:
        """Slide all tiles in *direction* ('up','down','left','right').

        Returns True if at least one tile moved or merged.
        """
        # Rotate the grid so we only need one sliding algorithm (left).
        rotations = {"left": 0, "up": 1, "right": 2, "down": 3}
        n_rot = rotations[direction]

        self._rotate(n_rot)
        moved = self._slide_left()
        self._rotate(4 - n_rot)          # rotate back

        if moved:
            self._spawn_tile()
        return moved

    def is_won(self) -> bool:
        for tile in self.tiles:
            if tile.value == self.WIN_VALUE:
                return True
        return False

    def is_game_over(self) -> bool:
        # Any empty cell → still moves available
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if self._grid[r][c] is None:
                    return False
        # Any adjacent pair with equal values → can still merge
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                val = self._grid[r][c].value
                if c + 1 < GRID_SIZE and self._grid[r][c + 1].value == val:
                    return False
                if r + 1 < GRID_SIZE and self._grid[r + 1][c].value == val:
                    return False
        return True

    # ── Private helpers ────────────────────────────────────

    def _reset_grid(self):
        self._grid = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

    def _spawn_tile(self):
        """Place a new 2 (90 %) or 4 (10 %) in a random empty cell."""
        empty = [
            (r, c)
            for r in range(GRID_SIZE)
            for c in range(GRID_SIZE)
            if self._grid[r][c] is None
        ]
        if not empty:
            return
        r, c = random.choice(empty)
        value = 4 if random.random() < 0.1 else 2
        self._grid[r][c] = Tile(value, r, c)

    # ── Slide algorithm (always slides LEFT) ──────────────

    def _slide_left(self) -> bool:
        """Compress and merge every row to the left.  Returns True if changed."""
        moved = False
        for r in range(GRID_SIZE):
            new_row, did_change = self._compress_row(
                [self._grid[r][c] for c in range(GRID_SIZE)]
            )
            if did_change:
                moved = True
            for c in range(GRID_SIZE):
                tile = new_row[c]
                if tile is not None:
                    tile.row = r
                    tile.col = c
                self._grid[r][c] = tile
        return moved

    def _compress_row(
        self, row: list
    ) -> tuple:
        """Slide non-None tiles left, merge equal neighbours.

        Returns (new_row, changed_flag).
        """
        # 1. Remove gaps
        tiles   = [t for t in row if t is not None]
        changed = len(tiles) != sum(1 for t in row if t is not None) or (
            [t for t in row if t is not None] != tiles
        )

        # 2. Merge adjacent equal tiles
        merged: list = []
        skip = False
        for i in range(len(tiles)):
            if skip:
                skip = False
                continue
            if i + 1 < len(tiles) and tiles[i].value == tiles[i + 1].value:
                # Merge: double the left tile, discard the right
                tiles[i].value *= 2
                self._score += tiles[i].value
                merged.append(tiles[i])
                skip    = True
                changed = True
            else:
                merged.append(tiles[i])

        # 3. Pad with None
        while len(merged) < GRID_SIZE:
            merged.append(None)

        # 4. Detect positional change
        for orig, new in zip(row, merged):
            if orig is not new:
                changed = True
                break

        return merged, changed

    # ── Grid rotation helpers ──────────────────────────────

    def _rotate(self, times: int):
        """Rotate the grid 90 degrees counter-clockwise *times* times.
        Also updates each tile's .row/.col to match its new grid position.
        """
        for _ in range(times % 4):
            n    = GRID_SIZE
            new  = [[None] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    tile = self._grid[r][c]
                    if tile is not None:
                        new_r, new_c = n - 1 - c, r
                        tile.row = new_r
                        tile.col = new_c
                        new[new_r][new_c] = tile
            self._grid = new
