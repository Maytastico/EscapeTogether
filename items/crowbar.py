from template.weapon import Weapon
from template.item import ItemProperties, ItemType
from core.equipment import EquipmentSlot

class Crowbar(Weapon): # "Brechstange" auf Englisch

    def __init__(self):
        super().__init__(
            name="Brechstange",
            description="Eine robuste Stahlstange mit einem gebogenen, abgeflachten Ende. Ideal zum Aufbrechen von Kisten oder als improvisierte Waffe.",
            attack_power=7, # Weniger als ein Schwert, aber immer noch effektiv
            slot=EquipmentSlot.MAIN_HAND # Oder EquipmentSlot.TWO_HAND, falls sie beidhändig ist
        )