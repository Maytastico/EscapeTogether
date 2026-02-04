from template.item import Item, ItemProperties, ItemType
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from core.gamestate import GameState

class Notebook(Item):
    def __init__(self, pages: List[str]):
        """
        Erstellt ein neues Notizbuch.

        Args:
            pages (list[str]): Liste mit Texten, wobei jeder Eintrag
                               eine Seite im Notizbuch darstellt
        """
        super().__init__(
            name="Notizheft",
            description="Ein einfaches Notizheft mit Informationen",
            properties=ItemProperties(
                item_type=ItemType.QUEST,
                interactable=True
            )
        )
        if not pages:
            raise ValueError("Notebook braucht mindestens eine Seite")

        # Alle Seiten des Notizbuchs
        self.pages = pages

        # Index der aktuell geöffneten Seite
        self.current_page = 0

    def interact(self, state: GameState):
        """
        Öffnet das Notizbuch und erlaubt dem Spieler,
        zwischen den Seiten zu wechseln.

        Steuerung:
        - 'a' = vorherige Seite
        - 'd' = nächste Seite
        - 'q' = Notizbuch schließen
        """
        while True:
            # Aktuelle Seite anzeigen
            self._render_page()

            # Benutzereingabe abfragen
            command = input(
                "\n[a] links | [d] rechts | [q] schließen: "
            ).lower()

            # Zur vorherigen Seite wechseln
            if command == "a":
                self._prev_page()

            # Zur nächsten Seite wechseln
            elif command == "d":
                self._next_page()

            # Notizbuch schließen
            elif command == "q":
                print("Du schließt das Notizbuch.")
                break

            # Ungültige Eingabe
            else:
                print("Unbekannte Eingabe.")

    def _render_page(self):
        """
        Gibt die aktuell ausgewählte Seite formatiert
        in der Konsole aus.
        """
        print("\n" + "=" * 40)
        print(f"📖 Seite {self.current_page + 1} / {len(self.pages)}")
        print("-" * 40)

        # Inhalt der aktuellen Seite anzeigen
        print(self.pages[self.current_page])

        print("=" * 40)

    def _next_page(self):
        """
        Wechselt zur nächsten Seite, falls möglich.
        """
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
        else:
            print("➡️ Letzte Seite erreicht.")

    def _prev_page(self):
        """
        Wechselt zur vorherigen Seite, falls möglich.
        """
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("⬅️ Erste Seite erreicht.")
