from template.interactable import Interactable
from core.gamestate import GameState
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from template.item import Item

class Bananenhaufen(Interactable):
    
    def __init__(self, items: list = None):
        super().__init__(
            name="Bananenhaufen",
            description="Ein robuster Bananenhaufen mit einem Bananenperfüm.",
            items=items,
            locked=False
        )
    
    def use(self, state: GameState) -> List["Item"]:
        # 1. Fall: Schrank ist schon offen
        return self._show_item_menu()
        