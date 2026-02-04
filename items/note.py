from core.gamestate import GameState
from template.item import Item, ItemProperties, ItemType
from colorama import Fore, Style

class Note(Item):
    """Eine einfache Notiz, die als Item gefunden werden kann."""
    def __init__(self, name:str = "Notiz", content: str= ""):
        super().__init__(
            name=name,
            description="Ein Stück Papier, das zwischen den Polstern steckte. Es steht etwas darauf geschrieben.",
            properties=ItemProperties(
                item_type=ItemType.QUEST,
                equippable=False,
                stackable=False,
                interactable=True
            )
        )
        self.content = content

    def interact(self, state: GameState):
        print(f"{Fore.YELLOW}Du liest die Notiz: {self.content}'{Style.RESET_ALL}")