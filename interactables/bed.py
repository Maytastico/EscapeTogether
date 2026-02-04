from template.interactable import Interactable
from core.gamestate import GameState
from template.item import Item
from colorama import Fore, Style
from typing import List

class Bed(Interactable):
    def __init__(self, items: List[Item]=[]):
        super().__init__(
            name="Bett",
            description="Ein großes Himmelbett. Die Laken sehen einladend, aber etwas staubig aus.",
            items=items # Der Brief ist unter dem Bett/der Matratze
        )
        self.is_sleeping = False

    def use(self, state: GameState)-> List[Item]:
        """Der Spieler kann schlafen, um seine HP vollständig zu regenerieren."""
        if not self.is_sleeping:
            print(f"{Fore.BLUE}Du legst dich hin und schließt die Augen...{Style.RESET_ALL}")
            self.is_sleeping = True
            
            # Vollständige Heilung
            old_hp = state.player.base_stats.hp
            state.player.base_stats.hp = 100 
            
            print("Zzz... Du schläfst tief und fest.")
            print(f"{Fore.GREEN}Du wachst erfrischt auf! HP: {old_hp} -> 100{Style.RESET_ALL}")
            self.is_sleeping = False
        else:
            print("Du bist bereits hellwach.")

        if self.items:
            print(f"{Fore.CYAN}Als du die Matratze anhebst, entdeckst du etwas darunter...{Style.RESET_ALL}")
            # Ruft das Standard-Menü zum Mitnehmen auf
            return self._show_item_menu()
        else:
            print("Außer ein paar Wollmäusen unter dem Rahmen findest du nichts.")

    def inspect(self):
        """Untersucht das Bett nach versteckten Dingen."""
        print(f"\nDu untersuchst: {self.name}")
        print(self.get_description())

        