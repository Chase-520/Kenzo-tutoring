# ============================================================
#  constants.py
#  All magic numbers and colours live here — one place to
#  change them and the whole game updates.
# ============================================================

# Window
WINDOW_TITLE  = "2048"
WINDOW_WIDTH  = 480
WINDOW_HEIGHT = 580          # extra height for the score bar

# Grid
GRID_SIZE     = 4            # 4×4 board
GRID_PADDING  = 12           # gap between tiles (px)
GRID_OFFSET_X = 20           # left margin of the grid
GRID_OFFSET_Y = 120          # top  margin of the grid (below score bar)

# Derived tile size so the grid exactly fits the window
TILE_SIZE = (
    WINDOW_WIDTH
    - 2 * GRID_OFFSET_X
    - (GRID_SIZE + 1) * GRID_PADDING
) // GRID_SIZE

# Frames per second
FPS = 60

# ── Colours ─────────────────────────────────────────────────
# General UI
COLOR_BG          = (250, 248, 239)
COLOR_GRID_BG     = (187, 173, 160)
COLOR_EMPTY_CELL  = (205, 193, 180)

COLOR_TEXT_DARK   = ( 47,  43,  46)   # used on light tiles
COLOR_TEXT_LIGHT  = (249, 246, 242)   # used on dark  tiles

COLOR_TITLE       = (119, 110, 101)
COLOR_SCORE_BG    = (187, 173, 160)
COLOR_SCORE_TEXT  = (249, 246, 242)

COLOR_OVERLAY     = (  0,   0,   0, 160)   # semi-transparent game-over

# Tile background colours keyed by tile value
TILE_COLORS = {
    0    : (205, 193, 180),
    2    : (238, 228, 218),
    4    : (237, 224, 200),
    8    : (242, 177, 121),
    16   : (245, 149,  99),
    32   : (246, 124,  95),
    64   : (246,  94,  59),
    128  : (237, 207, 114),
    256  : (237, 204,  97),
    512  : (237, 200,  80),
    1024 : (237, 197,  63),
    2048 : (237, 194,  46),
}
TILE_COLOR_DEFAULT = (60, 58, 50)      # for values > 2048

# Tile font sizes
FONT_TILE_LARGE  = 44   # 1–3 digit values
FONT_TILE_MEDIUM = 34   # 4-digit values
FONT_TILE_SMALL  = 26   # 5-digit values
FONT_UI          = 28
FONT_TITLE       = 52
FONT_MSG         = 40

# Animation
SLIDE_SPEED = 18    # pixels per frame during slide animation
