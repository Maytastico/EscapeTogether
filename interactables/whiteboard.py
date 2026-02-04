from template.interactable import Interactable
from core.gamestate import GameState

class Whiteboard(Interactable):
    
    def __init__(self, hint: str = "", content: str = ""):
        """Bietet ein interaktives Whiteboard an, auf dem Benutzer ihre Unterschrift hinterlassen können.
        Zudem können Hinweise darauf gezeichnet werden.
        """
        super().__init__(
            name="Schrank",
            description="Eine robuste Metallbox mit einem Tastenfeldschloss.",
        )
        self.content = ""
        self.hint = hint
    
    def use(self, state: GameState):
        """Ermöglicht es dem Benutzer, seine Unterschrift auf das Whiteboard zu schreiben."""
        self.content = input("Setze deine Unterschrift auf das Whiteboard: ").strip()
        print(f"Du schreibst '{self.content}' mit einem Marker auf das Whiteboard.")
    
    def inspect(self):
        """Untersuche das Whiteboard, um dessen Inhalt und Hinweise zu sehen.
        Wenn kein spezieller Hinweis vorhanden ist, wird eine Standardbeschreibung angezeigt.
        """
        if self.content != "" :
            print(f"Jemand hat '{self.content}' darauf geschrieben.")
        
        if self.hint != "":
            print(f"Hinweis: {self.hint}")
        else:
            print("Auf dem Whiteboard sind verschiedene wissenschaftliche Formeln und Diagramme gezeichnet.")