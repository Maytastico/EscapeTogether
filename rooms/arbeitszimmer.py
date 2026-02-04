from typing import TYPE_CHECKING
from template.room import Room
from interactables.radio import Radio
from interactables.table import Table
from interactables.whiteboard import Whiteboard
from items.note import Note
from items.crowbar import Crowbar
from colorama import Fore, Style
from items.notebook import Notebook


if TYPE_CHECKING:
    from core.gamestate import GameState

class Arbeitszimmer(Room):
    def __init__(self):
        super().__init__(
            name="Arbeitszimmer", 
            description="Ein staubiges Zimmer mit einem massiven Eichentisch. Das Licht flackert unheimlich."
        )
        
        # Wir erstellen eine Notiz mit einem Hinweis
        hinweis_notiz = Note(
            name="Zettel",
            content="Der Techniker meinte, unter dem Tisch klebt etwas... für Notfälle."
        )

        

        self.interactables.update({
            "tisch": Table(items=[hinweis_notiz]),
            "radio": Radio(), # Vielleicht spielt es nur statisches Rauschen?
            "whiteboard": Whiteboard(), # Hier könnten alte Skizzen drauf sein
            "bodenplatte": Table(name="Lose Bodenplatte", items=[
                Crowbar(), 
                Notebook(["Hi my name is jeff", "When I saw you I fell in love", "What is the purpose of life"])
            ]) # Versteckt
        })

    def exit(self, state: GameState) -> bool:
        """
        Man kommt nur raus, wenn man das Brecheisen (Crowbar) hat, 
        um die verklemmte Tür aufzuhebeln.
        """
        has_crowbar = any(isinstance(i, Crowbar) for i in state.player.inventory.items)
        
        if has_crowbar:
            print(f"{Fore.GREEN}Mit dem Brecheisen hebelst du die schwere Stahltür zum Labor auf!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Die Tür klemmt total. Mit bloßen Händen kriegst du die nicht auf.{Style.RESET_ALL}")
            print("Vielleicht liegt hier irgendwo ein Werkzeug rum?")
            return False