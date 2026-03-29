# Escape Room Together - Ein textbasiertes Escape-Room-Spiel in Python
```ansi
[2;31mE[0m[2;35mP[0m[2;34mI[0m[2;36mC[0m [2;32mB[0m[2;33mA[0m[2;31mN[0m[2;35mA[0m[2;34mN[0m[2;32m[2;36mE[0m[2;32m[0m[2;32mN[0m [2;33mV[0m[2;31mE[0m[2;35mR[0m[2;36m[2;34mS[0m[2;36m[0m[2;32m[0m[2;34m[2;36mI[0m[2;34m[0m[2;34m[2;32mO[0m[2;34m[0m[2;33mN[0m[2;31m![0m[2;35m![0m[2;34m![0m[2;36m![0m[2;32m![0m
```

Escape Room Together ist ein einfaches, textbasiertes Escape-Room-Spiel, das in Python geschrieben wurde. Das Spiel bietet eine interaktive Erfahrung, bei der Spieler Rätsel lösen und Hinweise sammeln müssen, um aus verschiedenen virtuellen Räumen zu entkommen.
Ziel ist mit anderen Teilnehmern das Spiel zu erweitern und neue Räume, Gegenstände und Rätsel zu erstellen!


## Installation
1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/Maytastic/EscapeRoomTogether.git
    ```
2. Navigieren Sie in das Verzeichnis:
   ```bash
   cd EscapeRoomTogether
   ```
3. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install colorama
   ```

## Game loop

1. Du kommst in das Spiel und befindest dich im ersten Raum.
2. Du kannst verschiedene Befehle eingeben, um mit dem Raum zu interagieren, z.B.:
   - `inspect [item]`: Untersucht ein bestimmtes Objekt im Raum.
   - `use [item]`: Verwendet einen Gegenstand aus deinem Inventar.
    - `inventory`: Zeigt die Gegenstände in deinem Inventar an.
    - `help`: Zeigt eine Liste der verfügbaren Befehle an.
3. Löse Rätsel und finde Hinweise, um den Raum zu verlassen.
4. Sobald du den Raum erfolgreich verlassen hast, gelangst du zum nächsten Raum.
    - Verlassen tust du mit `exit` Befehl, wenn du die Bedingungen zum Verlassen erfüllst.    

Ich habe die Dokumentation um die neuen Funktionen (History, Tab-Completion, Rezepte/Kochen und Debug-JSON) erweitert und die Struktur professionalisiert.

---

## Mitmachen

Füge deinen Raum, Gegenstand oder Rätsel hinzu, indem du eine neue Python-Datei im entsprechenden Verzeichnis erstellst und die vorhandenen Vorlagen nutzt.

### 1. Einen neuen Raum erstellen

Jeder Raum benötigt eine Klasse, die von `Room` (`template/room.py`) erbt. Dies garantiert standardisierte Methoden für Interaktionen und Bewegung.

* **Pflichtaufgabe `exit`:** Du musst die `exit`-Methode definieren. Sie wird aufgerufen, wenn der Spieler `exit` tippt, und gibt `True` (Erfolg) oder `False` (Bleiben) zurück.
* **Inventar-Check:** Nutze die Methode `gamestate.player.inventory.has_item("Name")`, um Rätselbedingungen zu prüfen.

```python
from template.room import Room
from colorama import Fore

class MyNewRoom(Room):
    def __init__(self):
        super().__init__(
            name="Geheimkammer",
            description="Ein dunkler Raum, der nach altem Pergament riecht."
        )
        self.schlüssel = Key(name="Goldener Schlüssel")
        # Füge Interaktionsobjekte hinzu
        self.interactables.update({"kühlschrank": Fridge(self.schlüssel)})

    def exit(self, state) -> bool:
        
        if state.player.inventory.has_item(self.schlüssel):
            print(f"{Fore.GREEN}Die schwere Steintür schwingt auf!{Fore.RESET}")
            return True
        print("Die Tür hat kein Schlüsselloch, aber eine quadratische Vertiefung...")
        return False

```

### 2. Interaktive Objekte & Kochen
Nicht alle Interaktiven Elemente sind getestet und könnten fehler haben.

Objekte befinden sich im Ordner `interactables/`. Du kannst sie in deinem Raum konfigurieren:

