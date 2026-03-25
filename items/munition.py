from template.item import Item

class Munition(Item):

    def __init__(self, data: str = ""):
        """ein magazin mit 20 patronen für ein sturmgewehr"""
        super().__init__(
            name="sturmgewehr magazin",
            description="ein magazin mit 20 patronen für ein sturmgewehr"
        )
        self.data: str = data
