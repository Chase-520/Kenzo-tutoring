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
    """Manages the 4x4 grid of Tile objects and all game logic.

    Public interface
    ----------------
    move(direction)  -> bool   Slide tiles; returns True if anything moved.
    is_game_over()   -> bool
    is_won()         -> bool
    reset()                    Start a brand-new game.
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
        """Slide all tiles in direction ('up','down','left','right').

        Strategy: rotate the grid so the target direction becomes 'left',
        run _slide_left(), then rotate back.

        Returns True if at least one tile moved or merged.
        """
        rotations = {"left": 0, "up": 1, "right": 2, "down": 3}
        n_rot = rotations[direction]

        self._rotate(n_rot)
        moved = self._slide_left()
        self._rotate(4 - n_rot)   # rotate back to original orientation

        if moved:
            self._spawn_tile()
        return moved

    def is_won(self) -> bool:
        """Return True if any tile on the board has reached WIN_VALUE (2048).

        HINT: Loop through self.tiles and check each tile's .value attribute.
        """
        # TODO: implement this method
        # Placeholder returns False so the game keeps running
        return False

    def is_game_over(self) -> bool:
        """Return True if no moves are possible.

        The game is over when:
          1. There are NO empty cells (None) in the grid, AND
          2. No two adjacent tiles (horizontally or vertically) have the same value.

        HINT: Check empty cells first — if any exist, return False immediately.
        Then loop through all cells and compare each tile with its right neighbour
        and its bottom neighbour.
        """
        # TODO: implement this method
        # Placeholder returns False so the game never ends prematurely
        return False

    # ── Private helpers ────────────────────────────────────

    def _reset_grid(self):
        self._grid = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

    def _spawn_tile(self):
        """Place a new 2 (90%) or 4 (10%) tile in a random empty cell."""
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

    # ── Slide algorithm (always slides LEFT) ───────────────

    def _slide_left(self) -> bool:
        """Compress and merge every row toward the left.

        For each row:
          1. Call _compress_row() to get the new arrangement of tiles.
          2. Update each tile's .row and .col to match its new position.
          3. Update self._grid with the new layout.

        Returns True if any row changed.

        HINT: After _compress_row() returns new_row, loop over the columns
        and for each non-None tile set tile.row = r, tile.col = c.
        """
        # TODO: implement this method
        # Placeholder does nothing — tiles won't move yet

        # print before
        print("Before")
        self._debug_grid()

        for index,i in enumerate(self._grid):
            self._compress_row(i)
            r,valid = self._compress_row(i)
            self._grid[index] = r
            
        # after compressing
        self._update_tile_xy()
        print("After")
        self._debug_grid()
        return False

    def _debug_grid(self):
        for row in self._grid:
            print(row)

    def _update_tile_xy(self):
        for r,row in enumerate(self._grid):
            for c,tile in enumerate(row):
                if tile is not None:
                    tile.col = c
                    tile.row = r

    def _compress_row(self, row: list) -> tuple:
        """Slide all tiles in one row to the left and merge equal neighbours.

        Rules:
          - Remove all gaps (None values), pack tiles to the left.
          - Scan left to right: if two adjacent tiles have the same value,
            merge them (double the left tile's value, discard the right tile).
            A tile that was just merged cannot merge again this turn.
          - Fill the rest of the row with None.
          - Add the merged tile's new value to self._score.

        Returns (new_row, changed) where:
          new_row : list of length GRID_SIZE with tiles packed left + None padding
          changed : bool, True if anything moved or merged

        HINT: Use a 'skip' boolean flag to prevent a tile from merging twice.
        Compare tiles[i].value == tiles[i+1].value to detect a merge.
        """

        new_list = [None, None, None, None]
        new_index = 0
        for tile in row:
            if tile is not None:
                pass
                new_list[new_index] = tile
                new_index += 1
        # TODO: implement this method
        # Placeholder returns the row unchanged so the game is still runnable
        row = new_list
        return row[:], False

    # ── Grid rotation helpers ──────────────────────────────

    def _rotate(self, times: int):
        """Rotate the grid 90 degrees counter-clockwise, 'times' times.

        Also update each tile's .row and .col to match its new grid position.

        The counter-clockwise rotation formula for one step is:
            new_row = (GRID_SIZE - 1) - col
            new_col = row

        HINT: Build a new empty grid, then for each (r, c) in self._grid,
        compute (new_r, new_c), update tile.row and tile.col, and place
        the tile in new[new_r][new_c]. Then replace self._grid with new.
        """
        # TODO: implement this method
        # Placeholder does nothing — move() will not work correctly without this
        for i in range(times):
            new_grid = []
            for c in range(len(self._grid[0])):
                col = []
                for r in range(len(self._grid)):
                    col.append(self._grid[r][c])
                new_grid.insert(0,col)
            
            self._debug_grid()
            print("$####################")
            for r in new_grid:
                print(r)
            
            self._grid = new_grid
            
        self._update_tile_xy()
           
                
        pass
