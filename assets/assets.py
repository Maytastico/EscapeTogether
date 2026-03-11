# ------------------------------------------------------------
# cellmaps.py
# ------------------------------------------------------------
"""
Zentrale Sammlung von CellMaps (List[List[Cell]]) für das
EscapeTogether‑Projekt.  Jede Map besteht aus Tupeln:

    Cell = Tuple[str, str, str]   # (Zeichen, FG‑Farbe, BG‑Farbe)

Die Farb‑Konstanten werden aus ``renderer.ansi_colors`` importiert.
Alle Maps können direkt mit ``renderer.drawCellMap(x, y, <MAP>)``
verwendet werden.
"""

from typing import List, Tuple
from renderer.ansi_colors import *

# ------------------------------------------------------------------
# Typ‑Alias
# ------------------------------------------------------------------
Cell = Tuple[str, str, str] # char, fg_code, bg_code

# ------------------------------------------------------------------
# Items (einzelne 1×1‑Kacheln)
# ------------------------------------------------------------------
EMPTY_CELL: Cell = (" ", FG_WHITE, BG_BLACK)
KEYCARD: List[List[Cell]] = [[("🔑", FG_WHITE, BG_BLUE)]]
CROWBAR: List[List[Cell]] = [[("🔧", FG_WHITE, BG_BLACK)]]
IRON_ARMOR: List[List[Cell]] = [[("🛡️", FG_WHITE, BG_RED)]]
NOTEBOOK: List[List[Cell]] = [[("📓", FG_WHITE, BG_GREEN)]]
PILL: List[List[Cell]] = [[("💊", FG_WHITE, BG_RED)]]
PAN: List[List[Cell]] = [[("🍳", FG_WHITE, BG_YELLOW)]]
SWORD: List[List[Cell]] = [[("⚔️", FG_WHITE, BG_BLACK)]]

# Backbag – 2×2, um eine Tasche zu visualisieren
BACKBAG: List[List[Cell]] = [
    [("👜", FG_WHITE, BG_BLACK), ("👜", FG_WHITE, BG_BLACK)],
    [("👜", FG_WHITE, BG_BLACK), ("👜", FG_WHITE, BG_BLACK)],
]

# ------------------------------------------------------------------
# Interactables (Umgebungsobjekte)
# ------------------------------------------------------------------
# Bett – 3×2
BED: List[List[Cell]] = [
    [("🛏️", FG_WHITE, BG_BLUE), ("🛏️", FG_WHITE, BG_BLUE), ("🛏️", FG_WHITE, BG_BLUE)],
    [("🛏️", FG_WHITE, BG_BLUE), ("🛏️", FG_WHITE, BG_BLUE), ("🛏️", FG_WHITE, BG_BLUE)],
]

# Sofa – 3×2
COUCH: List[List[Cell]] = [
    [("🛋️", FG_WHITE, BG_GREEN), ("🛋️", FG_WHITE, BG_GREEN), ("🛋️", FG_WHITE, BG_GREEN)],
    [("🛋️", FG_WHITE, BG_GREEN), ("🛋️", FG_WHITE, BG_GREEN), ("🛋️", FG_WHITE, BG_GREEN)],
]

# Kühlschrank – 2×3
FRIDGE: List[List[Cell]] = [
    [("🧊", FG_WHITE, BG_BLUE), ("🧊", FG_WHITE, BG_BLUE)],
    [("🧊", FG_WHITE, BG_BLUE), ("🧊", FG_WHITE, BG_BLUE)],
    [("🧊", FG_WHITE, BG_BLUE), ("🧊", FG_WHITE, BG_BLUE)],
]

# Schrank – 2×2
CABINET: List[List[Cell]] = [
    [("🗄️", FG_WHITE, BG_RED), ("🗄️", FG_WHITE, BG_RED)],
    [("🗄️", FG_WHITE, BG_RED), ("🗄️", FG_WHITE, BG_RED)],
]

# Fernseher – 2×2
TV: List[List[Cell]] = [
    [("📺", FG_WHITE, BG_BLACK), ("📺", FG_WHITE, BG_BLACK)],
    [("📺", FG_WHITE, BG_BLACK), ("📺", FG_WHITE, BG_BLACK)],
]

# Radio – 1×2 (vertikal)
RADIO: List[List[Cell]] = [
    [("📻", FG_WHITE, BG_BLACK)],
    [("📻", FG_WHITE, BG_BLACK)],
]

# Herd – 2×2
STOVE: List[List[Cell]] = [
    [("🔥", FG_WHITE, BG_RED), ("🔥", FG_WHITE, BG_RED)],
    [("🔥", FG_WHITE, BG_RED), ("🔥", FG_WHITE, BG_RED)],
]

# Tisch – 2×2
TABLE: List[List[Cell]] = [
    [("🪑", FG_WHITE, BG_GREEN), ("🪑", FG_WHITE, BG_GREEN)],
    [("🪑", FG_WHITE, BG_GREEN), ("🪑", FG_WHITE, BG_GREEN)],
]

# Whiteboard – 3×1 (horizontal)
WHITEBOARD: List[List[Cell]] = [
    [("📝", FG_WHITE, BG_BLACK), ("📝", FG_WHITE, BG_BLACK), ("📝", FG_WHITE, BG_BLACK)],
]

# Terminal – 1×3 (vertikal)
TERMINAL: List[List[Cell]] = [
    [(">", FG_WHITE, BG_BLACK)],
    [(">", FG_WHITE, BG_BLACK)],
    [(">", FG_WHITE, BG_BLACK)],
]

# ------------------------------------------------------------------
# Beispiel‑Map für ein kleines Zimmer (optional)
# ------------------------------------------------------------------
# 6 × 4‑Raster, das die oben definierten Farben nutzt (ohne Emojis)
BASIC_ROOM: List[List[Cell]] = [
    [("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_RED),   ("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_GREEN), ("0", FG_BLUE, BG_GREEN)],
]
