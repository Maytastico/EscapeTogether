from rooms.labor import Labor
from rooms.arbeitszimmer import Arbeitszimmer
from colorama import init, Style

# Initialisiert Colorama für farbige Terminal-Ausgaben
init()

# Liste der Räume definieren
# Hier können weitere Räume hinzugefügt werden
räume = [
    Arbeitszimmer(),
    Labor()
]

# Speichert den aktuellen Spielzustand
state = {
    "current_room_index": 0,
    "raum": räume[0],
    "inventar":[],
}

def main():
    # Willkommensnachricht
    print("Willkommen im Labor! Du bist im Wissenschaftslabor gefangen und musst den Ausgang finden, indem du den Code knackst.")
    state["raum"].help()
    
    # Spielschleife
    while True:
        # Benutzereingabe abfragen
        command = input(f"{Style.BRIGHT}Befehl eingeben: {Style.RESET_ALL}").strip().lower().split(" ")
        
        if command[0] == "exit":
            # Optionales Code-Argument verarbeiten
            code = None
            if len(command) > 1:
                code = command[1]
                
            success = False
            # Versuch, den Raum zu verlassen
            if code is None:
                # Inventar nutzen, um zu entkommen
                success = state["raum"].exit(state["inventar"])
            else:
                # Mitgelieferten Code zum Verlassen nutzen
                success = state["raum"].exit(code)
            
            # Wenn das Verlassen erfolgreich war, zum nächsten Raum oder Spiel beenden
            if success:
                if state["current_room_index"] + 1 < len(räume):
                    state["current_room_index"] += 1
                    state["raum"] = räume[state["current_room_index"]]
                    print("Du hast den nächsten Raum betreten.")
                    state["raum"].enter()
                else:
                    print("Herzlichen Glückwunsch! Du hast das Spiel erfolgreich abgeschlossen.")
                    break
                
        elif command[0] == "inspect":
            # Optionales Item-Argument verarbeiten
            item = command[1] if len(command) > 1 else None
            
            # Den Raum oder ein spezielles Objekt untersuchen
            state["raum"].inspect(item)
            
        elif command[0] == "use":
            # Überprüfen, ob ein Objekt angegeben wurde
            if len(command) < 2:
                print("Verwendung: use <objekt>")
            else:
                # Das angegebene Objekt benutzen
                item_name = command[1]
                
                # Versuch, das Objekt im Raum zu benutzen
                item = state["raum"].use_interactable(item_name)
                
                # Manche Aktionen geben Items für das Inventar zurück
                if item is not None:
                    if len(item) > 0:
                        state["inventar"].extend(item)
                    
        elif command[0] == "inventory":
            if len(state["inventar"]) == 0:
                print("Dein Inventar ist leer.")
            else:
                print("Dein Inventar enthält:")
                for item in state["inventar"]:
                    print(f"- {item.name}: {item.description}")
        elif command[0] == "jump":
            print("Du bist im folgenden Raum: ", state["raum"].__class__.__name__)
            if len(command) > 1:
                room_index = int(command[1])
                if 0 <= room_index < len(räume):
                    state["current_room_index"] = room_index
                    state["raum"] = räume[room_index]
                    print(f"Du bist zu Raum {room_index} gesprungen.")
                    state["raum"].enter()
                else:
                    print()
                    print("Der Raum existiert nicht.")
            else:
                print("Verwendung: jump <raum_nummer>")
                print("Aktuell gibt es folgende Räume:")
                for idx, raum in enumerate(räume):
                    print(f"- {idx}: {raum.__class__.__name__}")
                print()
        elif command[0] == "help":
            state["raum"].help()
        else:
            print("Unbekannter Befehl. Gib 'help' ein, um eine Liste der Befehle zu sehen.")    
    
if __name__ == "__main__":
    main()