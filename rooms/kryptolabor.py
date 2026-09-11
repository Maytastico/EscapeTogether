from typing import TYPE_CHECKING
from template.room import Room
from core.npc import NPC
from dialogue.action import Action
from dialogue.behaviour import Behaviour
from interactables.terminal import Terminal
from interactables.cabinet import Cabinet
from interactables.whiteboard import Whiteboard
from interactables.table import Table
from interactables.funkgerät import Funkgerät
from items.notebook import Notebook
from items.keycard import Keycard
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState


class KryptoLabor(Room):
    """Cyberkids: Mission Binärcode - Das Krypto-Komplott."""

    def __init__(self):
        super().__init__(
            name="Krypto-Labor",
            description=(
                "Ein provisorisches Einsatzquartier der Krypto-Taskforce. Kabel verlaufen über den Boden, "
                "ein Funkgerät rauscht leise vor sich hin und ein Terminal blinkt im Dunkeln.\n"
                "Die Verbindung ist unsicher - irgendwo da draußen lauert ein feindliches Hacker-Team."
            ),
        )

        self.interactables.update({
            "funkgerät": Funkgerät(
                binary_message="01000011 01001111 01000100 01000101",
                answer="code",
            ),
            "terminal": Terminal(
                files={
                    "/": ["/logs", "/home", "/system"],
                    "/logs": ["hacker_log", "static_rauschen"],
                    "/home": ["einsatzbefehl"],
                    "/system": ["firewall_status"],
                },
                content={
                    "/home/einsatzbefehl": (
                        "EINSATZBEFEHL - KRYPTO-TASKFORCE\n"
                        "1. Höre das Funkgerät ab und entschlüssle die verstärkte Binärnachricht.\n"
                        "2. Durchsuche dieses Terminal nach dem abgefangenen Hacker-Log (Ordner /logs)\n"
                        "   und knacke den Hex-Code fuer den Datentresor.\n"
                        "3. Nutze das Codebuch auf dem Schreibtisch, wenn du nicht weiterweißt.\n"
                        "Viel Erfolg, Agent!"
                    ),
                    "/logs/hacker_log": (
                        "ABGEFANGENES HACKER-LOG (HEX-CODE):\n\n"
                        "31 33 33 37\n\n"
                        "Wandle jedes Hex-Zeichenpaar in ein ASCII-Zeichen um, um den Zugangscode\n"
                        "fuer den Datentresor zu erhalten."
                    ),
                    "/logs/static_rauschen": "▓▒░ ...nur weißes Rauschen... falscher Kanal? ░▒▓",
                    "/system/firewall_status": (
                        "Firewall-Status: AKTIV\n"
                        "Alle Ports gesichert. Letzter Eindringungsversuch: TAK-TAK-TAK...\n"
                        "(Vermutlich nur ein Hacker, der es nicht ins System schafft.)"
                    ),
                },
            ),
            "datentresor": Cabinet(
                code="1337",
                name="Datentresor",
                description="Ein moderner Datentresor mit digitalem Zahlenschloss.",
                items=[Keycard(data="Cyberagenten-Ausweis")],
            ),
            "schreibtisch": Table(
                name="Schreibtisch",
                description="Ein Schreibtisch voller Unterlagen der Krypto-Taskforce.",
                items=[
                    Notebook(pages=[
                        (
                            "CODEBUCH - TEIL 1: BINÄRSYSTEM\n"
                            "--------------------------------\n"
                            "Computer kennen nur zwei Zustände: AUS (0) und AN (1) - wie ein Lichtschalter.\n"
                            "Reiht man 8 solcher Schalter (Bits) aneinander, nennt man das ein BYTE.\n"
                            "Jede Stelle hat einen festen Wert: 128-64-32-16-8-4-2-1.\n"
                            "Steht an einer Stelle eine 1, zählt der Wert mit, bei einer 0 nicht.\n\n"
                            "Beispiel: 01000001 -> 64 + 1 = 65. Und 65 ist im ASCII-Code der Buchstabe 'A'!\n"
                            "Um eine Nachricht zu entschlüsseln: Teile sie in 8er-Gruppen und schau in der\n"
                            "Tabelle auf Seite 3 nach, welcher Buchstabe zu jeder Gruppe gehört."
                        ),
                        (
                            "CODEBUCH - TEIL 2: HEXADEZIMAL-SYSTEM\n"
                            "----------------------------------------\n"
                            "Binärcode ist genau, aber lang: 8 Zeichen für einen einzigen Buchstaben.\n"
                            "Profi-Agenten nutzen deshalb HEXADEZIMAL-Code. Der zählt nicht nur bis 9,\n"
                            "sondern bis 15 - mit den Ziffern 0-9 und den Buchstaben A-F:\n"
                            "A=10  B=11  C=12  D=13  E=14  F=15\n\n"
                            "Ein Byte (8 Bit) passt IMMER genau in 2 Hex-Zeichen.\n"
                            "Beispiel: 01000001 = 0100 0001 = 4 1 -> Hex-Code '41' -> Buchstabe 'A'.\n"
                            "Merke: Immer 2 Hex-Ziffern zusammen ergeben 1 Zeichen. Tabelle auf Seite 3!"
                        ),
                        (
                            "CODEBUCH - TEIL 3: UMRECHNUNGSTABELLE (ASCII)\n"
                            "------------------------------------------------\n"
                            "Zeichen | Binär     | Hex\n"
                            "   0    | 00110000  | 30\n"
                            "   1    | 00110001  | 31\n"
                            "   2    | 00110010  | 32\n"
                            "   3    | 00110011  | 33\n"
                            "   4    | 00110100  | 34\n"
                            "   5    | 00110101  | 35\n"
                            "   6    | 00110110  | 36\n"
                            "   7    | 00110111  | 37\n"
                            "   8    | 00111000  | 38\n"
                            "   9    | 00111001  | 39\n"
                            "   A    | 01000001  | 41\n"
                            "   B    | 01000010  | 42\n"
                            "   C    | 01000011  | 43\n"
                            "   D    | 01000100  | 44\n"
                            "   E    | 01000101  | 45\n"
                            "   F    | 01000110  | 46\n"
                            "   ...  | ...       | ...\n"
                            "   O    | 01001111  | 4F\n"
                            "(Frag Agentin Byte, falls ein Buchstabe fehlt!)"
                        ),
                    ]),
                ],
            ),
            "whiteboard": Whiteboard(
                hint="Sprich mit Agentin Byte, wenn du nicht weiterweißt - und traue niemals einem Hacker!"
            ),
        })

        self.npcs.update({
            "byte": NPC("Agentin Byte", self._build_byte_dialogue()),
            "v01d": NPC("V01D", self._build_hacker_dialogue()),
        })

        self.kursleiter_rätsel_gelöst = False

    def _build_byte_dialogue(self) -> "Behaviour":
        hauptmenü = Behaviour(
            text=(
                "Agentin Byte flüstert: 'Psst, Agent! Bereit für deine Undercover-Ausbildung? "
                "Frag mich alles, bevor die feindlichen Hacker uns entdecken.'"
            ),
            actions=[],
        )

        binär_lektion = Behaviour(
            text=(
                "Agentin Byte: 'Computer kennen nur AUS (0) und AN (1) - wie ein Lichtschalter. "
                "Acht solcher Schalter hintereinander nennt man ein BYTE. Jede Stelle zählt: "
                "128-64-32-16-8-4-2-1, aber nur wenn dort eine 1 steht.\n"
                "Beispiel: 01000001 -> 64+1 = 65 -> Buchstabe A. Dein Codebuch hat die volle Tabelle!'"
            ),
            actions=[],
        )
        binär_lektion.actions = [Action(text="Zurück zum Hauptmenü", behaviour=hauptmenü)]

        hex_lektion = Behaviour(
            text=(
                "Agentin Byte: 'Hexadezimal-Code ist der Profi-Code: er zählt bis 15 mit 0-9 und A-F. "
                "Zwei Hex-Zeichen ergeben immer genau ein Byte, also ein Zeichen.\n"
                "Beispiel: 01000001 = 41 im Hex-Code = Buchstabe A. Schau ins Codebuch für die Tabelle!'"
            ),
            actions=[],
        )
        hex_lektion.actions = [Action(text="Zurück zum Hauptmenü", behaviour=hauptmenü)]

        tipp = Behaviour(
            text=(
                "Agentin Byte: 'Ein Tipp, Agent: Das Funkgerät hat eine verstärkte Nachricht in Binärcode "
                "abgefangen - teile sie in 8er-Gruppen. Und im Terminal versteckt sich unter /logs ein "
                "Hacker-Log in Hexadezimal-Code, den du für den Datentresor brauchst.'"
            ),
            actions=[],
        )
        tipp.actions = [Action(text="Zurück zum Hauptmenü", behaviour=hauptmenü)]

        abschied = Behaviour(
            text="Agentin Byte: 'Viel Erfolg, Agent. Ich behalte die Hacker im Auge.'",
            actions=[],
        )

        hauptmenü.actions = [
            Action(text="Erklär mir das Binärsystem", behaviour=binär_lektion),
            Action(text="Erklär mir das Hexadezimal-System", behaviour=hex_lektion),
            Action(text="Gib mir einen Tipp zur Mission", behaviour=tipp),
            Action(text="Gespräch beenden", behaviour=abschied),
        ]
        return hauptmenü

    def _build_hacker_dialogue(self) -> "Behaviour":
        hauptmenü = Behaviour(
            text=(
                "Auf dem Bildschirm blinkt eine verzerrte Stimme: 'Na, kleiner Agent? Denkst du wirklich, "
                "du kannst MEIN Netzwerk knacken?'"
            ),
            actions=[],
        )

        drohung = Behaviour(
            text=(
                "Der Hacker lacht: 'Ihr werdet den Code niemals knacken! Meine Verschlüsselung ist perfekt!' "
                "*Die Verbindung rauscht verdächtig.*"
            ),
            actions=[],
        )
        drohung.actions = [Action(text="Zurück", behaviour=hauptmenü)]

        falscher_tipp = Behaviour(
            text=(
                "Der Hacker grinst hinterlistig: 'Na gut, ein Tipp: Der Zugangscode ist 0000... "
                "vertrau mir!' Irgendwie wirkt das nicht besonders glaubwürdig."
            ),
            actions=[],
        )
        falscher_tipp.actions = [Action(text="Zurück", behaviour=hauptmenü)]

        abschied = Behaviour(
            text="Du trennst schnell die Verbindung, bevor der Hacker deinen Standort orten kann.",
            actions=[],
        )

        hauptmenü.actions = [
            Action(text="'Wir werden dich stoppen!'", behaviour=drohung),
            Action(text="Nach einem Tipp fragen", behaviour=falscher_tipp),
            Action(text="Verbindung trennen", behaviour=abschied),
        ]
        return hauptmenü

    def _letzte_uebertragung(self):
        """Das digitale Abschluss-Rätsel: Ziffer 4 von 4 der Agenten-Codekarte."""
        if self.kursleiter_rätsel_gelöst:
            return

        print(
            f"\n{Fore.CYAN}Eine letzte Übertragung geht ein: 'Glückwunsch, Agent! Eine letzte Nachricht: "
            f"Der Kursleiter feiert dieses Jahr seinen 24. Geburtstag. Addiere die Ziffern seines Alters "
            f"(2+4) - das ist deine letzte Zahl. Zur Bestätigung hier ihr Binärcode:'{Style.RESET_ALL}"
        )
        print(f"{Style.BRIGHT}0110{Style.RESET_ALL}\n")

        for _ in range(3):
            antwort = input("Löse das Rätsel - deine Antwort: ").strip().lower()
            if antwort in ("6", "0110"):
                self.kursleiter_rätsel_gelöst = True
                print(f"{Fore.GREEN}{Style.BRIGHT}Richtig! Ziffer 4 von 4: 6{Style.RESET_ALL}")
                print("Trage sie auf deine Agenten-Codekarte ein - jetzt hast du alle vier Ziffern beisammen!")
                return
            print(
                f"{Fore.RED}Nicht ganz. Tipp: Addiere die beiden Ziffern von 24 (2+4) oder entschlüssle "
                f"den Binärcode oben.{Style.RESET_ALL}"
            )

        print(f"{Fore.YELLOW}Kein Problem - frag einfach deine Kursleitung nach der letzten Ziffer!{Style.RESET_ALL}")

    def exit(self, state: "GameState") -> bool:
        hat_ausweis = any(
            isinstance(item, Keycard) and item.data == "Cyberagenten-Ausweis"
            for item in state.player.inventory.items
        )
        funknachricht_entschlüsselt = self.interactables["funkgerät"].solved

        if hat_ausweis and funknachricht_entschlüsselt:
            print(
                f"{Fore.GREEN}{Style.BRIGHT}Mission erfüllt! Mit dem Cyberagenten-Ausweis aus dem Datentresor "
                f"und der entschlüsselten Funknachricht übermittelst du die geheime Botschaft sicher an die "
                f"Zentrale.{Style.RESET_ALL}"
            )
            self._letzte_uebertragung()
            return True

        if not funknachricht_entschlüsselt:
            print(f"{Fore.RED}Die verstärkte Nachricht im Funkgerät ist noch nicht entschlüsselt!{Style.RESET_ALL}")
        if not hat_ausweis:
            print(f"{Fore.RED}Dir fehlt noch der Cyberagenten-Ausweis aus dem Datentresor!{Style.RESET_ALL}")
        return False
