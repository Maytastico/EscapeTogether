from template.item import ItemProperties, ItemType, Item
from core.stats import Stats
from core.equipment_slot import EquipmentSlot


class Armor(Item):
    def __init__(self, name: str, description: str, defense: int, slot: EquipmentSlot = EquipmentSlot.HEAD):
        self.properties = ItemProperties(ItemType.ARMOR, equippable=True, stackable=False, interactable=False)
        
        # Hier setzen wir das Stats-Objekt mit den gewünschten Boni
        self.properties.stat_modifiers = Stats(defense=defense)
        
        super().__init__(name, description, self.properties, slot)