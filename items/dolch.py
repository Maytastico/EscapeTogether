from template.item import Item

class Dolch(Item):
    
   def __init__(self, data: str = ""):
    """eine nahkampfwaffe effektiv bei attacken von hinten 30dmg oft genutzt für attentate"""
    super().__init__(
      name="weak dagger",
      description="kurze waffe mit 30 durrability und 30 dmg"
    )
    self.data: str = data
