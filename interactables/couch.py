from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from items.note import Note
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from template.item import Item

class Couch(Interactable):
    def __init__(self, items: List[Item]):
        super().__init__(
            name="Sofa",
            description="Eine alte, durchgesessene Couch mit braunem Samtbezug.",
            # Die Notiz legen wir direkt in die Items-Liste des Interactables
            items=[Note()]
        )
        self.is_lying_down = False

    def use(self, state: GameState):
        """Ermöglicht es dem Spieler, sich auf die Couch zu legen."""
        if not self.is_lying_down:
            self.is_lying_down = True
            print(f"{Fore.GREEN}Du legst dich auf die weichen Polster. Endlich mal eine Pause...{Style.RESET_ALL}")
            # Optional: Heile den Spieler ein wenig, wenn er sich ausruht
            state.player.base_stats.hp = min(100, state.player.base_stats.hp + 5)
            print("Du fühlst dich ein kleines bisschen erholter (+5 HP).")
        else:
            self.is_lying_down = False
            print("Du stehst wieder auf und bist bereit für weitere Abenteuer.")

    def inspect(self):
        """Untersucht die Couch und findet versteckte Items."""
        # Name und Beschreibung aus der Basisklasse anzeigen
        print(f"\nDu untersuchst: {self.name}")
        print(self.get_description())

        # Logik für das Finden der Notiz
        if self.items:
            print(f"{Fore.CYAN}Als du zwischen die Polster greifst, spürst du etwas Hartes...{Style.RESET_ALL}")
            # Nutzt das Menü aus der Basisklasse, um das Item zu entnehmen
            # In deinem System gibt _show_item_menu eine Liste zurück
            selected_items = self._show_item_menu()
            
            # Die Basisklasse Interactable kümmert sich in _show_item_menu 
            # bereits um das Entfernen aus self.items.
            return selected_items
        else:
            print("Du suchst in den Ritzen, findest aber nur ein paar alte Krümel.")

        if self.is_lying_down:
            print("Die Kissen sind noch warm, wo du gerade gelegen hast.")