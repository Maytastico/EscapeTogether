from template.item import Item

class Bananenschale(Item):
    
   def __init__(self, data: str = ""):
    super().__init__(
      name="Bananenschale",
      description="Die Leiche einer Banane"
    )
    self.data: str = data
