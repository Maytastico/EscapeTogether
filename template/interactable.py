from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from template.item import Item
    from core.gamestate import GameState

class Interactable(ABC):
    """
    Ein 'Interactable' ist ein Objekt in der Spielwelt, mit dem der Spieler 
    etwas machen kann (z.B. ein Schrank, ein Computer oder eine Truhe).
    
    Diese Klasse dient als Bauplan (Interface) für alle speziellen Objekte.
    """

    def __init__(self, name: str, description: str, items: Optional[List['Item']] = None, locked: bool = False):
        """
        Erstellt ein neues interaktives Objekt.
        
        Args:
            name: Der Name (z.B. 'Alter Safe').
            description: Was der Spieler sieht, wenn er das Objekt ansieht.
            items: Eine Liste von Gegenständen, die sich darin befinden.
            items_locked: Wenn True, kommt der Spieler erst nach einem Rätsel an die Items.
        """
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.locked = locked

    @abstractmethod
    def use(self, gamestate: 'GameState'):
        """
        Diese Methode MUSS in jeder Unterklasse (z.B. Klasse 'Computer') definiert werden.
        Hier wird festgelegt, was passiert, wenn man 'Benutzen' drückt.
        """
        pass

    def inspect(self):
        """
        Beschreibt das Objekt und zeigt gefundene Items an, falls diese nicht gesperrt sind.
        """
        print(f"\nDu untersuchst: {self.name}")
        print(self.get_description())

        # Hier nutzt du jetzt korrekt self.locked
        if self.locked:
            print("Es scheint verschlossen zu sein. Du musst erst ein Rätsel lösen oder einen Schlüssel finden.")
        elif self.items:
            self._show_item_menu()
        else:
            print("Du findest hier nichts Brauchbares.")

    def get_description(self) -> str:
        """Gibt den Beschreibungstext zurück."""
        return self.description
        
    def _show_item_menu(self) -> Optional[List['Item']]:
        """
        Ermöglicht die Auswahl mehrerer Items gleichzeitig (z.B. 0, 2).
        Gibt eine Liste der entnommenen Items zurück.
        """
        if not self.items:
            return None

        print("\nFolgende Items befinden sich hier:")
        for idx, item in enumerate(self.items):
            print(f"[{idx}] {item.name}")
        
        print(f"[{len(self.items)}] Abbrechen")
        
        raw_choice = input("Was möchtest du mitnehmen? (Nummern mit Komma trennen, z.B. 0,2): ").strip()
        
        # Eingabe in eine Liste von Zahlen umwandeln
        # Wir filtern alles raus, was keine Zahl ist oder nicht im Bereich der Liste liegt
        chosen_indices = []
        for part in raw_choice.split(','):
            part = part.strip()
            if part.isdigit():
                idx = int(part)
                if 0 <= idx < len(self.items):
                    chosen_indices.append(idx)

        if not chosen_indices:
            print("Du nimmst nichts mit.")
            return None

        # WICHTIG: Wir sortieren die Indizes absteigend (von groß nach klein).
        # Warum? Wenn wir Item 0 löschen, rutscht Item 1 auf Position 0 nach.
        # Löschen wir von hinten nach vorne, bleiben die vorderen Indizes korrekt!
        selected_items = []
        for idx in sorted(chosen_indices, reverse=True):
            item = self.items.pop(idx)
            selected_items.append(item)
            print(f"Du hast '{item.name}' eingesteckt.")

        return selected_items