# 2048 — OOP Teaching Project

## Quick start
```bash
pip install pygame
python main.py
```

## Controls
| Key | Action |
|-----|--------|
| ↑ ↓ ← → or W A S D | Slide tiles |
| R | Restart |
| Esc | Quit |

---

## Project structure

```
2048_game/
├── main.py           Entry point — just 3 lines
├── constants.py      All numbers & colours in one place
├── tile.py           Tile class
├── board.py          Board class
├── renderer.py       Renderer class
├── input_handler.py  InputHandler class
└── game.py           Game class (main orchestrator)
```

---

## OOP Concepts — one per file

### 1. `tile.py` — **Encapsulation**
A `Tile` bundles together its *data* (value, row, col, pixel x/y)
and the *behaviour* that operates on that data (draw, animate, snap).
Nothing outside the class needs to know how the drawing works.

```python
tile = Tile(value=8, row=1, col=2)
tile.draw(screen)                 # just call it — no need to know details
tile.move_towards_target(speed=18)
```

### 2. `board.py` — **Abstraction**
`Board` exposes only what callers need:

```python
board.move("left")    # slide tiles — returns True if anything changed
board.is_game_over()
board.is_won()
board.score
board.tiles           # list of all Tile objects
```

The complex rotation trick, the merge algorithm, and the spawn logic
are all **private** (`_slide_left`, `_compress_row`, `_rotate`, …).
Callers never need to see them.

### 3. `renderer.py` — **Single Responsibility Principle (SRP)**
`Renderer` does exactly one thing: draw to the screen.
It never changes game state. When game logic changes, this file
is untouched; when the visual design changes, only this file changes.

### 4. `input_handler.py` — **Separation of Concerns**
All pygame event handling is isolated here.
The rest of the game never imports `pygame.KEYDOWN`.
Changing from keyboard to gamepad input = only change this file.

### 5. `game.py` — **Composition & State Machine**
`Game` owns a `Board`, a `Renderer`, and an `InputHandler` as
instance attributes — this is **composition** ("has-a" relationship).

It also implements a simple **state machine**:

```
          move()
playing ──────────► won  ──► (R) ──► playing
        └──────────► game_over ──┘
```

### 6. `constants.py` — **DRY (Don't Repeat Yourself)**
Every magic number lives here. Change `GRID_SIZE = 5` and the game
becomes 5×5. Change `TILE_SIZE` and all tiles resize together.

---

## Discussion questions for class

1. What would break if `Board` directly modified `Tile.x` and `Tile.y`
   instead of only changing `row` and `col`?

2. Why is it useful that `Renderer.draw()` receives the board as a
   parameter instead of storing it as `self._board`?

3. Could you swap `Board` for a new `HexBoard` class without touching
   `Renderer` or `InputHandler`? Why or why not?

4. What OOP principle does `constants.py` support?
