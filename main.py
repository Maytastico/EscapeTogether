from rooms.labor import Labor
from rooms.arbeitszimmer import Arbeitszimmer
from rooms.kitchen import Kitchen
from colorama import init, Style, Fore
from core.gamestate import GameState
import json

# Initialisiert Colorama für farbige Terminal-Ausgaben
init()

# Liste der Räume definieren
# Hier können weitere Räume hinzugefügt werden
räume = [
    Kitchen(),
    Arbeitszimmer(),
    Labor()
]

# Speichert den aktuellen Spielzustand
state = GameState(räume)


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
                    
        elif command[0] == "inv":
            while True:
                # 1. Übersicht anzeigen
                print(f"\n{Fore.CYAN}--- INVENTAR-MANAGEMENT ---{Style.RESET_ALL}")
                
                # Zeige aktuelles Equipment
                print(f"{Style.BRIGHT}Ausrüstung:{Style.RESET_ALL}")
                for slot, item in state.player.equipment.items():
                    name = item.name if item else "Leer"
                    print(f"  {slot.value}: {Fore.GREEN}{name}{Style.RESET_ALL}")
                
                # Zeige aktuelle Stats (basierend auf deiner total_stats property)
                print(f"Stats: {state.player.total_stats}")
                print("-" * 30)

                # Zeige Items im Inventar
                if not state.player.inventory.items:
                    print("Dein Rucksack ist leer.")
                else:
                    print("Items im Rucksack:")
                    for idx, item in enumerate(state.player.inventory.items):
                        print(f"  [{idx}] {item.name}")

                # 2. Untermenü-Eingabe
                print(f"\nOptionen: {Fore.YELLOW}[Nr]{Style.RESET_ALL} Equip, {Fore.YELLOW}'use [Nr]'{Style.RESET_ALL} Use, {Fore.YELLOW}'json [Nr]'{Style.RESET_ALL} Data, {Fore.YELLOW}'exit'{Style.RESET_ALL} Exit")
                sub_cmd = input(f"{Fore.CYAN}Inventar-Aktion >> {Style.RESET_ALL}").strip().lower().split(" ")

                if sub_cmd[0] == "exit":
                    break
                
                # Direkt eine Nummer zum Ausrüsten
                if sub_cmd[0].isdigit():
                    idx = int(sub_cmd[0])
                    if 0 <= idx < len(state.player.inventory.items):
                        item = state.player.inventory.items[idx]
                        # Nutze deine equip-Funktion (die automatisch das Item aus dem Inv nimmt)
                        state.player.equip(item, item.slot)
                    else:
                        print("Ungültiger Index.")

                # Benutzen von Consumables (z.B. Heiltrank)
                elif sub_cmd[0] == "use" and len(sub_cmd) > 1:
                    idx_str = sub_cmd[1]
                    if idx_str.isdigit():
                        idx = int(idx_str)
                        if 0 <= idx < len(state.player.inventory.items):
                            item = state.player.inventory.items[idx]
                            if item.properties.interactable:
                                item.interact(state)
                            else:
                                print("Dieses Item kann man nicht benutzen.")
                    else:
                        print("Bitte gib eine Nummer an, z.B. 'use 0'")
            
                elif sub_cmd[0] == "json" and len(sub_cmd) > 1:
                    idx_str = sub_cmd[1]
                    if idx_str.isdigit():
                        idx = int(idx_str)
                        if 0 <= idx < len(state.player.inventory.items):
                            item = state.player.inventory.items[idx]
                            
                            # Helper-Funktion um Enums und komplexe Objekte JSON-tauglich zu machen
                            def json_default(obj):
                                if hasattr(obj, "__dict__"):
                                    return vars(obj)
                                if hasattr(obj, "value"): # Für Enums (EquipmentSlot, ItemType)
                                    return str(obj.value)
                                return str(obj)

                            # Objekt in formatierten String umwandeln
                            item_json = json.dumps(item, default=json_default, indent=4, ensure_ascii=False)
                            
                            print(f"\n{Fore.MAGENTA}--- ITEM DATA (JSON) ---{Style.RESET_ALL}")
                            print(item_json)
                            print(f"{Fore.MAGENTA}------------------------{Style.RESET_ALL}")
                        else:
                            print("Ungültiger Index.")

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