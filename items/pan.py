from template.item import Item, ItemProperties, ItemType
from core.equipment import EquipmentSlot
from typing import List, Optional, TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState

class Pan(Item):
    def __init__(self, contents: Optional[List[Item]] = None):
        super().__init__(
            name="Pfanne", 
            description="Eine große schwarze Pfanne mit eingebrannten Essensresten.",
            properties=ItemProperties(
                item_type=ItemType.QUEST,
                equippable=True,
                stackable=False,
                interactable=True,
            ),
            slot=EquipmentSlot.MAIN_HAND
        )
        # Fix: Erstelle eine neue Liste, falls keine übergeben wurde
        self.contents: List[Item] = contents if contents is not None else []

    def interact(self, state: 'GameState'):
        print(f"\n{Style.BRIGHT}{Fore.CYAN}--- {self.name} Management ---{Style.RESET_ALL}")
        
        # 1. Inhalt anzeigen
        if self.contents:
            contained_names = ", ".join([f"{Fore.GREEN}{item.name}{Style.RESET_ALL}" for item in self.contents])
            print(f"Aktueller Inhalt: {contained_names}")
        else:
            print("Die Pfanne ist momentan leer.")

        # 2. Menü für den Spieler
        print(f"\nWas möchtest du tun?")
        print(f"{Fore.YELLOW}[1]{Style.RESET_ALL} Zutaten hinzufügen")
        print(f"{Fore.YELLOW}[2]{Style.RESET_ALL} Pfanne ausleeren (Items gehen verloren)")
        print(f"{Fore.YELLOW}[3]{Style.RESET_ALL} Nichts tun")
        
        choice = input(f"{Fore.CYAN}Auswahl >> {Style.RESET_ALL}").strip()

        if choice == "1":
            self._add_ingredients(state)
        elif choice == "2":
            self.clear_pan()
            print(f"{Fore.RED}Du hast die Pfanne ausgekippt.{Style.RESET_ALL}")
        else:
            print("Du steckst die Pfanne wieder weg.")

    def _add_ingredients(self, state: 'GameState'):
        print("\nWelche Zutaten möchtest du hineinlegen?")
        # Nutzt dein vorhandenes Inventar-Menü
        new_items = state.player.inventory.open()
        
        if new_items:
            # Hier filtern wir die Pfanne selbst aus, damit man sie nicht in sich selbst legen kann!
            valid_items = [item for item in new_items if item is not self]
            self.contents.extend(valid_items)
            
            if len(valid_items) < len(new_items):
                print(f"{Fore.YELLOW}Hinweis: Du kannst die Pfanne nicht in sich selbst legen!{Style.RESET_ALL}")
            
            print(f"{Fore.GREEN}Erfolgreich hinzugefügt: {', '.join([i.name for i in valid_items])}{Style.RESET_ALL}")
        else:
            print("Keine Zutaten hinzugefügt.")

    def clear_pan(self):
        """Leert die Pfanne."""
        self.contents.clear()