Fasst alle Interaktiven Elemente haben Standardwerte, also kannst du sie auch ohne Inhalt beschreiben.
Wenn das Programm abstürzt, dann siehst du oft welche Werte gesetzt werden müssen.

* **Schrank (Cabinet):** Kann mit `code` und `items` (Liste von Gegenständen) erstellt werden.
```python
"cabinet": Cabinet(code="4267", items=[Keycard(data="Ausgangs-Keycard"),Sword(),IronBoots(),IronHead(),]),
```
* **Herd (Stove):** Akzeptiert eine Liste von `Recipe`-Objekten.\
```python
"herd": Stove(recipes=[ultimatives_rezept])
```
* **Bett (Bed):** Kann Items enthalten und ermöglicht dich auf das Bett zu legen um HP zu regenerieren\
```python
"bett": Bed(items=[Note(name="Zerknüllter Zettel",content="Meine Nase ist kalt")])
```
* **Sofa (Couch):** Ermöglicht das durchsuchen des Couch dabei können Items hinterlegt werden\
```python
"sofa": Couch(items=[Note("Schmutziger Zettel", "Wow ich bin schmutzig")]),
```
* **Kühlschrank (Fridge):** Kann Consumables enthalten. Kann mit `locked` gespeert werden mit `items` können Sachen in den Kühlschrank reingelgt werden\
```python
"kühlschrank": Fridge(items=[Salt(), Pepper(), Egg()], locked=False)
```
* **Radio (Radio):** Ein Radio welches die Frequenzen ändern kann. Je nach Frequenz können andere
Nachrichten versteckt werden\
```python
"radio": Radio(initial_stations={100: "Deine Mom", 120: "Dein Dad"})
```
* **Tisch (Table):** Akzeptiert eine Liste von `Recipe`-Objekten.
```python
"tisch": Table(items=[Note(
            name="Zettel",
            content="Der Techniker meinte, unter dem Tisch klebt etwas... für Notfälle."
        )]),
```
* **Terminal (Terminal):** Interaktiver Computer in dem du Dateien und informationen verstecken kannst.
Benötigt Dateien (`files`) und deren inhalte (`content`)
```python
"terminal": Terminal(
                files={
                    "/": ["/home", "/var", "/etc"],
                    "/home": ["/user", "/dokumente", "notiz"],
                    "/var": ["/log", "/tmp"],
                    "/etc": ["konfig.cfg", "hosts"],
                },
                content={
                    "/etc/konfig.cfg": "schrank_code=4267 # Der Code für den Schrank",
                    "/home/notiz": "Denk daran, die Server-Logs auf Anomalien zu prüfen.\nDie Keycard für den Ausgang befindet sich im Schrank.\nIch nutze übrigens Arch (I use Arch btw).\nDer Schrank-Code wird über dieses Terminal konfiguriert.",
                    "/etc/hosts": "ad.com 0.0.0.0\ngoogle.de 0.0.0.0",
                },
            ),
```
* **TV (TV):** Ein Fernseher, welches Kannäle bietet in dennen du Informationen und hinweise verstecken kannst.
```python
"tv": Television(channels=["Das licht scheint nicht geradeaus", "Blumen richen toll"])
```
* **Whiteboard (Whiteboard):** Auf dem Whiteboard kannst du informationen verstecken. Der Spieler kann auch sachen draufmalen. `hint` ermöglicht ein einfachen Vorschlag zu machen, `content` ermöglicht die ganzen Text auf dem Whiteboard zu schreiben
```python
"whiteboard": Whiteboard(),
```

## Eigenes Interaktives Element

Ein interaktives Element besteht immer aus einer `def __init__(self)` und einer `def use(self, state)->List[Item]`
Bei der Initialisierung führst du immer die super funktion auf und konfigurierst dein Interaktives element

Beispiel:

```python
from template.interactable import Interactable
from core.gamestate import GameState
from template.item import Item
from colorama import Fore, Style
from typing import List

class Bed(Interactable):
    def __init__(self, items: List["Item"]=[]):
        super().__init__(
            name="Bett",
            description="Ein großes Himmelbett. Die Laken sehen einladend, aber etwas staubig aus.",
            items=items # Der Brief ist unter dem Bett/der Matratze
        )

    def use(self, state: GameState)-> List["Item"]:
        
        return self.items # gibt beim use direkt die Items zurück
        

```
#### Rezepte definieren

