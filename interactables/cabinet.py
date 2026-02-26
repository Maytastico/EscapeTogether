from template.interactable import Interactable
from core.gamestate import GameState
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from template.item import Item

class Cabinet(Interactable):
    
    def __init__(self, code: str, items: list = None):
        super().__init__(
            name="Schrank",
            description="Eine robuste Metallbox mit einem Tastenfeldschloss.",
            items=items,
            locked=True
        )
        self.code = code
    
    def use(self, state: GameState) -> List["Item"]:
        # 1. Fall: Schrank ist schon offen
        if not self.locked:
            print("Der Schrank ist bereits geöffnet.")
            self._show_item_menu()
            return # Wir beenden die Funktion hier

        # 2. Fall: Schrank ist noch zu -> Code abfragen
        eingabe = input("Tastenfeld-Code eingeben: ").strip()
        
        if eingabe == self.code:
            print("KLICK! Der Schrank öffnet sich.")
            self.locked = False  # Schloss wird dauerhaft entfernt
            return self._show_item_menu()
        else:
            print("Falscher Code! Das Schloss piept rot.")