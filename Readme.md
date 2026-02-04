# Escape Room Together - Ein textbasiertes Escape-Room-Spiel in Python

Escape Room Together ist ein einfaches, textbasiertes Escape-Room-Spiel, das in Python geschrieben wurde. Das Spiel bietet eine interaktive Erfahrung, bei der Spieler Rätsel lösen und Hinweise sammeln müssen, um aus verschiedenen virtuellen Räumen zu entkommen.
Ziel ist mit anderen Teilnehmern das Spiel zu erweitern und neue Räume, Gegenstände und Rätsel zu erstellen.


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
        # Füge Interaktionsobjekte hinzu
        self.interactables.update({})

    def exit(self, state) -> bool:
        if state.player.inventory.has_item("Goldener Schlüssel"):
            print(f"{Fore.GREEN}Die schwere Steintür schwingt auf!{Fore.RESET}")
            return True
        print("Die Tür hat kein Schlüsselloch, aber eine quadratische Vertiefung...")
        return False

```

### 2. Interaktive Objekte & Kochen
Nicht alle Interaktiven Elemente sind getestet und könnten fehler haben.

Objekte befinden sich im Ordner `interactables/`. Du kannst sie in deinem Raum konfigurieren:

* **Schrank (Cabinet):** Kann mit `code` und `items` (Liste von Gegenständen) erstellt werden.
* **Herd (Stove):** Akzeptiert eine Liste von `Recipe`-Objekten.

#### Rezepte definieren

Rezepte vergleichen die Namen der Items in einer Pfanne mit den Anforderungen.

```python
from template.recipe import Recipe
from items.consumables import Ei, Salz, Omelett

# Zutaten sind Instanzen, result_item ist das fertige Objekt
rezept = Recipe(ingredients=[Ei(), Salz()], result_item=Omelett())

```
#### Items hinzufügen
Es gibt aktuell drei verschiedene Itemarten

* No

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

---

**Möchtest du, dass ich noch einen Abschnitt über das Erstellen komplett neuer Items (z.B. Waffen oder Rüstungen) mit ihren spezifischen Werten hinzufüge?**