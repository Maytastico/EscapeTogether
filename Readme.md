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

## Mitmachen

Füge deinen Raum, Gegenstand oder Rätsel hinzu, indem du eine neue Python-Datei im entsprechenden Verzeichnis erstellst und die vorhandenen Vorlagen nutzt.

Jeder Raum braucht eine eigene Klasse, die von der `Room`-Klasse erbt. Diese befindet sich im Ordner `template/room.py` und gibt dem Raum standardisierte Methoden und Attribute vor, als auch standardisierte Interaktionen.

Du musst exit selber definieren, um zu bestimmen, was passiert, wenn der Spieler den Raum verlässt.
Beim verlassen wird von der Hauptlogik das Inventar des
Spielers übergeben. Hier kannst du überprüfen, ob der Spieler bestimmte Gegenstände besitzt, um den Raum zu verlassen.

Beispiel:
```python
from template.room import Room
class MyNewRoom(Room):
    def __init__(self):
        super().__init__()
        self.interactables.update({
            # Füge hier deine Gegenstände hinzu
        })

    def exit(self, items: list):
        print("You exit My New Room.")

```
Aktuell gibt es 3 interaktive objekte:
- Terminal (im Ordner interactables/terminal.py)
- Cabinet (im Ordner interactables/cabinet.py)
- Whiteboard (im Ordner interactables/whiteboard.py)

Du kannst diese erweitern oder neue erstellen.
Um sie in deinem Spiel zu verwenden kannst du sie
importieren wie hier gezeigt:
```python
from interactables.terminal import Terminal
```

Interaktive Objekte können konfiguriert werden, indem du ihre Attribute im Konstruktor änderst.

Zum Beispiel kannst du einen Schrank mit einem Code und Gegenständen erstellen:
```python
from interactables.cabinet import Cabinet
class MyNewRoom(Room):
    def __init__(self):
        super().__init__(
            name="My New Room",
            description="A description of my new room.",
        )
        self.interactables.update({
            "cabinet": Cabinet(code="1234", items=[Keycard()])
        })
```

Wenn du deinen Raum fertiggestellt hast, füge ihn der Liste der Räume in `main.py` hinzu, damit er im Spiel verfügbar ist.
Sobald der ein Rätsel im Raum gelöst wird, wird der Index erhöht und der Spieler gelangt in den nächsten Raum.

```python
from rooms.my_new_room import MyNewRoom

räume = [
    Labor(),
    MyNewRoom(),  # Füge deinen neuen Raum hier hinzu
]
...
```

## Vorschläge für neue Räume

### Gewaltsamer Ausbruch

Du findest eine Brechstange in einem Schrank, mit der du die Tür aufbrechen kannst.
Und du öffnest die Tür des Schrankes mit einem Code der auf dem Whiteboard steht.

Items: Brechstange
Iteraktives Objekt: Schrank (cabinet), Whiteboard (whiteboard)

Raum zum Verlassen: Brechstange im Inventar

### Geheimer Durchgang
Du findest einen geheimen Durchgang hinter einem Gemälde, das du mit einem speziellen Werkzeug entfernen kannst.
Items: Werkzeugkasten
Iteraktives Objekt: Gemälde (painting)

Raum zum Verlassen: Werkzeugkasten im Inventar

### Serverraum Zugang
Du musst einen Code eingeben, um die Tür zum Serverraum zu öffnen.
Items: Keycard
Iteraktives Objekt: Terminal (terminal)
Raum zum Verlassen: Keycard im Inventar

### Notizenheft
Du findest ein Notizheft mit wichtigen Hinweisen, die dir helfen, den Raum zu verlassen.
Items: Notizheft
Iteraktives Objekt: Schreibtisch (desk)
Raum zum Verlassen: Notizheft im Inventar

### Chemielabor
Du musst die richtige Kombination von Chemikalien mischen, um eine Reaktion auszulösen, die dir den Weg nach draußen zeigt.
Items: Chemikalien
Iteraktives Objekt: Labortisch (lab_table)
Raum zum Verlassen: Erfolgreiche Reaktion   
