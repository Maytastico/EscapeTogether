from enum import Enum, auto
from dataclasses import dataclass

class Key(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    ENTER = auto()
    ESC = auto()
    BACKSPACE = auto()
    CHAR = auto()          # normale Zeichen (a‑z, 0‑9, …)

@dataclass
class KeyEvent:
    key: Key
    char: str = "" 