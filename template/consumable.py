from template.item import Item, ItemProperties, ItemType
from typing import TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState

class Consumable(Item):
    def __init__(self, name: str = "Essbares Item", description: str = "", hp: int = 0, bananig: bool = False):
        super().__init__(
            name=name,
            description=description,
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )
        self.hp = hp
        self.bananig = bananig

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = player.base_stats.hp
        player.base_stats.hp += self.hp
        if player.base_stats.bananig:
            player.base_stats.bananig = True
        else:
            player.base_stats.bananig = self.bananig
        
        print(f"{Fore.GREEN}Du isst {self.name}. Du bekommst {self.hp} HP{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)