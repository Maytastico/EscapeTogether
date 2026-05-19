from template.consumable import Consumable
from colorama import *
from core.gamestate import GameState
from items.bananenschale import Bananenschale

class BananenItem(Consumable): # "Banane" auf Deutsch

    def __init__(self):
        super().__init__(
            name="Banane",
            description="Eine robuste Banane mit einem gebogenen, abgeflachten Ende. Ideal zum Essen oder als improvisiertes Bananenperfüm.",
            hp=10000
            # sehr effektiv
        )
    def interact(self, state: "GameState"):
        super().interact(state)
        
        state.player.inventory.add([Bananenschale()])
        