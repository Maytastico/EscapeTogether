from template.item import Item
from colorama import *
import math

class Ram(Item): # "RAM" als Amkürzung

    def __init__(self):
        super().__init__(
            name="RAM",
            description="Ein robustes RAM mit einem gebogenen, abgeflachten Ende. Ideal zum Computerbauer traden oder als improvisierten CPU.",
            # sehr effektiv
        )
    def interact(self, state: 'GameState'):
        print(f"{Style.BRIGHT}{Fore.WHITE}Du selber kannst nichts momentan mit diesem RAM anfangen.\nVielleicht kann ein Computerbauer etwas damit anfangen...{Style.RESET_ALL}")
        return
