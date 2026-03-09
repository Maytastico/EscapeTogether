# ui/resize_watcher.py
import signal
from .terminal_size import get_terminal_size
from typing import Callable

class ResizeWatcher:
    def __init__(self, callback: Callable[[int, int], None]):
        self._callback = callback
        signal.signal(signal.SIGWINCH, self._handle)

    def _handle(self, signum, frame):
        w, h = get_terminal_size()
        self._callback(w, h)
