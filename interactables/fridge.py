from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from typing import List

class Fridge(Interactable):
    
    def __init__(self, items: List = None, locked: bool = True):
        """Ein Kühlschrank, der Items kühlt und gelagert werden kann."""
        super().__init__(
            name="Kühlschrank",
            description="Ein großer, weißer Kühlschrank. Er summt leise vor sich hin.",
            items=items if items is not None else [],
            locked=locked # Der Kühlschrank startet standardmäßig geschlossen
        )

    def use(self, state: GameState):
        """Interaktion: Öffnen/Schließen und Items verwalten."""
        if self.locked:
            print(f"Du öffnest die Tür des {self.name}s. Ein Schwall kalter Luft kommt dir entgegen.")
            self.locked = False
            # Direkt das Menü nach dem Öffnen zeigen
            self._manage_items(state)
        else:
            print("Möchtest du [1] Etwas herausnehmen, [2] Etwas hineinlegen oder [3] Die Tür schließen?")
            choice = input("Wahl: ").strip()
            
            if choice == "1":
                self._take_item(state)
            elif choice == "2":
                self._place_item(state)
            elif choice == "3":
                self.locked = True
                print("Du schließt die Kühlschranktür mit einem satten Plopp.")

    def _manage_items(self, state: GameState):
        """Hilfsmethode für die Übersicht nach dem Öffnen."""
        if self.items:
            print("Im Inneren leuchtet ein schwaches Licht. Du siehst verschiedene Vorräte.")
        else:
            print("Der Kühlschrank ist gähnend leer.")

    def _take_item(self, state: GameState):
        if not self.items:
            print(f"{Fore.YELLOW}Nichts da, was man essen könnte.{Style.RESET_ALL}")
            return

        chosen_items = self._show_item_menu()
        if chosen_items:
            state.player.inventory.add(chosen_items)

    def _place_item(self, state: GameState):
        print(f"\n{Fore.CYAN}Was möchtest du kühl lagern?{Style.RESET_ALL}")
        items_to_place = state.player.inventory.open()
        
        if items_to_place:
            self.items.extend(items_to_place)
            print("Du hast die Items sicher verstaut.")

    def inspect(self):
        """Beschreibt den Zustand des Kühlschranks."""
        super().inspect()
        if not self.locked:
            print(f"{Fore.BLUE}Die Tür steht offen und die Kälte entweicht.{Style.RESET_ALL}")
        else:
            print("Die Tür ist fest verschlossen.")