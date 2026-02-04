from template.armor import Armor
from core.equipment import EquipmentSlot

# --- KOPF ---
class IronHead(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenhelm",
            description="Ein schwerer, kalter Helm aus geschmiedetem Eisen.",
            defense=5,
            slot=EquipmentSlot.HEAD
        )

# --- TORSO ---
class IronChestplate(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenbrustplatte",
            description="Ein massiver Brustpanzer aus Eisenplatten.",
            defense=12,
            slot=EquipmentSlot.CHEST
        )

# --- BEINE ---
class IronLeggings(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenbeinschienen",
            description="Schützende Eisenplatten für die Oberschenkel und Waden.",
            defense=8,
            slot=EquipmentSlot.LEGS
        )

# --- FÜSSE ---
class IronBoots(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenstiefel",
            description="Schwere Stiefel mit Eisenkappen. Nicht sehr bequem, aber sicher.",
            defense=4,
            slot=EquipmentSlot.FEET
        )