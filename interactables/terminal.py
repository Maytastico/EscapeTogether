from template.interactable import Interactable
from colorama import Fore, Style

class Terminal(Interactable):

    def __init__(self, path="/", files:dict=None, content:dict=None):
        """Ein einfacher Terminal-Simulator mit Basisbefehlen wie ls, cd, pwd und cat.
        @param path: Der aktuelle Verzeichnispfad, in dem sich der Benutzer befindet.
        @param files: Ein Dictionary, das die Dateistruktur darstellt. Schlüssel sind Pfade,
                      Werte sind Listen von Dateien/Verzeichnissen in diesen Pfaden.
        @param content: Ein Dictionary für Dateiinhalte. Schlüssel sind Dateipfade,
                        Werte sind die Inhalte dieser Dateien.
        @example:
            files = {
                "/": ["/home", "/var", "/etc"],
                "/home": ["/user", "/documents", "notiz"],
                "/var": ["/log", "/tmp"],
                "/etc": ["konfig.cfg", "hosts"],
            }
            content = {
                "/etc/konfig.cfg": "schrank_code=4267 # Der Code für den Schrank",
                "/home/notiz": "Denk daran, die Server-Logs auf Anomalien zu prüfen.\nDie Keycard für den Ausgang ist im Schrank.\nIch nutze übrigens Arch (I use Arch btw).\nDer Schrank-Code wird über dieses Terminal konfiguriert.",
                "/etc/hosts": "ad.com" 
                }
        """
        
        self.path:str = path
        self.files:dict = files if files is not None else {}
        self.content:dict = content if content is not None else {}
        
    def _process_command(self, cmd:str):
        """Verarbeitet einen einzelnen vom Benutzer eingegebenen Befehl. 
        Unterstützte Befehle: ls, cd, pwd, cat, help.
        @param cmd: Der vom Benutzer eingegebene Befehl-String.
        """
        command = cmd.split(" ")
        if command[0] == "help":
            self.help()
        elif command[0] == "ls":
            if self.path in self.files:
                for item in self.files[self.path]:
                    print(item)
            else:
                print("Keine Dateien gefunden.")
        elif command[0] == "cd":
            if len(command) > 1:
                if command[1] == "..":
                    self.path = "/"
                elif command[1] in self.files:
                    self.path = command[1]
                else:
                    print("Verzeichnis nicht gefunden.")
            else:
                print("Verwendung: cd <verzeichnis>")
        elif command[0] == "pwd":
            print(self.path if self.path else "/")
        elif command[0] == "cat":
            if len(command) > 1:
                file_to_open = f"{self.path}/{command[1]}"
                if file_to_open in self.content:
                    print(f"{Style.RESET_ALL}{self.content[file_to_open]}")
                else:
                    print("Datei nicht gefunden.")
            else:
                print("Verwendung: cat <datei>")
        print(Style.RESET_ALL)
    
    def use(self):
        """Simuliert die Nutzung des Terminals. Bietet eine Befehlszeile zur Interaktion an.
        Unterstützte Befehle: ls, cd, pwd, cat, help, exit.
        Nutzt eine Schleife, bis 'exit' eingegeben wird.
        """
        print("\n\nTerminal wird gestartet...")
        print("Um das Terminal zu verlassen, gib 'exit' ein.")
        print("Willkommen bei Sci-tech Unix")
        self.help()
        while True:
            print(Style.BRIGHT + Fore.GREEN)
            cmd = input(f"user@scitech:{self.path}$ ").strip().split(" ")
            command = cmd[0]
            if command == "exit":
                print("Terminal wird beendet...")
                print(Style.RESET_ALL)
                break
            elif command == "":
                continue
            else:
                self._process_command(" ".join(cmd))
        
    def help(self):
        """Zeigt Hilfe-Informationen zu den verfügbaren Befehlen an."""
        print("Verfügbare Befehle: ls, cd, pwd, cat, help")
        print(f"{Style.BRIGHT}{Fore.BLUE}cat{Style.RESET_ALL} - Zeigt den Inhalt einer Datei an")
        print(f"{Style.BRIGHT}{Fore.BLUE}ls{Style.RESET_ALL} - Listet alle Dateien im aktuellen Verzeichnis auf")
        print(f"{Style.BRIGHT}{Fore.BLUE}cd{Style.RESET_ALL} - Wechselt das Verzeichnis")
        print(f"{Style.BRIGHT}{Fore.BLUE}pwd{Style.RESET_ALL} - Zeigt den aktuellen Pfad an")
        
    def inspect(self):
        """Untersuche das Terminal (gemäß Interactable-Interface)."""
        print("Das Terminal ist ein High-Tech-Gerät mit einem leuchtenden Bildschirm und einer Tastatur.")
        print("Auf dem Gehäuse klebt ein Sticker mit der Aufschrift 'I use Arch btw.'.")