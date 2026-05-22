from template.interactable import Interactable
from core.gamestate import GameState
from items.ram import Ram
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from template.item import Item

class AltesGehäuse(Interactable):
    
    def __init__(self):
        super().__init__(
            name="Altes PC Gehäuse",
            description="Ein PC Gehäuse der mit dem Alten PC verbunden ist.",
            items=None,
            locked=False
        )
    ram = False
    
    def use(self, state: GameState) -> List["Item"]:
        
        if self.ram:
            print("Alle Bauteile eines PCs sind hier drinne!")
        else:
            print("Es sieht so aus als ob hier kein RAM drinn ist.")
            if state.player.inventory.has_item(Ram()):
                eingabe = input("Möchtest du dein RAM reintun? (y/n)")
                if eingabe.lower() == "y":
                    self.ram = True
                    state.player.inventory.remove_by_name("RAM")
                    print("Du hast dein RAM reingetan")
                else:
                    print("Du hast dich entschieden dein RAM nicht reinzutun")
