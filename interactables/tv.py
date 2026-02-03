from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from typing import List

class Television(Interactable):
    
    def __init__(self, hint: str = "", channels: List[str]=None):
        """Ein Fernseher, der verschiedene Kanäle und Informationen anzeigen kann."""
        super().__init__(
            name="Fernseher",
            description="Ein alter Röhrenfernseher mit einer staubigen Bildfläche.",
            locked=False
        )
        self.is_on = False
        self.current_channel = 0
        self.hint = hint
        self.channels = channels or [
            "Rauschen...",
            f"Hinweis: {hint}",
            "Werbung für Nuka-Cola."
        ]

    def use(self, state: GameState):
        """Schaltet den Fernseher ein/aus oder wechselt den Kanal."""
        if not self.is_on:
            self.is_on = True
            print(f"{Fore.BLUE}*Klick* Der Fernseher summt leise und das Bild flackert auf.{Style.RESET_ALL}")
            self._display_current_program()
        else:
            choice = input("Möchtest du [1] Kanal wechseln oder [2] Ausschalten? ").strip()
            if choice == "1":
                self.current_channel = (self.current_channel + 1) % len(self.channels)
                self._display_current_program()
            else:
                self.is_on = False
                print(f"{Fore.BLACK}Der Bildschirm wird schwarz.{Style.RESET_ALL}")

    def _display_current_program(self):
        """Interne Methode zur Anzeige des aktuellen Programms."""
        print(f"\n{Fore.YELLOW}Kanal {self.current_channel}:{Style.RESET_ALL}")
        print(f"» {self.channels[self.current_channel]} «")

    def inspect(self):
        """Untersucht den Fernseher genauer."""
        # Erst die Standard-Beschreibung der Basisklasse
        super().inspect()
        
        if self.is_on:
            print("Der Fernseher läuft gerade. Das Licht des Bildschirms spiegelt sich in deinen Augen.")
        else:
            print("Der Bildschirm ist dunkel. Du kannst dein eigenes verzerrtes Spiegelbild im Glas sehen.")
        
        if self.hint and not self.is_on:
            print("Am Gehäuse klebt ein kleiner Zettel, aber du kannst ihn im Dunkeln nicht lesen. Vielleicht solltest du ihn einschalten?")