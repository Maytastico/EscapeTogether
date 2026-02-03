from core.gamestate import GameState
from template.item import Item, ItemProperties, ItemType
from colorama import Fore, Style

class Note(Item):
    """Eine einfache Notiz, die als Item gefunden werden kann."""
    def __init__(self):
        super().__init__(
            name="Zerknitterte Notiz",
            description="Ein Stück Papier, das zwischen den Polstern steckte. Es steht etwas darauf geschrieben.",
            properties=ItemProperties(
                item_type=ItemType.QUEST,
                equippable=False,
                stackable=False,
                interactable=True
            )
        )

    def interact(self, state: GameState):
        print(f"{Fore.YELLOW}Du liest die Notiz: 'Vergiss nicht, das Radio auf 101.2 MHz zu stellen!'{Style.RESET_ALL}")