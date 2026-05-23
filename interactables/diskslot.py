from template.interactable import Interactable
from template.disk import Disk
from core.gamestate import GameState
from typing import List, TYPE_CHECKING
from colorama import *
if TYPE_CHECKING:
    from template.item import Item

class Diskslot(Interactable):
    
    def __init__(self):
        super().__init__(
            name="Diskslot",
            description="Ein Diskslot vebindet zum Alten PC",
            locked=True
        )
        disk = None
    
    def use(self, state: GameState):
        
        if self.disk == None:
            print(f"Es ist keine Disk drinnen.")
        else:
            print(f"Disk drinnen: {self.disk.name}")
        
        inv_discs = [] #todotodo

        print(f"\nWas möchtest du tun?")

        