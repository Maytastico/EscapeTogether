
from template.consumable import Consumable
from typing import TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState

class Apple(Consumable):
    def __init__(self):
        super().__init__(
            name="Apfel",
            description="Ein knackiger grüner Apfel. Stillt ein wenig den Hunger.",
            hp=10
        )

class HealthPotion(Consumable):
    def __init__(self):
        super().__init__(
            name="Großer Heiltrank",
            description="Heilt 50 Lebenspunkte.",
            hp=50
        )

class StrengthElixir(Consumable):
    def __init__(self):
        super().__init__(
            name="Elixier der Stärke",
            description="Erhöht deine Basis-Stärke permanent um 2.",
            hp=0
        )
        self.strength_gain = 2

    def interact(self, state: 'GameState'):
        player = state.player
        # Permanente Erhöhung der Basis-Stats
        player.base_stats.strength += self.strength_gain
        
        print(f"{Fore.CYAN}Du spürst neue Kraft! Basis-Stärke ist jetzt {player.base_stats.strength}.{Style.RESET_ALL}")
        print(f"Deine Gesamtstärke (inkl. Ausrüstung) beträgt nun: {player.total_stats.strength}")
        
        player.inventory.remove_by_object(self)

class Bread(Consumable):
    def __init__(self):
        super().__init__(
            name="Frisches Brot",
            description="Ein einfaches Brot. Heilt 10 HP.",
            hp=10
        )

class Egg(Consumable):
    def __init__(self):
        super().__init__(
            name="Frisches Ei",
            description="Ein Ei vom Huhn. Muss erste gekocht werden. Heil 4 HP",
            hp=4
        )

class CookedEgg(Consumable):
    def __init__(self):
        super().__init__(
            name="Gebratenes Spiegelei",
            description="Ein leckeres Spiegelei. Heil 10 HP",
            hp=10
        )

class Pepper(Consumable):
    def __init__(self):
        super().__init__(
            name="Pfeffer",
            description="Pfeffer zum Kochen. Lässt dich weinen.",
            hp=0
        )

class Salt(Consumable):
    def __init__(self):
        super().__init__(
            name="Salz",
            description="Salz zum Kochen. Lässt essen besser schmecken.",
            hp=0
        )