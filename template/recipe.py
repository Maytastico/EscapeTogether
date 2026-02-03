from template.item import Item
from typing import List

class Recipe:
    def __init__(self, ingredients: List[str], result_item: 'Item'):
        self.ingredients = sorted(ingredients) # Sortieren für leichteren Vergleich
        self.result_item = result_item