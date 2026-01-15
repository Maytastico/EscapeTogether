from template.interactable import Interactable

class Cabinet(Interactable):
    
    def __init__(self, code: str, items: list = None):
        """Bietet einen interaktiven Schrank, der mit einem Tastenfeld-Code verschlossen ist.
        @param code: Der Tastenfeld-Code, der zum Öffnen des Schranks benötigt wird.
        @param items: Eine Liste von Gegenständen im Schrank, die beim Öffnen zurückgegeben wird."""
        self.locked = True
        self.items = items if items is not None else []
        self.code = code
    
    def use(self) -> list:
        """Fragt nach dem Tastenfeld-Code, um den Schrank zu öffnen.
        Bei korrektem Code werden die Gegenstände im Schrank zurückgegeben,
        andernfalls wird mitgeteilt, dass der Schrank verschlossen ist."""
        code = input("Tastenfeld-Code eingeben: ").strip()
        if code == self.code:
            print("Du öffnest den Schrank. Darin findest du:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")
            self.locked = False
            return self.items
        else:
            print("Der Schrank ist verschlossen. Du brauchst den richtigen Code, um ihn zu öffnen.")
    
    def inspect(self):
        """Untersucht den Schrank und zeigt seine Beschreibung an."""
        print("Der Schrank ist eine robuste Metallbox mit einem Tastenfeldschloss an der Vorderseite.")
