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

class Fluchtwagen(Room):
    def __init__(self):
        super().__init__(
            name="Fluchtwagen", 
            description="Deine Mates haben dich abgeholt und du musst das  Passwort für den root login über dein Funkgerät versenden. Nutze Verschlüsselung der Schlüssel steht in deinem Notizbuchf"
        )
        
        # Wir erstellen eine Notiz mit einem Hinweis

        self.interactables.update({
            "funkgerät": Funkgerät(
                name="HydraHide Funkgerät", 
                binary_message="0x66 0x88 0x44 0x99 (Unverschlüsselte Nachricht)", 
                answer="0x65 0x8B 0x47 0x9A"
            ),
        })



    def exit(self, state: "GameState") -> bool:
        if self.interactables["funkgerät"].solved == True:
            print(f"{Fore.GREEN}Du hast den Code richtig verschlüsselt. Deine Mates sind stolz auf dich.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Falscher Zugangscode! Du kannst den Serverraum nicht betreten.{Style.RESET_ALL}")
            return False