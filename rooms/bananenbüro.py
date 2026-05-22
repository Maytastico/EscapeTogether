from typing import TYPE_CHECKING
from interactables.alterpc import AlterPc
from interactables.altespcgehäuse import AltesGehäuse
#from items.bananenperfüm import Bananenperfüm
from colorama import Fore, Style
from template.room import Room
from core.stats import Stats

if TYPE_CHECKING:
    from core.gamestate import GameState

class BananenBüro(Room):
    def __init__(self):
        super().__init__(name="Bananen Büro", description="Ein Büro nur für Bananenarbeiten gedacht")
        self.interactables.update(
            {
                "alterpc":AlterPc(),
                "pcgehäuse":AltesGehäuse()
            }
        )

    def exit(self, state: "GameState") -> bool:
        # wip
        return False