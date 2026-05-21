from template.interactable import Interactable
from core.gamestate import GameState
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from template.item import Item

class BananenBaum(Interactable):
    
    def __init__(self, items: list = None):
        super().__init__(
            name="Bananenbaum",
            description="Ein robuster Bananenbaum mit einem Banane.",
            items=items,
            locked=False
        )
    
    def use(self, state: GameState) -> List["Item"]:
        
        return self._show_item_menu()
        