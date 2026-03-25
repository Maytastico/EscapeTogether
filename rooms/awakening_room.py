from template.room import Room
from interactables.tisch import Tisch
from items.dolch import Dolch
from items.munition import Munition


class Aufwachraum(Room):
       def __init__(self):
         """du öffnest deine augen und siehst setzt dich auf 
     und siehst das du in einem bett einer krankenstation liegst"""
           # Objekte werden in der Unterklasse mit self.interactables.update({...}) spezifiziert
         self.interactables.update(
              "Tisch", item=[Dolch(),Munition(),Munition()]
              )
      
         def exit(self, items)->bool:
           print("Du hast es geschafft")
         return True