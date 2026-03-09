

# ansi_colors.py
# -------------------------------------------------
# Grundfarben (0‑7) – 8‑Bit‑Codes, wie in den meisten Terminals üblich
# -------------------------------------------------
FG_BLACK   = "30"
FG_RED     = "31"
FG_GREEN   = "32"
FG_YELLOW  = "33"
FG_BLUE    = "34"
FG_MAGENTA = "35"
FG_CYAN    = "36"
FG_WHITE   = "37"

BG_BLACK   = "40"
BG_RED     = "41"
BG_GREEN   = "42"
BG_YELLOW  = "43"
BG_BLUE    = "44"
BG_MAGENTA = "45"
BG_CYAN    = "46"
BG_WHITE   = "47"

# -------------------------------------------------
# 256‑Farbpalette (0‑255)
# -------------------------------------------------
def fg_256(n: int) -> str:
    """Foreground‑Farbe aus der 256‑Palette."""
    return f"38;5;{n}"

def bg_256(n: int) -> str:
    """Background‑Farbe aus der 256‑Palette."""
    return f"48;5;{n}"

# Beispiel‑Nutzung:
#   ESC = "\x1b["
#   print(f"{ESC}{fg_256(196)}mHello{ESC}[0m")   # leuchtendes Rot

# -------------------------------------------------
# True‑Color (24‑Bit) – RGB‑Werte 0‑255
# -------------------------------------------------
def fg_rgb(r: int, g: int, b: int) -> str:
    """Foreground‑Farbe als 24‑Bit‑RGB."""
    return f"38;2;{r};{g};{b}"

def bg_rgb(r: int, g: int, b: int) -> str:
    """Background‑Farbe als 24‑Bit‑RGB."""
    return f"48;2;{r};{g};{b}"

# -------------------------------------------------
# Hilfsfunktion zum Erzeugen des kompletten Escape‑Strings
# -------------------------------------------------
def esc(code: str) -> str:
    """Wraps a raw ANSI code (z. B. '31' oder '38;5;196') in ESC brackets."""
    return f"\x1b[{code}m"

# -------------------------------------------------
# Beispiel‑Konstanten für häufig genutzte 256‑Farben
# -------------------------------------------------
FG_ORANGE   = fg_256(208)   # leuchtendes Orange
FG_LIME     = fg_256(154)   # helles Grün
FG_PURPLE   = fg_256(129)   # violett
BG_ORANGE   = bg_256(208)
BG_LIME     = bg_256(154)
BG_PURPLE   = bg_256(129)

# -------------------------------------------------
# Reset‑Code (wird nach jedem farbigen Segment empfohlen)
# -------------------------------------------------
RESET = "\x1b[0m"
