from typing import TYPE_CHECKING
from interactables.bananenbaum import BananenBaum
from items.bananenperfüm import Bananenperfüm
from items.ram import Ram
from items.banane import BananenItem
from colorama import Fore, Style
from template.room import Room
from core.stats import Stats

if TYPE_CHECKING:
    from core.gamestate import GameState

class BananenGarten(Room):
    def __init__(self):
        super().__init__(name="Bananen-Garten", description="Ein Garten mit einem riesigen Bananenbaum")
        self.interactables.update(
            {
                "bananenbaum": BananenBaum()
            }
        )

    def exit(self, state: "GameState") -> bool:
        if state.player.base_stats.bananig:
            print(f"{Fore.GREEN}{Style.BRIGHT}Du bist bananig genug!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Du bist nicht bananig genug um den Raum zu verlassen!!{Style.RESET_ALL}")
            return False