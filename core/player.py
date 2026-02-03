from core.inventory import Inventory
from core.stats import Stats
from template.item import Item
from core.equipment_slot import EquipmentSlot
from colorama import Fore, Style

class Player:
    def __init__(self, name: str = ""):
        self.name: str = name
        self.inventory:Inventory = Inventory()
        self.base_stats: Stats = Stats(hp=100, strength=10)
        
        # Das Equipment-Verzeichnis enthält nun alles
        self.equipment = {
            EquipmentSlot.HEAD: None,
            EquipmentSlot.CHEST: None,
            EquipmentSlot.LEGS: None,
            EquipmentSlot.FEET: None,
            EquipmentSlot.MAIN_HAND: None,
        }

    def equip(self, item: Item, slot: EquipmentSlot):
        """Universelle Methode zum Ausrüsten."""
        if not item.properties.equippable:
            print(f"{Fore.RED}Das Item '{item.name}' kann nicht ausgerüstet werden!{Style.RESET_ALL}")
            return

        # Altes Item zurück ins Inventar
        old_item = self.equipment[slot]
        if old_item:
            self.inventory.add(old_item)

        # Neues Item anlegen
        self.equipment[slot] = item
        print(f"{item.name} auf {slot.value} ausgerüstet.")

    @property
    def total_stats(self) -> Stats:
        total = self.base_stats
        for item in self.equipment.values():
            if item:
                total += item.properties.stat_modifiers
        return total