Rezepte vergleichen die Namen der Items in einer Pfanne mit den Anforderungen.

```python
from template.recipe import Recipe
from items.consumables import Ei, Salz, Omelett

# Zutaten sind Instanzen, result_item ist das fertige Objekt
rezept = Recipe(ingredients=[Ei(), Salz()], result_item=Omelett())

```
## Items hinzufügen
Es gibt aktuell verschiedene Itemarten

* Consumable -> Items die du essen kannst wie Heilpotions, Stärkepotions
* Armor -> Rüstungen die dich im Kampf schützen
* Weapons -> Items die du nutzen kannst um dich zu verteidigen
* Item -> Standard Item template aus dem du neue Itemarten bilden kannst

#### Consumbale
Einfaches Consumable

```python
from template.consumable import Consumable
class Bread(Consumable):
    def __init__(self):
        super().__init__(
            name="Frisches Brot",
            description="Ein einfaches Brot. Heilt 10 HP.",
            hp=10
        )
```

Consumable mit Erweiterungen

```python

from template.consumable import Consumable
from typing import TYPE_CHECKING
from colorama import Fore, Style

if TYPE_CHECKING:
    from core.gamestate import GameState
class StrengthElixir(Consumable):
    def __init__(self):
        super().__init__(
            name="Elixier der Stärke",
            description="Erhöht deine Basis-Stärke permanent um 2.",
            hp=0
        )
        self.strength_gain = 2

    def interact(self, state: 'GameState'):
        player = state.player
        # Permanente Erhöhung der Basis-Stats
        player.base_stats.strength += self.strength_gain
        
        print(f"{Fore.CYAN}Du spürst neue Kraft! Basis-Stärke ist jetzt {player.base_stats.strength}.{Style.RESET_ALL}")
        print(f"Deine Gesamtstärke (inkl. Ausrüstung) beträgt nun: {player.total_stats.strength}")
        
        player.inventory.remove_by_object(self)
```

### Weapon
Ein Waffe ist ein equipable Item du musst daher sagen wo diese ausgerüstet werden soll. 
```python
from template.weapon import Weapon
from core.equipment import EquipmentSlot

class Crowbar(Weapon): # "Brechstange" auf Englisch

    def __init__(self):
        super().__init__(
            name="Brechstange",
            description="Eine robuste Stahlstange mit einem gebogenen, abgeflachten Ende. Ideal zum Aufbrechen von Kisten oder als improvisierte Waffe.",
            attack_power=7, # Weniger als ein Schwert, aber immer noch effektiv
            slot=EquipmentSlot.MAIN_HAND # Oder EquipmentSlot.TWO_HAND, falls sie beidhändig ist
        )
```

### Armor
```python
from template.armor import Armor
from core.equipment import EquipmentSlot
# --- TORSO ---
class IronChestplate(Armor):
    def __init__(self):
        super().__init__(
            name="Eisenbrustplatte",
            description="Ein massiver Brustpanzer aus Eisenplatten.",
            defense=12,
            slot=EquipmentSlot.CHEST
        )
```

### Item
Ein einfaches Item muss explizierter definiert werden so müssen hier die ItemProperties eingestellt werden

```python
class Pan(Item):
    def __init__(self, contents: Optional[List["Item"]] = None):
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
        self.contents: List["Item"] = contents if contents is not None else []
```

Wenn du dein Item wie hier Interactable machst musst eine `interact` funtion zur Klasse hinzufügen wie hier.
Diese wird aufgerufen wenn du im inventar managment das Item mit use ausführst.
```python

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
```

#### Debugging mit JSON

Um die genauen Daten eines Items im Inventar zu prüfen (z.B. für die Entwicklung neuer Rätsel), kannst du im Inventar-Menü den `json`-Befehl nutzen:

* Befehl: `json [Index]` (z.B. `json 0`)
* Gibt alle Attribute, Enums und Zustände des Objekts im JSON-Format aus.

### 4. Den Raum registrieren

Nachdem dein Raum fertig ist, muss er in der `main.py` in die Liste eingetragen werden. Die Reihenfolge in der Liste bestimmt die Abfolge im Spiel.

```python
from rooms.my_new_room import MyNewRoom

räume = [
    Labor(),
    Kueche(),
    MyNewRoom(),  # Dein Raum als drittes Level
]

```

