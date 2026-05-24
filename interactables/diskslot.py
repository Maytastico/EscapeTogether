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
            print(f"Diese Disk ist grade drinnen: {self.disk.name}")
        
        inv_discs = []
        for item in state.player.inventory.items:
            if item == Disk:
                inv_discs.append(item)
        options = [f"Nichts"]
        if self.disk:
            options.append(f"Disk raustun")
            for disc in inv_discs:
                options.append(f"Disk austauschen mit {disc.name}")
        else:
            for disc in inv_discs:
                options.append(f"Disk reintun {disc.name}")

        eingabe = ""
        while not eingabe.isdigit()
        print(f"\nWas möchtest du tun?")
        for i in len(options): # todo: alternative für for loop
            print(f"[{i}] {options[i]}")
        print()

        eingabe = input(">>")
