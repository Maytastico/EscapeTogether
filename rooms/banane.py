from typing import TYPE_CHECKING
from interactables.bananenhaufen import Bananenhaufen
from interactables.laptop import Laptop
from interactables.bananenmaschine import Bananenmaschine
from items.bananenperfüm import Bananenperfüm
from items.ram import Ram
from items.banane import BananenItem
from colorama import Fore, Style
from template.room import Room

if TYPE_CHECKING:
    from core.gamestate import GameState

class Banane(Room):
    def __init__(self):
        super().__init__(name="Bananen Raum", description="Ein Bananenraum in einem bananigen Geruch getaucht")
        self.interactables.update(
            {
                "bananenhaufen":Bananenhaufen([Bananenperfüm()]),
                "laptop":Laptop([Ram()]),
                "bananenmaschine":Bananenmaschine([BananenItem()])
            }
        )

    def exit(self, state: "GameState") -> bool:
        print(f"{Fore.RED}{Style.BRIGHT}Du bist nicht bananig um den Raum zu verlassen!!{Style.RESET_ALL}")