# ============================================================
#  test_tile_rendering.py
#
#  Standalone test — no pygame window needed.
#  Checks that every tile's .row/.col matches where it
#  actually sits in board._grid after each move direction.
# ============================================================
import os, sys
os.environ["SDL_VIDEODRIVER"] = "dummy"   # headless pygame
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1, 1))           # required before font/surface use

sys.path.insert(0, os.path.dirname(__file__))

from constants import GRID_SIZE, GRID_OFFSET_X, GRID_OFFSET_Y, GRID_PADDING, TILE_SIZE
from tile  import Tile
from board import Board


# ── Helpers ────────────────────────────────────────────────

def expected_pixel(row, col):
    x = GRID_OFFSET_X + GRID_PADDING + col * (TILE_SIZE + GRID_PADDING)
    y = GRID_OFFSET_Y + GRID_PADDING + row * (TILE_SIZE + GRID_PADDING)
    return float(x), float(y)


def grid_snapshot(board):
    """Return dict {(r,c): tile_value} for every occupied cell."""
    snap = {}
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            t = board._grid[r][c]
            if t is not None:
                snap[(r, c)] = t.value
    return snap


def check_consistency(board, label=""):
    """
    For every tile object, assert:
      1. tile.row / tile.col matches where it lives in _grid
      2. tile.target_x / target_y matches expected_pixel(row, col)

    Returns list of error strings (empty = all good).
    """
    errors = []

    # Build reverse map: tile_id → (grid_row, grid_col)
    grid_pos = {}
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            t = board._grid[r][c]
            if t is not None:
                grid_pos[id(t)] = (r, c)

    for tile in board.tiles:
        actual_r, actual_c = grid_pos.get(id(tile), (None, None))

        # --- Check 1: tile.row / tile.col vs grid position ---
        if tile.row != actual_r or tile.col != actual_c:
            errors.append(
                f"[{label}] Tile(value={tile.value}) "
                f"has .row={tile.row}, .col={tile.col} "
                f"but lives at grid[{actual_r}][{actual_c}]"
            )

        # --- Check 2: target pixel vs expected pixel ---
        exp_x, exp_y = expected_pixel(tile.row, tile.col)
        if tile.target_x != exp_x or tile.target_y != exp_y:
            errors.append(
                f"[{label}] Tile(value={tile.value}) at ({tile.row},{tile.col}): "
                f"target_pixel=({tile.target_x},{tile.target_y}) "
                f"expected=({exp_x},{exp_y})"
            )

    return errors


def print_grid(board, title=""):
    print(f"\n  {title}")
    for r in range(GRID_SIZE):
        row_str = ""
        for c in range(GRID_SIZE):
            t = board._grid[r][c]
            row_str += f"{t.value:5}" if t else "    ."
        print(" ", row_str)


def make_deterministic_board():
    """
    Create a board with a fixed, known layout so we can reason about
    exactly what should happen after each move.

    Layout (values):
        2  0  0  0
        0  4  0  0
        0  0  8  0
        0  0  0 16
    """
    board = Board.__new__(Board)         # skip __init__ (no random spawns)
    board._score = 0
    board._grid  = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

    placements = [(0,0,2), (1,1,4), (2,2,8), (3,3,16)]
    for r, c, v in placements:
        board._grid[r][c] = Tile(v, r, c)

    return board


# ── Tests ──────────────────────────────────────────────────

def run_tests():
    all_errors = []
    total_checks = 0

    directions = ["left", "right", "up", "down"]

    for direction in directions:
        board = make_deterministic_board()

        print_grid(board, f"BEFORE move('{direction}')")
        board.move(direction)
        print_grid(board, f"AFTER  move('{direction}')")

        errors = check_consistency(board, label=f"after move('{direction}')")
        total_checks += len(board.tiles)

        if errors:
            all_errors.extend(errors)
            for e in errors:
                print(f"  ❌ {e}")
        else:
            print(f"  ✅ All tile positions consistent after move('{direction}')")

    # ── Also test chained moves ──────────────────────────────
    board = make_deterministic_board()
    for d in ["left", "up", "right", "down"]:
        board.move(d)
        errors = check_consistency(board, label=f"chained after '{d}'")
        if errors:
            all_errors.extend(errors)
            for e in errors:
                print(f"  ❌ {e}")

    if not all_errors:
        print(f"\n✅  All {total_checks}+ tile position checks passed.\n")
    else:
        print(f"\n❌  {len(all_errors)} error(s) found:\n")
        for e in all_errors:
            print(f"   • {e}")

    return len(all_errors) == 0


if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
