from template.item import Item

class Bananenschale(Item):
    
    def __init__(self, data: str = ""):
        """Ein einfaches Bananenschalen-Item, das zum Entriegeln von Bananen oder Bananen verwendet werden kann.
        @param data: Die auf der Bananeschalen gespeicherten Daten (z. B. ein Zugriffscode)."""
        super().__init__(
            name="Bananenschale", 
            description="Eine Plastik-Bananenschale mit einem Magnetstreifen. Es sieht so aus, als könnte sie zum Entriegeln elektronischer Schlösser verwendet werden.",
        )
        self.data: str = data

