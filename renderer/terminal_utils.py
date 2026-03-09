# renderer/terminal_utils.py
"""
Hilfsfunktionen für den Terminal‑Renderer.
Nur ANSI‑Escapes – funktioniert auf Linux, macOS und Windows 10+.
"""

def clear_terminal() -> None:
    """
    Löscht den gesamten Bildschirminhalt und setzt den Cursor
    nach links oben (Zeile 1, Spalte 1).
    """
    # 2J  → clear screen, H → cursor home
    print("\x1b[2J\x1b[H", end="", flush=True)
