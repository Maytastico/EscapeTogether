from template.room import Room
from interactables.terminal import Terminal
from interactables.cabinet import Cabinet
from interactables.whiteboard import Whiteboard
from items.keycard import Keycard
from colorama import Fore, Style


class Labor(Room):

    def __init__(self):
        super().__init__()
        self.interactables.update(
            {
                "terminal": Terminal(
                    files={
                        "/": ["/home", "/var", "/etc"],
                        "/home": ["/user", "/dokumente", "notiz"],
                        "/var": ["/log", "/tmp"],
                        "/etc": ["konfig.cfg", "hosts"],
                    },
                    content={
                        "/etc/konfig.cfg": "schrank_code=4267 # Der Code für den Schrank",
                        "/home/notiz": "Denk daran, die Server-Logs auf Anomalien zu prüfen.\nDie Keycard für den Ausgang befindet sich im Schrank.\nIch nutze übrigens Arch (I use Arch btw).\nDer Schrank-Code wird über dieses Terminal konfiguriert.",
                        "/etc/hosts": "ad.com 0.0.0.0\ngoogle.de 0.0.0.0",
                    },
                ),
                "whiteboard": Whiteboard(),
                "cabinet": Cabinet(code="4267", items=[Keycard(data="Ausgangs-Keycard")]),
            }
        )

    def exit(self, items) -> bool:
        """Überprüft, ob der Benutzer die richtige Keycard besitzt, um das Labor zu verlassen."""
        for item in items:
            if isinstance(item, Keycard):
                if item.data == "Ausgangs-Keycard":
                    print("Du benutzt die Keycard, um die Tür zu entriegeln und das Labor zu verlassen.")
                    return True
                else:
                    print(f"{Fore.RED}Die Keycard scheint an dieser Tür nicht zu funktionieren.{Style.RESET_ALL}")
                    return False    
        
        # Falls keine Keycard in der Liste gefunden wurde
        print(f"{Fore.RED}Die Tür ist verschlossen. Du benötigst eine Keycard, um das Labor zu verlassen.{Style.RESET_ALL}")
        return False