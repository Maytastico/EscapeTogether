# renderer/renderer.py
from __future__ import annotations
from typing import List, Tuple
import renderer.ansi_colors as ansi
from .terminal_utils import clear_terminal   # die Funktion aus dem vorherigen Beitrag

Cell = Tuple[str, str, str]
EMPTY_CELL: Cell = (" ", ansi.FG_WHITE, ansi.BG_BLACK)


class TerminalRenderer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._prev: List[List[Cell]]
        self._curr: List[List[Cell]]
        self._prev = self._make_empty_buffer()
        self._curr = self._make_empty_buffer()

    # ------------------------------------------------------------------
    def _make_empty_buffer(self) -> List[List[Cell]]:
        return [[EMPTY_CELL for _ in range(self.width)]
                for _ in range(self.height)]

    # ------------------------------------------------------------------
    def clear_screen(self) -> None:
        clear_terminal()
        self._prev = self._make_empty_buffer()
        self._curr = self._make_empty_buffer()

    # ------------------------------------------------------------------
    def resize(self, width: int, height: int, clear: bool = True) -> None:
        self.width = max(1, width)
        self.height = max(1, height)
        self._prev = self._make_empty_buffer()
        self._curr = self._make_empty_buffer()
        if clear:
            clear_terminal()

    # ------------------------------------------------------------------
    def draw_text(self,
                  x: int,
                  y: int,
                  text: str,
                  fg: str = ansi.FG_WHITE,
                  bg: str = ansi.BG_BLACK) -> None:
        for i, ch in enumerate(text):
            cx = x + i
            if cx > len(self._prev) or cx > len(self._curr):
                break
            if 0 <= cx < self.width and 0 <= y < self.height:
                self._curr[y][cx] = (ch, fg, bg)

    # ------------------------------------------------------------------
    def render(self) -> None:
        # Guard – falls die Buffer‑Größen aus irgendeinem Grund nicht passen
        if (
            len(self._prev) != self.height
            or len(self._curr) != self.height
            or any(len(row) != self.width for row in self._prev)
            or any(len(row) != self.width for row in self._curr)
        ):
            self._prev = self._make_empty_buffer()
            self._curr = self._make_empty_buffer()

        out = []
        move = "\x1b[{row};{col}H"

        for y in range(self.height):
            prev_row = self._prev[y] if y < len(self._prev) else self._prev[-1]

            cur_row = self._curr[y] if y < len(self._curr) else self._curr[-1]


            max_len = max(len(prev_row), len(cur_row))
            if len(prev_row) < max_len:
                prev_row += [EMPTY_CELL] * (max_len - len(prev_row))
            if len(cur_row) < max_len:
                cur_row += [EMPTY_CELL] * (max_len - len(cur_row))

            col = 0
            while col < max_len:
                if prev_row[col] != cur_row[col]:
                    start = col
                    while col < max_len and prev_row[col] != cur_row[col]:
                        col += 1
                    segment = cur_row[start:col]

                    out.append(move.format(row=y + 1, col=start + 1))
                    seq = ""
                    for ch, fg, bg in segment:
                        seq += f"\x1b[{fg};{bg}m{ch}"
                    seq += "\x1b[0m"
                    out.append(seq)
                else:
                    col += 1

        if out:
            print("".join(out), end="", flush=True)

        # Buffer‑Tausch für den nächsten Frame
        self._prev, self._curr = self._curr, self._prev
        self._curr = self._make_empty_buffer()
