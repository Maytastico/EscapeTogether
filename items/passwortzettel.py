from template.item import Item, ItemProperties

class Passwortzettel(Item):
    
    def __init__(self, data: str = ""):
        super().__init__(
            name="Passwortzettel", 
            description="Zettel mit Passwörtern"
        )
        
        self.data: str = data

    def interact(self, state):
        print(
"""
 ____________
|            |
| PASSWÖRTER |
|            |
| Laptop:    |
| █████████  |
| PC:        |
| b4Nan3!    |
|____________|
"""
        )