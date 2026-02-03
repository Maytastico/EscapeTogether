from template.item import Item, ItemProperties, ItemType
from core.equipment_slot import EquipmentSlot
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from core.gamestate import GameState

class Pan(Item):

    def __init__(self):
        super().__init__(
            name="Pfanne", 
            description="Eine große schwarze Pfanne mit eingebrannten Essensresten.",
            attack_power=10,
            properties=ItemProperties(
                item_type=ItemType.QUEST,
                equippable=True, # Auf True gesetzt, da ein Slot zugewiesen ist
                stackable=False,
                interactable=True,
            ),
            slot=EquipmentSlot.MAIN_HAND
        )
        # Liste direkt initialisieren
        self.contents: List[Item] = [] 

    def interact(self, state: 'GameState'):
        print(f"--- {self.name} ---")
        if self.contents:
            contained_names = ", ".join([item.name for item in self.contents])
            print(f"In der Pfanne liegt bereits: {contained_names}")
        
        print("Möchtest du etwas zum Kochen hineinlegen?")

        # Items aus dem Inventar holen
        new_items = state.player.inventory.open()
        
        if new_items:
            self.contents.extend(new_items)
            print(f"Du hast {len(new_items)} Item(s) in die Pfanne gelegt.")
        else:
            print("Du hast nichts hinzugefügt.")

    def clear_pan(self) -> List[Item]:
        """Leert die Pfanne und gibt die Items zurück (z.B. nach dem Kochen)."""
        items_to_return = self.contents[:]
        self.contents.clear()
        return items_to_return