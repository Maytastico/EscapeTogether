from abc import ABC, abstractmethod
from colorama import Style, Fore
from typing import TYPE_CHECKING, Dict, Optional, Any

# Dies ist nur für die Autovervollständigung beim Programmieren wichtig
if TYPE_CHECKING:
    from core.gamestate import GameState

class Room(ABC):
    """
    Stell dir einen 'Room' wie eine Kulisse in einem Film vor.
    Jeder Raum hat Dinge, die darin herumstehen (Interactables) und
    Regeln, wie man ihn wieder verlassen kann.
    """
   
    def __init__(self, name: str, description: str):
        # Das 'interactables'-Wörterbuch ist wie ein Inhaltsverzeichnis des Raums.
        # Es speichert: "Name des Objekts": Das Objekt selbst.
        self.interactables: Dict[str, Any] = {}
        self.name: str = name
        self.description: str = description

    
    def enter(self):
        """
        Wird automatisch aufgerufen, wenn der Spieler den Raum betritt.
        Gibt dem Spieler einen ersten Überblick, was er sehen kann.
        """
        print(f"\n{Fore.GREEN}--- {self.name} betreten ---{Style.RESET_ALL}")
        print(self.description)
        print("Du blickst dich um und siehst folgende Dinge:")
        
        # Wir gehen die Liste der Namen im Wörterbuch durch
        for name in self.interactables:
            print(f"- {name.capitalize()}")
    
    @abstractmethod
    def exit(self, state: 'GameState') -> bool:
        """
        Dies ist ein 'Bauplan-Teil'. Jeder Raum muss selbst entscheiden, 
        ob der Spieler gehen darf (z.B. ob die Tür abgeschlossen ist).
        
        Args:
            state: Das Gedächtnis des Spiels (Hat der Spieler den Schlüssel?).
        Returns:
            True (Spieler darf gehen) oder False (Spieler bleibt im Raum).
        """
        pass
    
    def inspect(self, item_name: Optional[str] = None):
        """
        Lässt den Spieler den Raum oder ein Ding darin genau untersuchen.
        
        Args:
            item_name: Der Name des Dinges. Wenn leer, wird der ganze Raum beschrieben.
        """
        if item_name is None:
            # Der Spieler hat nur "inspect" eingegeben, ohne ein Ziel.
            print("Du schaust dich allgemein im Raum um.")
            self.enter() # Zeigt einfach nochmal die Liste der Objekte
        else:
            # Wir suchen das Objekt. .lower() sorgt dafür, dass 'Safe' und 'safe' beides klappt.
            target = self.interactables.get(item_name.lower())
            if target:
                # Wir sagen dem Objekt: 'Beschreibe dich mal selbst!'
                target.inspect()
            else:
                print(f"Hier gibt es nichts namens '{item_name}', das du untersuchen kannst.")
                
    def use_interactable(self, item_name: str, state: 'GameState') -> Any:
        """
        Wird aufgerufen, wenn der Spieler 'use [Objekt]' tippt.
        Versucht, die 'Benutzen'-Funktion des Objekts zu starten.
        """
        target = self.interactables.get(item_name.lower())
        
        if target:
            # Führt die Aktion des Objekts aus (z.B. Tresor öffnen)
            return target.use(state)
        else:
            print(f"Du versuchst '{item_name}' zu benutzen, aber das Item ist nicht hier.")
        
    def help(self):
        """
        Ein kleiner Spickzettel für den Spieler, falls man nicht weiterweiß.
        """
        print(f"\n{Fore.YELLOW}--- WAS KANN ICH TUN? ---{Style.RESET_ALL}")
        print(f"{Fore.BLUE}inspect [Name]{Style.RESET_ALL} - Schau dir etwas genau an")
        print(f"{Fore.BLUE}use [Name]{Style.RESET_ALL}     - Benutze ein Gerät oder öffne etwas")   
        print(f"{Fore.BLUE}inventory{Style.RESET_ALL}      - Schau in deine Taschen")
        print(f"{Fore.BLUE}exit{Style.RESET_ALL}           - Versuche, zum nächsten Raum zu gehen")
        print(f"{Fore.RED}jump{Style.RESET_ALL}           - Springt zum nächten Raum (Debug Mode)")