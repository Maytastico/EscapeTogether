from template.interactable import Interactable
from core.gamestate import GameState
from typing import List, TYPE_CHECKING
from colorama import *
if TYPE_CHECKING:
    from template.item import Item

class Bananenmaschine(Interactable):
    
    def __init__(self, items: list = None):
        super().__init__(
            name="Bananenmaschine",
            description="Eine robuste Bananenmaschine mit einem Bananenmaschinenknopf.",
            items=items,
            locked=False
        )
    
    def use(self, state: GameState) -> List["Item"]:
        if self.items == []:
            print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}BANANENMASCHINE ÜBERFORDERT.\nKANN KEINE WEITEREN BANANEN PRODOZIEREN.{Style.RESET_ALL}")
        else:
            print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}KNOPF GEDRÜCKT.\nBANANE WIRD PRODUZIERT.{Style.RESET_ALL}")
            return self._show_item_menu()