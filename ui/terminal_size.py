# ui/terminal_size.py
import os

def get_terminal_size() -> tuple[int, int]:
    """Rückgabe (width, height) – funktioniert unter Unix und Windows."""
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except OSError:                     # z. B. wenn kein echtes TTY
        return 80, 24                    # Fallback‑Werte
