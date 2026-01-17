from template.room import Room

class Arbeitszimmer(Room):
    
    def __init__(self):
        super().__init__()
        self.interactables.update({
            
        })
        
    def exit(self, items)->bool:
        print("Du hast es geschafft")
        return True