from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from template.item import Item


class Inventory:
    def __init__(self):
        self.items: List[Item] = []

    def add(self, item: List[Item]):
        self.items.extend(item)
    
    def remove_by_name(self, name: str):
        # Option 1: Using a loop and remove()
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break  # Stop after finding the first match to avoid index errors

    def remove_by_object(self, item: Item):
        self.items.remove(item)
