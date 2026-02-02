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
        
    def _show_item_menu(self) -> Optional['Item']:
        """
        Zeigt ein interaktives Menü in der Konsole an, um Gegenstände aus 
        diesem Objekt auszuwählen und zu entnehmen.

        Der Spieler sieht eine nummerierte Liste aller enthaltenen Items 
        plus einer Option zum Abbrechen. Bei einer gültigen Wahl wird 
        das Item aus dem Inventar des Objekts entfernt und zurückgegeben.

        Returns:
            Item: Das gewählte Item-Objekt, wenn die Wahl gültig war.
            None: Wenn der Vorgang abgebrochen wurde oder die Eingabe ungültig war.
        """
        # Falls das Objekt leer ist, brauchen wir kein Menü anzeigen
        if not self.items:
            return None

        print("\nFolgende Items befinden sich hier:")
        # enumerate erstellt ein Paar aus (Index, Inhalt), z.B. (0, "Schlüssel")
        for idx, item in enumerate(self.items):
            print(f"[{idx}] {item.name}")
        
        # Die Zahl für "Abbrechen" ist immer die nächste freie Nummer
        print(f"[{len(self.items)}] Abbrechen")
        
        choice = input("Was möchtest du mitnehmen? (Nummer eingeben): ").strip()
        
        # Validierung: Ist die Eingabe eine Zahl?
        if choice.isdigit():
            idx = int(choice)
            
            # Validierung: Liegt die Zahl im Bereich der Liste?
            if 0 <= idx < len(self.items):
                # .pop entfernt das Element an der Stelle 'idx' und gibt es zurück
                selected_item = self.items.pop(idx)
                print(f"Du hast '{selected_item.name}' eingesteckt.")
                return [selected_item]
        
        # Fallback, wenn nichts ausgewählt wurde
        print("Du nimmst nichts mit.")
        return None