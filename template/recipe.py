from template.item import Item
from typing import List

class Recipe:
    def __init__(self, ingredients: List[Item], result_item: Item):
        # Wir sortieren nach dem Namen der Klasse, damit der Vergleich stabil ist
        self.ingredients = sorted([item.name.strip().lower() for item in ingredients])
        self.result_item = result_item