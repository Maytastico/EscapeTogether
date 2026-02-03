from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style
from typing import Dict, Optional

class Radio(Interactable):
    
    def __init__(self, initial_stations: Optional[Dict[float, str]] = None):
        """
        Ein Radio mit dynamischen Sendern.
        initial_stations: Ein Dictionary mit {Frequenz: "Nachricht"}
        """
        super().__init__(
            name="Radio",
            description="Ein altes Kofferradio. Die Frequenzskala ist handbeschriftet.",
            locked=False
        )
        self.is_on = False
        self.frequency = 88.0
        
        # Standard-Sender, falls keine mitgegeben werden
        self.stations = initial_stations if initial_stations is not None else {
            88.0: "Klassische Musik spielt leise vor sich hin."
        }

    def add_station(self, frequency: float, message: str):
        """Fügt einen neuen Sender hinzu oder überschreibt einen bestehenden."""
        self.stations[frequency] = message
        # Optional: Kleines Feedback für das Debugging oder Log
        # print(f"Sender auf {frequency} MHz hinzugefügt.")

    def use(self, state: GameState):
        if not self.is_on:
            self.is_on = True
            print(f"{Fore.YELLOW}*Knacks* Das Radio ist an.{Style.RESET_ALL}")
            self._play_current_station()
        else:
            print("\n[1] Frequenz wählen")
            print("[2] Ausschalten")
            choice = input("Wahl: ").strip()

            if choice == "1":
                self._tune_radio()
            else:
                self.is_on = False
                print("Stille.")

    def _tune_radio(self):
        val = input("Frequenz (MHz): ").strip()
        try:
            self.frequency = float(val)
            self._play_current_station()
        except ValueError:
            print("Der Regler klemmt.")

    def _play_current_station(self):
        content = self.stations.get(self.frequency, "Nur weißes Rauschen...")
        print(f"\n{Fore.CYAN}[FM {self.frequency} MHz]{Style.RESET_ALL}")
        print(f"» {content} «")