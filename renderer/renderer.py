from typing import List, Tuple
from renderer.ansi_colors import *

Cell = Tuple[str, str, str] # (char, fg_code, bg_code)

EMPTY_CELL: Cell = (" ",  FG_WHITE,  BG_BLACK)

class TerminalRenderer:

    def __init__(self, width: int, height:int):
        self.width = width
        self.height = height

        self._prev: List[List[Cell]]
        self._curr: List[List[Cell]]

        self._prev = self._make_empty_buffer()
        self._curr = self._make_empty_buffer()

    def _make_empty_buffer(self) -> List[List["Cell"]]:
        return [[EMPTY_CELL for _ in range(self.width)] for _ in range(self.height)]
    
    def clear_terminal(self) -> None:
        print("\x1b[2J\x1b[H", end="", flush=True)
    
    def clear(self):
        empty = (" ", "37", "40")
        for y in range(self.height):
            self._curr[y] = [empty for _ in range(self.width)]

    def draw_text(self, 
                  x: int, 
                  y: int, 
                  text: str,
                  fg: str =  FG_WHITE,
                  bg: str =  BG_BLACK):
        for i, ch in enumerate(text):
            cx = x + i
            if 0 <= cx < self.width and 0 <= y < self.height:
                self._curr[y][cx] = (ch, fg, bg)

    def move_curser(self, row: int, col: int):
        return f"\x1b[{row};{col}H"

    def render(self):
        out = []
        cursor_move = "\x1b[{row};{col}H"   # 1‑basiert

        for y in range(self.height):
            row_prev = self._prev[y]
            row_curr = self._curr[y]

            col = 0
            while col < self.width:
                if row_prev[col] != row_curr[col]:
                    # Beginn einer veränderten Sequenz finden
                    start = col
                    # Sammle zusammenhängende gleiche Zellen, um die Escape‑Sequenz nur einmal zu senden
                    while (col < self.width and
                           row_prev[col] != row_curr[col]):
                        col += 1
                    segment = row_curr[start:col]

                    # Cursor an den Start setzen
                    out.append(cursor_move.format(row=y+1, col=start+1))

                    # Baue die ANSI‑Sequenz für das Segment
                    seq = ""
                    for ch, fg, bg in segment:
                        seq += f"\x1b[{fg};{bg}m{ch}"
                    seq += "\x1b[0m"          # Reset am Ende des Segments
                    out.append(seq)
                else:
                    col += 1

        # Alles auf einmal ausgeben (weniger System‑Calls)
        if out:
            print("".join(out), end="", flush=True)

        # Nach dem Rendern wird der aktuelle Buffer zum vorherigen
        self._swap_buffers()

    def _swap_buffers(self):
        self._prev, self._curr = self._curr, self._prev
        # _curr wird wieder als leeres Arbeits‑Buffer benutzt
        self._curr = self._make_empty_buffer()


