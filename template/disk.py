from template.item import Item, ItemProperties, ItemType
from typing import TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState

class Disk(Item):
    def __init__(self, name: str = "Disk", description: str = "Eine Disk für einen bestimmten PC"):
        super().__init__(
            name=name,
            description=description,
            properties=ItemProperties(
                item_type=ItemType.MATERIAL,
                equippable=False,
                stackable=False,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        print("Du kannst nicht mit einer Disk interagieren aber ein bestimmter PC schon...")

    def play(self,pc):
        print("standard disk disk lolol")