from template.room import Room

class Arbeitszimmer(Room):
    
    def __init__(self):
        super().__init__(name="Arbeitszimmer", description="Ein leeres Arbeitszimmer mit keinem Inhalt")
        self.interactables.update({
        })
        
    def exit(self, items)->bool:
        print("Du hast es geschafft")
        return True