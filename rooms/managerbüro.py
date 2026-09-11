from typing import TYPE_CHECKING
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

class Managerbüro(Room):
    def __init__(self):
        super().__init__(
            name="Managerbüro", 
            description="Es ist nacht und du bistin das Büro des Geheimdienstmanagers eingebrochen und suchst nach dem Zugangcode in den Geheimen Serverraum. "
        )
        
        # Wir erstellen eine Notiz mit einem Hinweis
        hinweis_notiz = Note(
            name="Merkzettel",
            content="Ich muss noch Milch und Brot kaufen, bevor ich nach Hause gehe. Ach ja, und der Zugangscode für den Serverraum ist 1234. Das Passwort musst du in dezimaler Form eingeben, nicht in binärer Form."
        )

        rote_hinweis_notiz = Note(
            name="Roter Merkzettel",
            content="1000 1001 0101 0010 (binär)"
        )

        self.interactables.update({
            "tisch": Table(items=[hinweis_notiz, rote_hinweis_notiz]),
            "radio": Radio(initial_stations={100: "Wunderschönen Guten Abend und ein herzliches Willkommen zu unserem Techno Dienstag", 120: "zzzzzzzZZZzzzzZZ"}),
            "whiteboard": Whiteboard(hint="Der Zugangscode ist nicht 1234. Der Exitcode ist in der realen Welt Wach auf Neo"), # Hier könnten alte Skizzen drauf sein
            "tresor": Cabinet(name="Tresor", code="8952", items=[Note("Zettel im Tresor", "Das Passwort findest du bei einem Legendäre Gerät, welches Generationen verbindet und zum Spielen dient. ")]), # Versteckt
            "bodenplatte": Table(name="Lose Bodenplatte", items=[
                Crowbar(), 
                Notebook(["Hi my name is jeff", "When I saw you I fell in love", "What is the purpose of life"])
            ]), # Versteckt
        })

                

    def exit(self, state: "GameState") -> bool:
        input_code = input("Gib den Zugangscode in ASCII-Code ein, um den Serverraum zu betreten: ").strip()
        if input_code == "wii":
            print(f"{Fore.GREEN}Der Zugangscode ist korrekt! Du betrittst den geheimen Serverraum.{Style.RESET_ALL}")
            return True
        elif input_code == "1234":
            print(f"{Fore.RED}Oh Junge da hab ich dich aber hops genommen lol{Style.RESET_ALL}")
            return False
        else:
            print(f"{Fore.RED}Falscher Zugangscode! Du kannst den Serverraum nicht betreten.{Style.RESET_ALL}")
            return False