from template.room import Room
from interactables.fridge import Fridge
from interactables.stove import Stove
from interactables.table import Table
from template.recipe import Recipe
from items.consumables import Salt, Pepper, Egg, CookedEgg
from typing import TYPE_CHECKING
from items.pan import Pan

if TYPE_CHECKING: 
    from core.gamestate import GameState

class Kitchen(Room):
    def __init__(self):
        super().__init__(
            name="Küche",
            description="Ein moderner, aber etwas unordentlicher Küchenbereich. Es riecht nach altem Fett und Reinigungsmitteln."
        )
        ultimatives_rezept = Recipe(ingredients=[Salt(), Pepper(), Egg()], result_item=CookedEgg())
        # Interactables hinzufügen
        self.interactables = {
            "kühlschrank": Fridge(items=[Salt(), Pepper(), Egg()], locked=False),
            "herd": Stove(recipes=[ultimatives_rezept]),
            "küchentisch": Table(items=[Pan(contents=[Salt(), Pepper(), Egg()])])
        }
        
    def exit(self, gamestate: GameState) -> bool:
        if gamestate.player.inventory.has_item(CookedEgg()):
            return True

        print("Du brauchst was zu essen um in den nächsten Raum zu kommen")
        return False

