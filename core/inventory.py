from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from template.item import Item


class Inventory:
    def __init__(self):
        self.items: List["Item"] = []

    def add(self, item: List["Item"]):
        self.items.extend(item)

    def open(self) -> List['Item']:
        if not self.items:
            print("Dein Inventar ist leer.")
            return []

        print("Du hast folgende Items im Inventar. Wähle die Nummern aus (getrennt durch Komma):")
        for idx, obj in enumerate(self.items):
            print(f"[{idx}] - {obj.name}")

        selection_raw = input("Auswahl (z.B. 0,2): ")
        
        selected_items = []
        # Indizes aus dem String extrahieren und säubern
        indices = [s.strip() for s in selection_raw.split(",") if s.strip().isdigit()]

        for idx_str in indices:
            idx = int(idx_str)
            if 0 <= idx < len(self.items):
                item = self.items[idx]
                selected_items.append(item)
            else:
                print(f"Ungültiger Index: {idx}")

        # Ausgewählte Items aus dem Inventar entfernen
        for item in selected_items:
            self.items.remove(item)

        return selected_items
        
    
    def remove_by_name(self, name: str):
        # Option 1: Using a loop and remove()
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break  # Stop after finding the first match to avoid index errors

    def remove_by_object(self, item: "Item"):
        self.items.remove(item)

    def has_item(self, item_name: "Item"):
        """Prüft, ob ein Item anhand seines Namens im Inventar ist."""
        for item in self.items:
            if item.name.lower() == item_name.name.lower():
                return True
        return False
