from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from renderer.ansi_colors import *

if TYPE_CHECKING:
    from renderer.renderer import TerminalRenderer, Cell
    from typing import List

pipeline: List[Widget] = []

map: List[List[Cell]] = [
    [("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_RED),("0", FG_BLUE, BG_GREEN)],
    [("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_GREEN),("0", FG_BLUE, BG_GREEN)],
]

# renderer/pipeline.py
def render_frame(state, renderer: "TerminalRenderer"):
    renderer.draw_text(int(renderer.width/2), int(renderer.height/2), "Hi du Nudel")
    renderer.draw_text(3, 3, "Bananen sind schön")
    renderer.draw_text(5, 4, "Blumen sind bunt")
    renderer.draw_text(3, 10, "Blumen sind bunt")
    renderer.draw_rect(int(renderer.height / 2 - 10), int(renderer.width /2 - 50), 5, 100, bg=BG_YELLOW)
    renderer.drawCellMap(int(renderer.height / 2 - 10), int(renderer.width /2 - 50), map)
    renderer.render()

class Widget(ABC):

    @abstractmethod
    def draw():
        pass