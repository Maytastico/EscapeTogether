from core.inventory import Inventory

class Player:

    def __init__(self, name: str=""):
        self.name: str = name
        self.inventory: Inventory = Inventory()