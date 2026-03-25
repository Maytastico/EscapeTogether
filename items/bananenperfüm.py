from template.consumable import Consumable
from colorama import *

class Bananenperfüm(Consumable): # "Bananenperfüm" auf Deutsch

    def __init__(self):
        super().__init__(
            name="Bananenperfüm",
            description="Ein robustes Bananenperfüm mit einem gebogenen, abgeflachten Ende. Ideal zum Öffnen von Türen oder als improvisierte Banane.",
            hp=100
            # sehr effektiv
        )
    def interact(self, state: 'GameState'):
        super().interact(state)
        print()
        print(f"{Fore.YELLOW}{Style.BRIGHT}vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        print(f"Du sprühst das Perfüm auf deinen Körper. OH MEIN GOTT DAS RIECHT GUT!!111!11")
        print(f"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{Style.RESET_ALL}")
