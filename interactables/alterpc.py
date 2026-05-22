from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore,Style
from time import sleep
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from template.item import Item

class AlterPc(Interactable):
    
    def __init__(self):
        super().__init__(
            name="Alter PC",
            description="Ein alter PC mit Bananen OS",
            items=None,
            locked=False
        )
    ram = False
    
    def use(self, state: GameState) -> List["Item"]:
        
        print(f"\nDu startest den PC...")
        sleep(2)
        print()
        print(f"{Style.BRIGHT} BANANEN OS{Style.RESET_ALL}")
        sleep(0.5)
        print(f" Booting...")
        sleep(3)
        if self.ram:
            pass
        else:
            print(f"{Fore.RED}{Style.BRIGHT} !!! No RAM detected !!!{Style.RESET_ALL}")
            sleep(1)
            print(f" Shutting down...")
            sleep(3)
            print(f"\nDer Bildschirm wird schwarz...")

        
        