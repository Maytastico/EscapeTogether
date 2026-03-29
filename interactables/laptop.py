from template.interactable import Interactable
from core.gamestate import GameState
from typing import List, TYPE_CHECKING
import os
from time import sleep
from colorama import *
if TYPE_CHECKING:
    from template.item import Item

class Laptop(Interactable):
    
    def __init__(self, items: list = None):
        super().__init__(
            name="Laptop",
            description="Ein robuster Laptop mit einem Bananensticker.",
            items=items,
            locked=True
        )
    
    def use(self, state: GameState) -> List["Item"]:
        if self.locked:
            print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}BITTE EINLOGGEN :)")
            print(f"{Style.NORMAL}Username: {os.getlogin()}")
            passwort = input(f"Passwort: ")
            print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED}FALSCHESS PASSWORT!!!!!11!!")
            sleep(1)
            print(f"SELBSTZERSTÖRUNG IN")
            sleep(0.5)
            print(f"3")
            sleep(1)
            print(f"2")
            sleep(1)
            print(f"1")
            sleep(1)
            print(f"{Style.NORMAL}{Fore.RED}B{Fore.YELLOW}U{Fore.BLACK}M{Fore.RED}M{Fore.BLACK}!{Fore.YELLOW}!")
            sleep(0.5)
            print(f"{Style.RESET_ALL}{Style.BRIGHT}Der Laptop explodiert und das hier wird sichtbar:{Style.RESET_ALL}")
            self.locked = False
            return self._show_item_menu()
        else:
            if self.items == []:
                print(f"{Style.RESET_ALL}{Style.BRIGHT}In den Ruinen von dem ehemaligen Laptop ist nichts mehr{Style.RESET_ALL}")
                return
            else:
                print(f"{Style.RESET_ALL}{Style.BRIGHT}In den Ruinen von dem ehemaligen Laptop ist das hier:{Style.RESET_ALL}")
                return self._show_item_menu()