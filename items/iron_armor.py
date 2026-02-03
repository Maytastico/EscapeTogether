from template.armor import Armor
from template.item import ItemProperties, ItemType
from core.equipment_slot import EquipmentSlot

# --- KOPF ---
class IronHead(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenhelm",
            description="Ein schwerer, kalter Helm aus geschmiedetem Eisen.",
            defense_value=5,
            properties=ItemProperties(
                item_type=ItemType.ARMOR,
                equippable=True,
                stackable=False,
                interactable=False
            ),
            slot=EquipmentSlot.HEAD
        )

# --- TORSO ---
class IronChestplate(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenbrustplatte",
            description="Ein massiver Brustpanzer aus Eisenplatten.",
            defense_value=12,
            properties=ItemProperties(
                item_type=ItemType.ARMOR,
                equippable=True,
                stackable=False,
                interactable=False
            ),
            slot=EquipmentSlot.CHEST
        )

# --- BEINE ---
class IronLeggings(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenbeinschienen",
            description="Schützende Eisenplatten für die Oberschenkel und Waden.",
            defense_value=8,
            properties=ItemProperties(
                item_type=ItemType.ARMOR,
                equippable=True,
                stackable=False,
                interactable=False
            ),
            slot=EquipmentSlot.LEGS
        )

# --- FÜSSE ---
class IronBoots(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenstiefel",
            description="Schwere Stiefel mit Eisenkappen. Nicht sehr bequem, aber sicher.",
            defense_value=4,
            properties=ItemProperties(
                item_type=ItemType.ARMOR,
                equippable=True,
                stackable=False,
                interactable=False
            ),
            slot=EquipmentSlot.FEET
        )