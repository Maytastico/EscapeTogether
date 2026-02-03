from template.item import Item, ItemProperties, ItemType
from core.gamestate import GameState
from core.stats import Stats
from core.equipment_slot import EquipmentSlot

class Weapon(Item):
    def __init__(self, 
                 name: str, 
                 description: str, 
                 attack_power: int, 
                 weapon_type: str = "Sword",
                 rarity: str = "Common",
                 slot:EquipmentSlot = EquipmentSlot.MAIN_HAND):
        
        # Eigenschaften für Waffen: Ausrüstbar, aber nicht stapelbar
        props = ItemProperties(
            item_type=ItemType.WEAPON, 
            equippable=True, 
            stackable=False,
            interactable=False
        )
        props.rarity = rarity
        
        # Wir speichern die Angriffskraft im Stats-Objekt
        # (Falls deine Stats-Klasse noch kein 'strength' oder 'attack' hat, 
        # kannst du das dort ergänzen)
        props.stat_modifiers = Stats(strength=attack_power)
        
        super().__init__(name, description, props)
        
        self.attack_power = attack_power
        self.weapon_type = weapon_type
        self.slot: EquipmentSlot = slot


    def interact(self, state: 'GameState'):
        """Wird aufgerufen, wenn der Spieler die Waffe im Inventar anklickt."""
        print(f"Du ziehst dein {self.name}...")
        # Nutzt die universelle equip-Methode des Players für die Haupthand
        state.player.equip(self, EquipmentSlot.MAIN_HAND)

    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc} [Attack: {self.attack_power} | Type: {self.weapon_type}]"