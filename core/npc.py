
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.player import Player
    from types.behaviour import Behaviour
    from typing import List
    

class NPC(Player):

    def __init__(self, name: str = "", behaviour: "Behaviour"= None):
        super().__init__(name)
        self.behaviour = behaviour
        

    def conversation(self):
        if self.behaviour is None:
            print("Keine Konversation verfügbar.")
            return
        
        print(f"{self.behaviour.text}")
        print("Du beginnst ein Gespräch mit dem NPC.")
        while self.behaviour is not None:
            for key, action in enumerate(self.behaviour.actions):
                print(f" {key}: {action.text}")
            print("Wähle q um das Gespräch zu beenden.")
            choice = input("Wähle eine Aktion: ")
            if choice.isdigit() and 0 <= int(choice) < len(self.behaviour.actions):
                self.behaviour = self.behaviour.act(int(choice))    
            if choice.lower() == 'q':
                print("Das Gespräch wurde beendet.")
                break
            else:
                print("Ungültige Auswahl.")
