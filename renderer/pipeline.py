from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from renderer.renderer import TerminalRenderer
# renderer/pipeline.py
def render_frame(state, renderer: "TerminalRenderer"):
    renderer.draw_text(int(renderer.width/2), int(renderer.height/2), "Hi du Nudel")
    renderer.draw_text(3, 3, "Bananen sind schön")
    renderer.draw_text(5, 4, "Blumen sind bunt")
    renderer.draw_text(3, 10, "Blumen sind bunt")
    renderer.render()
