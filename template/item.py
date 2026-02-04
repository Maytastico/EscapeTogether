from abc import ABC
from typing import TYPE_CHECKING
from enum import Enum
from core.stats import Stats

if TYPE_CHECKING:
    from core.gamestate import GameState
    from core.equipment import EquipmentSlot

class ItemType(Enum):
    WEAPON = 1
    ARMOR = 2
    CONSUMABLE = 3
    QUEST = 4
    MATERIAL = 5

class ItemProperties:
    def __init__(self, item_type=ItemType.MATERIAL, equippable=False, stackable=True, interactable=False):
        self.item_type = item_type
        self.equippable = equippable
        self.interactable = interactable
        self.stackable = stackable
        self.rarity: str = "Common"
        self.value: int = 0
        self.weight: float = 0.0
        
        self.stat_modifiers: Stats = Stats()

class Item(ABC):
    
    def __init__(self, name: str, description: str="", properties: ItemProperties = ItemProperties(), slot: EquipmentSlot= None):
        super().__init__()
        self.name: str = name
        self.description: str = description
        self.properties: ItemProperties = properties
        self.slot: EquipmentSlot = slot
    
    def interact(self, state: GameState):
        if not self.properties.interactable:
            print("Du kannst nicht mit diesem Item interagieren")

    def inspect(self):
        print(self.get_description())

    def get_description(self):
        return self.description



