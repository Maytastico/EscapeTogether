from template.item import Item, ItemProperties, ItemType
from typing import TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState

class Apple(Item):
    def __init__(self):
        super().__init__(
            name="Apfel",
            description="Ein knackiger grüner Apfel. Stillt ein wenig den Hunger.",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        print("Mampf... Der Apfel war erfrischend.")
        state.player.hunger -= 10 # Beispiel für ein Hunger-System
        state.player.inventory.remove_by_object(self)


class HealthPotion(Item):
    def __init__(self):
        super().__init__(
            name="Großer Heiltrank",
            description="Heilt 50 Lebenspunkte.",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )
        self.heal_amount = 50

    def interact(self, state: 'GameState'):
        player = state.player
        # Wir greifen auf base_stats.hp zu
        current_hp = player.base_stats.hp
        max_hp = 100 # Hier könntest du auch player.max_hp nutzen, falls vorhanden

        if current_hp >= max_hp:
            print(f"{Fore.YELLOW}Deine HP sind bereits voll!{Style.RESET_ALL}")
            return

        # Heilung anwenden
        new_hp = min(max_hp, current_hp + self.heal_amount)
        player.base_stats.hp = new_hp
        
        print(f"{Fore.GREEN}Du trinkst {self.name}. HP: {current_hp} -> {new_hp}{Style.RESET_ALL}")
        
        # Wichtig: Aus dem Inventar entfernen (deine Inventory.remove_by_object Methode)
        player.inventory.remove_by_object(self)


class StrengthElixir(Item):
    def __init__(self):
        super().__init__(
            name="Elixier der Stärke",
            description="Erhöht deine Basis-Stärke permanent um 2.",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )
        self.strength_gain = 2

    def interact(self, state: 'GameState'):
        player = state.player
        # Permanente Erhöhung der Basis-Stats
        player.base_stats.strength += self.strength_gain
        
        print(f"{Fore.CYAN}Du spürst neue Kraft! Basis-Stärke ist jetzt {player.base_stats.strength}.{Style.RESET_ALL}")
        print(f"Deine Gesamtstärke (inkl. Ausrüstung) beträgt nun: {player.total_stats.strength}")
        
        player.inventory.remove_by_object(self)


class Bread(Item):
    def __init__(self):
        super().__init__(
            name="Frisches Brot",
            description="Ein einfaches Brot. Heilt 10 HP.",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = min(100, player.base_stats.hp + 10)
        
        print(f"{Fore.GREEN}Das Brot schmeckt gut. +10 HP.{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)

class Egg(Item):
    def __init__(self):
        super().__init__(
            name="Frisches Ei",
            description="Ein Ei vom Huhn. Muss erste gekocht werden. Heil 4 HP",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = min(100, player.base_stats.hp + 4)
        
        print(f"{Fore.GREEN}Das Ei ist schleimig. +4 HP.{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)

class CookedEgg(Item):
    def __init__(self):
        super().__init__(
            name="Gebratenes Spiegelei",
            description="Ein leckeres Spiegelei. Heil 10 HP",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = min(100, player.base_stats.hp + 10)
        
        print(f"{Fore.GREEN}Das Spiegelei ist lecker. +10 HP.{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)

class Pepper(Item):
    def __init__(self):
        super().__init__(
            name="Pfeffer",
            description="Pfeffer zum Kochen. Lässt dich weinen.",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = min(100, player.base_stats.hp + 0)
        
        print(f"{Fore.GREEN}Pfeffer heilt dich nicht wirklich lol.{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)

class Salt(Item):
    def __init__(self):
        super().__init__(
            name="Salz",
            description="Salz zum Kochen. Lässt essen besser schmecken.",
            properties=ItemProperties(
                item_type=ItemType.CONSUMABLE,
                equippable=False,
                stackable=True,
                interactable=True
            )
        )

    def interact(self, state: 'GameState'):
        player = state.player
        player.base_stats.hp = min(100, player.base_stats.hp + 0)
        
        print(f"{Fore.GREEN}Salz heilt dich nicht wirklich lol.{Style.RESET_ALL}")
        player.inventory.remove_by_object(self)