from abc import ABC, abstractmethod
from colorama import Style, Fore

class Room(ABC):
   
    def __init__(self):
        """
        Abstrakte Basisklasse für einen Raum im Escape-Game.
        Jeder Raum enthält interaktive Objekte und definiert Methoden zum Betreten,
        Verlassen, Untersuchen und Benutzen von Objekten.
        """ 
        # Objekte werden in der Unterklasse mit self.interactables.update({...}) spezifiziert
        self.interactables: dict[str, object] = {}
    
    def enter(self):
        """Logik beim Betreten des Raums. Zeigt die Objekte im Raum an.
        Wird aufgerufen, wenn der Raum gewechselt oder betreten wird."""
        print("Du befindest dich im Raum. Du siehst:")
        for item in self.interactables:
            print(f"- {str(item)}")
    
    @abstractmethod
    def exit(self, token: list|str) -> bool:
        """Logik zum Verlassen des Raums. Gibt True zurück, wenn das Verlassen erfolgreich ist, andernfalls False.
        Herbei kann der token der zum Verlassen benötigt wird übergeben werden, dieser ist entweder eine Liste von Items oder ein Passwort.
        @param token: Liste von Items oder ein Passwort, das zum Verlassen des Raums benötigt wird.
        @return: True, wenn der Raum erfolgreich verlassen werden kann, sonst False.
        """
        pass
    
    def inspect(self, item_name: str=None):
        """Untersuche den Raum oder ein spezifisches Objekt."""
        if item_name is None:
            print("Du siehst verschiedene Objekte im Raum:")
            for name in self.interactables:
                print(f"- {name.capitalize()}")
        else:
            target = self.interactables.get(item_name.lower())
            if target:
                target.inspect()
            else:
                print(f"Hier gibt es kein Objekt namens '{item_name}'.")
                
    def use_interactable(self, item_name: str) -> list:
        """Benutze ein spezifisches Objekt im Raum."""
        item = self.interactables.get(item_name.lower())
        
        if item:
            return item.use()
        else:
            print(f"Kein Objekt namens '{item_name}' im Labor gefunden.")
        
    def help(self):
        """Zeigt Hilfe-Informationen zu den verfügbaren Befehlen im Raum an."""
        print("Verfügbare Befehle: use, exit, inspect, help, inventory")
        print(f"{Style.BRIGHT}{Fore.BLUE}use{Style.RESET_ALL} - Interagiere mit einem Objekt im Raum")   
        print(f"{Style.BRIGHT}{Fore.BLUE}exit{Style.RESET_ALL} - Verlasse den Raum (erfordert ggf. Items oder ein Passwort)")
        print(f"{Style.BRIGHT}{Fore.BLUE}inspect{Style.RESET_ALL} - Sieh dich im Raum um oder betrachte ein Objekt genau")
        print(f"{Style.BRIGHT}{Fore.BLUE}inventory{Style.RESET_ALL} - Zeigt die Gegenstände an, die du bei dir trägst")
        print(f"{Style.BRIGHT}{Fore.RED}jump{Style.RESET_ALL} - Wechsle zu einem anderen Raum (nur zum Testen)")