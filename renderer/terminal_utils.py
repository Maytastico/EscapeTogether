# renderer/terminal_utils.py
import os
import sys

def clear_terminal() -> None:
    """
    Löscht den gesamten Bildschirminhalt und setzt den Cursor
    nach links oben (Zeile 1, Spalte 1) – ohne re‑entranten
    `print`‑Aufruf.
    """
    # ANSI‑Escape‑Sequenz: 2J = clear screen, H = cursor home
    seq = b"\x1b[2J\x1b[H"
    # Schreiben Sie direkt auf den Dateideskriptor von stdout
    os.write(sys.stdout.fileno(), seq)
    # Optional: sofortiges Flush, falls stdout gepuffert ist
    sys.stdout.flush()
