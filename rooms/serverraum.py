from typing import TYPE_CHECKING
from interactables.funkgerät import Funkgerät
from interactables.terminal import Terminal
from template.room import Room
from interactables.radio import Radio
from interactables.table import Table
from interactables.whiteboard import Whiteboard
from items.note import Note
from items.crowbar import Crowbar
from colorama import Fore, Style
from items.notebook import Notebook
from interactables.cabinet import Cabinet


if TYPE_CHECKING:
    from core.gamestate import GameState

class Serverraum(Room):
    def __init__(self):
        super().__init__(
            name="Serverraum", 
            description="Okay das dreistellige Passwort war ja sehr einfach, das hätte ich von dem aber nicht erwartet. Du siehst mehrere Server in dem Raum. Frage bei deinen Kollegen nach welchen Server du hacken musst. Schaue in dein Notizbuch, dort findest du die Hinweise."
        )
        
        # Wir erstellen eine Notiz mit einem Hinweis

       

        rote_hinweis_notiz = Note(
                    name="Klebezettel",
                    content="Das Passwort für das Terminal ist in Dezimalform"
                )

        klebe_hinweis_notiz = Note(
            name="Gelber Klebezettel",
            content="Das Terminal Passwort findest du bei den 3D Druckern."
        )

        self.interactables.update({
            "tisch": Table(items=[rote_hinweis_notiz, klebe_hinweis_notiz]),
            "funkgerät": Funkgerät(name="HydraHide Funkgerät", binary_message="0100 1011 0000 (Verschlüsselte Nachricht)", answer="783"),
            "terminal": Terminal( content={
                "/etc/log/surveillance.log": "vsh (hex) Ausgang",
                "/root/password.txt": "0x66 0x88 0x44 0x99."
            },
            files={
                "/": ["/etc", "/root"],
                "/etc": ["/etc/log"],
                "/etc/log": ["surveillance.log"],
                "/root": ["password.txt"],
                "/opt": ["mc", "surveillance"],
            })
        })


    def init_state(self, state: "GameState"):
         state.get_player().inventory.add([Notebook([
                    "Die Verbindung mit dem Funkgerät ist verschlüsselt nutze XOR um die Nachricht zu entschlüsseln und zu verschlüsseln.", 
                    "Der Schlüssel ist 0000 0011 (0x03)", 
                    "Wende den Schlüssel auf die Nachricht an um das Passwort zu erhalten.", 
                    "Bei dem Terminal musst die ersten 0011 verwenden um die Nachricht zu entschlüsseln.",
                    "Du brauchst das Root passwort des Servers, damit deine Kollegen die Datenbank hacken können. Das Passwort ist in Binärform und muss in Dezimalform eingegeben werden."
                ])])
                

    def exit(self, state: "GameState") -> bool:
        input_code = input("Gib den Zugangscode in HEX-Code ein, um zu verschwinden: ").strip()
        if input_code == "0x56 0x53 0x48":
            print(f"{Fore.GREEN}Der Zugangscode ist korrekt! Du bist draußen an der frischen Luft.{Style.RESET_ALL}")
            return True
        elif input_code == "1234":
            print(f"{Fore.RED}Oh Junge da hab ich dich aber hops genommen lol{Style.RESET_ALL}")
            return False
        else:
            print(f"{Fore.RED}Falscher Zugangscode! Du kannst den Serverraum nicht betreten.{Style.RESET_ALL}")
            return False