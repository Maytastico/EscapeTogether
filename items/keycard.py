from template.item import Item

class Keycard(Item):
    
    def __init__(self, data: str = ""):
        """Ein einfaches Keycard-Item, das zum Entriegeln von Türen oder Schränken verwendet werden kann.
        @param data: Die auf der Keycard gespeicherten Daten (z. B. ein Zugriffscode)."""
        super().__init__(
            name="Keycard", 
            description="Eine Plastik-Keycard mit einem Magnetstreifen. Es sieht so aus, als könnte sie zum Entriegeln elektronischer Schlösser verwendet werden."
        )
        self.data: str = data
