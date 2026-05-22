from template.item import Item
from colorama import *

class Ram(Item): # "RAM" als Amkürzung

    def __init__(self):
        super().__init__(
            name="RAM",
            description="Ein robustes RAM mit einem gebogenen, abgeflachten Ende. Ideal zum Computerbauen oder als improvisierten CPU.",
            # sehr effektiv
        )
    def interact(self, state: 'GameState'):
        print(f"{Style.BRIGHT}{Fore.WHITE}Du selber kannst nichts momentan mit diesem RAM anfangen.\nVielleicht kann ein Computer etwas damit anfangen...{Style.RESET_ALL}")
        return
