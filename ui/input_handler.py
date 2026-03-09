# ui/input_handler.py
import sys
import threading
import queue
from .key_event import Key, KeyEvent

# ----------------------------------------------------------------------
# Linux / macOS – termios + tty
# ----------------------------------------------------------------------
if sys.platform != "win32":
    import tty
    import termios
    import select

    class _UnixReader(threading.Thread):
        def __init__(self, q: queue.Queue):
            super().__init__(daemon=True)
            self.q = q
            self.fd = sys.stdin.fileno()
            self.old_settings = termios.tcgetattr(self.fd)

        def run(self):
            try:
                tty.setcbreak(self.fd)          # raw‑ähnlich, kein Enter nötig
                while True:
                    # select mit Timeout, damit Thread sauber beendet werden kann
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        ch = sys.stdin.read(1)
                        self.q.put(self._translate(ch))
            finally:
                termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

        def _translate(self, ch: str) -> KeyEvent:
            # Escape‑Sequenzen für Pfeiltasten
            if ch == "\x1b":
                nxt = sys.stdin.read(2)          # z. B. "[A"
                seq = ch + nxt
                mapping = {
                    "\x1b[A": Key.UP,
                    "\x1b[B": Key.DOWN,
                    "\x1b[C": Key.RIGHT,
                    "\x1b[D": Key.LEFT,
                }
                return KeyEvent(mapping.get(seq, Key.ESC))
            if ch == "\r" or ch == "\n":
                return KeyEvent(Key.ENTER)
            if ch == "\x7f":
                return KeyEvent(Key.BACKSPACE)
            if ch == "\x03":                     # Ctrl‑C
                raise KeyboardInterrupt
            # alles andere als normales Zeichen
            return KeyEvent(Key.CHAR, char=ch)

# ----------------------------------------------------------------------
# Windows – msvcrt
# ----------------------------------------------------------------------
else:
    import msvcrt

    class _WindowsReader(threading.Thread):
        def __init__(self, q: queue.Queue):
            super().__init__(daemon=True)
            self.q = q

        def run(self):
            while True:
                if msvcrt.kbhit():
                    ch = msvcrt.getwch()
                    self.q.put(self._translate(ch))

        def _translate(self, ch: str) -> KeyEvent:
            # Pfeiltasten kommen als zwei Zeichen: 0x00/0xE0 gefolgt von Code
            if ch in ("\x00", "\xe0"):
                code = msvcrt.getwch()
                mapping = {
                    "H": Key.UP,
                    "P": Key.DOWN,
                    "K": Key.LEFT,
                    "M": Key.RIGHT,
                }
                return KeyEvent(mapping.get(code, Key.ESC))
            if ch == "\r":
                return KeyEvent(Key.ENTER)
            if ch == "\x08":
                return KeyEvent(Key.BACKSPACE)
            if ch == "\x03":                     # Ctrl‑C
                raise KeyboardInterrupt
            return KeyEvent(Key.CHAR, char=ch)

# ----------------------------------------------------------------------
# Öffentliche API
# ----------------------------------------------------------------------
class InputHandler:
    """
    Nicht‑blockierender Input‑Handler.
    Aufruf:  event = handler.get_key()   (None, wenn nichts gedrückt)
    """
    def __init__(self):
        self._queue = queue.Queue()
        self._reader = (_UnixReader(self._queue) if sys.platform != "win32"
                        else _WindowsReader(self._queue))
        self._reader.start()

    def get_key(self) -> KeyEvent | None:
        """
        Gibt das nächste KeyEvent zurück oder None, wenn keine Eingabe vorliegt.
        """
        try:
            return self._queue.get_nowait()
        except queue.Empty:
            return None
