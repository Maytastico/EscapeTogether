from template.item import Item

class Notizbuch(Item):
    def __init__(self):
        super().__init__(
            name="Notizbuch",
            description="Ein altes Notizbuch mit handschriftlichen Notizen."
        )
    
    def inspect(self):
        print("Das Notizbuch enthält verschiedene kryptische Notizen und Skizzen.")
    