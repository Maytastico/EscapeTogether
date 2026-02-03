from rooms.labor import Labor
from rooms.arbeitszimmer import Arbeitszimmer
from colorama import init, Style
from core.gamestate import GameState

# Initialisiert Colorama für farbige Terminal-Ausgaben
init()

# Liste der Räume definieren
# Hier können weitere Räume hinzugefügt werden
räume = [
    Arbeitszimmer(),
    Labor()
]

# Speichert den aktuellen Spielzustand
state = GameState(räume)
from items.keycard import Keycard
state.player.inventory.add([Keycard("hi"), Keycard("miau")])


def main():
    # Willkommensnachricht
    print("Willkommen im Labor! Du bist im Wissenschaftslabor gefangen und musst den Ausgang finden, indem du den Code knackst.")
    state.get_current_room().help()
    state.get_current_room().enter()
    
    # Spielschleife
    while True:
        # Benutzereingabe abfragen
        command = input(f"{Style.BRIGHT}Befehl eingeben: {Style.RESET_ALL}").strip().lower().split(" ")
        
        if command[0] == "exit":
            success = state.get_current_room().exit(state)
            
            # Wenn das Verlassen erfolgreich war, zum nächsten Raum oder Spiel beenden
            if success:
                if state.next_room():
                    print("Du hast den nächsten Raum betreten.")
                    state.get_current_room().enter()
                else:
                    print("Herzlichen Glückwunsch! Du hast das Spiel erfolgreich abgeschlossen.")
                    break
                
        elif command[0] == "inspect":
            # Optionales Item-Argument verarbeiten
            item = command[1] if len(command) > 1 else None
            
            # Den Raum oder ein spezielles Objekt untersuchen
            state.get_current_room().inspect(item)
            
        elif command[0] == "use":
            # Überprüfen, ob ein Objekt angegeben wurde
            if len(command) < 2:
                print("Verwendung: use <objekt>")
            else:
                # Das angegebene Objekt benutzen
                item_name = command[1]
                
                # Versuch, das Objekt im Raum zu benutzen
                item = state.get_current_room().use_interactable(item_name, state)
                
                # Manche Aktionen geben Items für das Inventar zurück
                if item is not None:
                    if len(item) > 0:
                        state.player.inventory.add(item)
                    
        elif command[0] == "inventory":

            if len(state.player.inventory.items) == 0:
                print("Dein Inventar ist leer.")
                continue
            
            print("Dein Inventar enthält:")
            for idx, item in enumerate(state.player.inventory.items):
                print(f"- [{idx}] {item.name}: {item.description}")
                
            if len(command) > 2:
                arg = command[1]
                item_id = command[2]

                if arg == "equip":

                    if not item_id.isnumeric():
                        print("Verwendung: inventory equip <Nummer des Item>")
                        continue
                    item = state.player.inventory.items[int(item_id)]
                    state.player.equip(item=item, slot=item.slot)
            
                

        elif command[0] == "jump":
            print("Du bist im folgenden Raum: ", state.get_current_room().__class__.__name__)
            if len(command) > 1:
                room_index = int(command[1])
                if state.change_room(room_index):
                    print(f"Du bist zu Raum {room_index} gesprungen.")
                    state.get_current_room().enter()
                else:
                    print()
                    print("Der Raum existiert nicht.")
            else:
                print("Verwendung: jump <raum_nummer>")
                print("Aktuell gibt es folgende Räume:")
                for idx, raum in enumerate(state.rooms):
                    print(f"- {idx}: {raum.__class__.__name__}")
                print()

        elif command[0] == "help":
            state.get_current_room().help()
        else:
            print("Unbekannter Befehl. Gib 'help' ein, um eine Liste der Befehle zu sehen.")    
    
if __name__ == "__main__":
    main()