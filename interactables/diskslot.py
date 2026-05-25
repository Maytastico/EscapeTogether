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
        self.disk = None
    
    def use(self, state: GameState):
        
        if self.disk == None:
            print(f"Es ist keine Disk drinnen.")
        else:
            print(f"Diese Disk ist grade drinnen: {self.disk.name}")
        
        inv_discs = []
        for item in state.player.inventory.items:
            if isinstance(item, Disk):
                inv_discs.append(item)
        
        options = [f"Nichts"]
        if self.disk:
            options.append(f"Disk raustun")
            for disc in inv_discs:
                options.append(f"Disk austauschen mit: '{disc.name}'")
        else:
            for disc in inv_discs:
                options.append(f"Disk reintun: '{disc.name}'")

        eingabe = ""
        print(f"\nWas möchtest du tun?")
        for i in range(len(options)):
            print(f"[{i}] {options[i]}")
        print()

        eingabe = input(">>")
        if eingabe.isdigit():
            eingabe = int(eingabe)
            if eingabe >= 0 and eingabe < len(options):
                
                if eingabe == 0:
                    print(f"Du tust nichts.")
                else:
                    if self.disk:
                        if eingabe == 1:
                            # disk raustun
                            state.player.inventory.add([self.disk])
                            self.disk = None
                            print(f"Du entfernst die Disk.")
                        else:
                            # disk austauschen mit ...
                            state.player.inventory.add([self.disk])
                            state.player.inventory.remove_by_object(inv_discs[eingabe - 2])
                            self.disk = inv_discs[eingabe - 2]
                            print(f"Du tauscht die Disk aus.")
                    else:
                        # disk reintun ...
                        state.player.inventory.remove_by_object(inv_discs[eingabe - 1])
                        self.disk = inv_discs[eingabe - 1]
                        print(f"Du tust deine Disk rein.")

            else:
                print(f"Bitte gebe eine Nummer von 0 bis {len(eingabe)-1} ein")
        else:
            print(f"Bitte gebe eine Nummer ein")
