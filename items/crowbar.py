from template.weapon import Weapon
from template.item import ItemProperties, ItemType
from core.equipment_slot import EquipmentSlot

class Crowbar(Weapon): # "Brechstange" auf Englisch

    def __init__(self):
        super().__init__(
            name="Brechstange",
            description="Eine robuste Stahlstange mit einem gebogenen, abgeflachten Ende. Ideal zum Aufbrechen von Kisten oder als improvisierte Waffe.",
            attack_power=7, # Weniger als ein Schwert, aber immer noch effektiv
            properties=ItemProperties(
                item_type=ItemType.TOOL, # Oder ItemType.WEAPON, je nachdem wie du es klassifizierst
                equippable=True,
                stackable=False,
                interactable=True, # Brechstangen können oft für Umwelträtsel genutzt werden
            ),
            slot=EquipmentSlot.MAIN_HAND # Oder EquipmentSlot.TWO_HAND, falls sie beidhändig ist
        )