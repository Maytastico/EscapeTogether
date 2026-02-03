from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from typing import List

class Table(Interactable):
    
    def __init__(self, name: str = "Holztisch", description: str = "Ein einfacher Tisch aus Eichenholz.", items: List = None):
        """Ein Tisch, auf dem Gegenstände platziert und von dem sie genommen werden können."""
        super().__init__(
            name=name,
            description=description,
            items=items if items is not None else [],
            locked=False
        )

    def use(self, state: GameState):
        """Interaktion mit dem Tisch: Items nehmen oder abstellen."""
        print(f"\n--- {self.name} ---")
        print("[1] Etwas vom Tisch nehmen")
        print("[2] Etwas auf den Tisch stellen")
        print("[3] Nichts tun")
        
        choice = input("Was möchtest du tun? ").strip()

        if choice == "1":
            self._take_item(state)
        elif choice == "2":
            self._place_item(state)
        else:
            print("Du entscheidest dich, den Tisch so zu lassen, wie er ist.")

    def _take_item(self, state: GameState):
        """Nutzt das Menü der Basisklasse, um Items zu entnehmen."""
        if not self.items:
            print(f"{Fore.YELLOW}Der Tisch ist leer.{Style.RESET_ALL}")
            return

        # Die Basisklasse hat bereits die Logik zum Auswählen und Entfernen
        chosen_items = self._show_item_menu()
        
        if chosen_items:
            # Füge die entnommenen Items dem Spieler-Inventar hinzu
            state.player.inventory.add(chosen_items)

    def _place_item(self, state: GameState):
        """Öffnet das Spieler-Inventar, um ein Item auf den Tisch zu legen."""
        print(f"\n{Fore.CYAN}Welches Item möchtest du auf den Tisch legen?{Style.RESET_ALL}")
        
        # Wir nutzen die 'open'-Methode deines Inventars
        items_to_place = state.player.inventory.open()
        
        if items_to_place:
            self.items.extend(items_to_place)
            item_names = ", ".join([i.name for i in items_to_place])
            print(f"Du hast {item_names} auf den Tisch gestellt.")
        else:
            print("Du hast nichts abgelegt.")

    def inspect(self):
        """Zeigt an, was auf dem Tisch liegt."""
        super().inspect() # Nutzt die Standard-Anzeige der Basisklasse
        if not self.locked and self.items:
            # Zusätzlicher atmosphärischer Text
            print(f"Der Tisch sieht mit {len(self.items)} Gegenstand/Gegenständen darauf ziemlich belegt aus.")