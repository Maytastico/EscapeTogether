from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from items.pan import Pan
    from template.recipe import Recipe

class Stove(Interactable):
    def __init__(self, recipes: List['Recipe']):
        super().__init__(
            name="Küchenherd",
            description="Ein alter Gasherd. Die Flammen leuchten bläulich.",
        )
        self.recipes = recipes

    def use(self, state: GameState):
        print(f"\n{Fore.ORANGE}--- {self.name} ---{Style.RESET_ALL}")
        
        # 1. Prüfen, ob der Spieler eine Pfanne in der Hand hält
        active_item = state.player.equipment.get(state.player.equipment_slot.MAIN_HAND)
        
        if not isinstance(active_item, Pan):
            print("Du brauchst eine Pfanne in der Hand, um hier etwas zu kochen.")
            return

        if not active_item.contents:
            print("Die Pfanne ist leer. Leg erst Zutaten hinein (Pfanne im Inventar benutzen).")
            return

        print(f"Du stellst die Pfanne mit {len(active_item.contents)} Zutaten auf den Herd...")
        self._try_cooking(active_item, state)

    def _try_cooking(self, pan: 'Pan', state: GameState):
        # Namen der aktuellen Zutaten in der Pfanne extrahieren und sortieren
        current_ingredients = sorted([item.name for item in pan.contents])
        
        for recipe in self.recipes:
            if current_ingredients == recipe.ingredients:
                print(f"{Fore.GREEN}Es zischt und brutzelt... Du hast '{recipe.result_item.name}' zubereitet!{Style.RESET_ALL}")
                
                # Pfanne leeren und das neue Item ins Inventar legen
                pan.clear_pan()
                state.player.inventory.add([recipe.result_item])
                return

        # Wenn kein Rezept passt
        print(f"{Fore.RED}Das riecht nicht gut... Die Zutaten verkohlen zu ungenießbarem Matsch.{Style.RESET_ALL}")
        pan.clear_pan()