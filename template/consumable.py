from template.item import Item, ItemProperties, ItemType
from typing import TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState

class Consumable(Item):
    def __init__(self, name: str = "Essbares Item", description: str = "", hp: int = 0):
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

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = min(100, player.base_stats.hp + 0)
        
        print(f"{Fore.GREEN}Du isst {self.name}. Du bekommst {self.hp} HP{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)