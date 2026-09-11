from template.interactable import Interactable
from core.gamestate import GameState
from colorama import Fore, Style


class Funkgerät(Interactable):

    def __init__(self, binary_message: str, answer: str, name: str = "Funkgerät",
                 description: str = "Ein altes Funkgerät. Eine kleine Anzeige zeigt 'SIGNAL VERSTÄRKT'."):
        """Ein Funkgerät, das eine abgefangene, verstärkte Nachricht im Binärcode empfängt.
        @param binary_message: Die Nachricht in 8-Bit-Gruppen, z.B. '01000011 01001111 01000100 01000101'.
        @param answer: Das entschlüsselte Wort. Groß-/Kleinschreibung spielt keine Rolle.
        """
        super().__init__(name=name, description=description, locked=True)
        self.binary_message = binary_message
        self.answer = answer.strip().lower()
        self.solved = False

    def _play_message(self):
        print(f"\n{Fore.YELLOW}*Kratzen* *Rauschen* Eine verstärkte Nachricht wird empfangen...{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{self.binary_message}{Style.RESET_ALL}")
        print("...das Signal bricht ab.\n")

    def use(self, state: GameState):
        if self.solved:
            print(f"{Fore.GREEN}Die Nachricht wurde bereits erfolgreich entschlüsselt.{Style.RESET_ALL}")
            self._play_message()
            return

        self._play_message()
        print("[1] Antwort eingeben")
        print("[2] Nichts tun")
        choice = input("Was möchtest du tun? ").strip()

        if choice == "1":
            guess = input("Entschlüsseltes Wort: ").strip().lower()
            if guess == self.answer:
                self.locked = False
                self.solved = True
                print(f"\n{Fore.GREEN}{Style.BRIGHT}Empfang bestätigt! Die Nachricht wurde korrekt entschlüsselt.{Style.RESET_ALL}")
                print("Für einen Moment verstummt das Rauschen der feindlichen Hacker.")
            else:
                print(f"{Fore.RED}Falsch entschlüsselt. Teile die Bits in 8er-Gruppen und schlage im Codebuch nach!{Style.RESET_ALL}")
        else:
            print("Du lässt das Funkgerät weiterlaufen.")

    def inspect(self):
        print(f"\nDu untersuchst: {self.name}")
        print(self.get_description())
        if self.solved:
            print(f"{Fore.GREEN}Ein grünes Lämpchen blinkt - die Nachricht wurde erfolgreich entschlüsselt.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Ein rotes Lämpchen blinkt - eine unentschlüsselte Nachricht wartet.{Style.RESET_ALL}")
