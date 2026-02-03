from template.item import Item, ItemProperties, ItemType
from core.equipment_slot import EquipmentSlot
from core.stats import Stats
from colorama import Fore, Style

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.gamestate import GameState

class LeatherBackpack(Item):
    def __init__(self):
        # Wir definieren hier die Stat-Modifier, die der Rucksack gibt
        # Zum Beispiel: Erhöht die Tragekapazität (hier als 'speed' simuliert 
        # oder du fügst ein neues Attribut in Stats ein)
        self.stat_modifiers = Stats(hp=0, strength=0, defense=2, speed=-2) 
        # Ein voller Rucksack macht vielleicht etwas langsamer (-2 Speed), 
        # schützt aber den Rücken (+2 Defense)

        super().__init__(
            name="Lederrucksack",
            description="Ein geräumiger Rucksack aus gegerbtem Leder. Erhöht deinen Platz, ist aber etwas sperrig.",
            properties=ItemProperties(
                item_type=ItemType.EQUIPMENT,
                equippable=True,
                stackable=False,
                interactable=False
            ),
            slot=EquipmentSlot.BACK
        )

    def interact(self, state: 'GameState'):
        # Optional: Man könnte den Rucksack auch benutzen, 
        # um zu sehen, wie voll er ist.
        current_weight = len(state.player.inventory.items)
        print(f"{Fore.CYAN}Du rückst die Gurte deines Rucksacks zurecht.")
        print(f"Er enthält aktuell {current_weight} Gegenstände.{Style.RESET_ALL}")