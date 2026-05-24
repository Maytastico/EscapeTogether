from template.disk import Disk
from colorama import *
from core.gamestate import GameState
from items.bananenschale import Bananenschale

class BananenDisk(Disk): # "Banane" auf Deutsch

    def __init__(self):
        super().__init__(
            name="Bananen Disk"
            # sehr effektiv
        )
    def interact(self, state: "GameState"):
        super().interact(state)
        
    def play(self):
        print(f"""
        .-.
       /  |
      |  /
   .'\|.-; _
  /.-.;\  |\|
  '   |'._/ `
      |  \ 
       \  |
        '-'
ASCII Art made by Joan G. Stark :)
""")