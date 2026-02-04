from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from typing import List, TYPE_CHECKING
from core.equipment import EquipmentSlot
from items.pan import Pan

if TYPE_CHECKING:
    from template.recipe import Recipe
    from template.item import Item

class Stove(Interactable):
    def __init__(self, recipes: List['Recipe']):
        super().__init__(
            name="Küchenherd",
            description="Ein alter Gasherd. Die Flammen leuchten bläulich.",
        )
        self.recipes = recipes

    def use(self, state: GameState) -> List[Item]:
        print(f"\n{Fore.YELLOW}--- {self.name} ---{Style.RESET_ALL}")
        
        # 1. Ausrüstung prüfen
        active_item = state.player.equipment.get(EquipmentSlot.MAIN_HAND)
        
        # Sicherstellen, dass es eine Pfanne ist (und nicht None)
        if not isinstance(active_item, Pan):
            print(f"{Fore.RED}Du brauchst eine Pfanne in der Hand (ausgerüstet), um hier etwas zu kochen.{Style.RESET_ALL}")
            return

        # 2. Inhalt prüfen
        if not active_item.contents:
            print("Die Pfanne ist leer. Du kannst keine heiße Luft braten!")
            return

        # 3. Kochvorgang starten
        zutaten_liste = ", ".join([item.name for item in active_item.contents])
        print(f"Du stellst die Pfanne mit {Fore.CYAN}{zutaten_liste}{Style.RESET_ALL} auf das Feuer...")
        return self._try_cooking(active_item, state)

    def _try_cooking(self, pan: 'Pan', state: GameState):
        # Normalisierung der Namen (strip und lower), um Fehler durch Leerzeichen/Großschreibung zu vermeiden
        current_ingredients = sorted([item.name.strip().lower() for item in pan.contents])
        
        for recipe in self.recipes:
            # Wir gehen davon aus, dass recipe.ingredients in der Recipe-Klasse ebenfalls sortiert und kleingeschrieben sind
            if current_ingredients == recipe.ingredients:
                print(f"{Fore.GREEN}Es zischt und brutzelt verführerisch... Du hast '{recipe.result_item.name}' zubereitet!{Style.RESET_ALL}")
                
                # Das Ergebnis-Item
                new_item = recipe.result_item
                
                pan.clear_pan()
                
                # Wichtig: Deine Inventory.add() Methode erwartet laut vorigem Code eventuell eine Liste oder ein Item.
                # Wenn sie ein Item erwartet:
                return [new_item]

        # Fehlgeschlagener Versuch
        print(f"{Fore.RED}Ein beißender Geruch steigt auf... Deine Zutaten ({', '.join(current_ingredients)}) sind zu ungenießbarem Matsch verkohlt.{Style.RESET_ALL}")
        pan.clear_pan()