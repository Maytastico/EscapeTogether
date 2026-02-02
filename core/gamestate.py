from typing import List
from template.room import Room
from core.player import Player



class GameState:

    def __init__(self, rooms: list):
        self.rooms: List[Room] = rooms
        self._current_room: int = 0
        self.player = Player("")

        if len(self.rooms) < 1:
            print("Du brauchst mindestens einen Raum zum Spielen")
            print(f"Die übergebene List hat {len(rooms)} Räume")

    def change_room(self, id: int) -> bool:
        if len(self.rooms) - 1 < id:
            return False
        self._current_room = id
        return True

    def next_room(self) -> bool:
        next_room = self._current_room + 1
        return self.change_room(next_room)

    def get_current_room(self) -> "Room":
        """Gibt das Object des aktuellen Raums zurück

        Returns:
            Raum: Referenz des aktuellen Raumobjekts
        """
        return self.rooms[self._current_room]

    def get_room(self, id: int) -> "Room":
        """Gibt den übergebenen Raum zurück

        Args:
            id (int): Nummer des Raums in der Liste

        Returns:
            Raum: Die Referenz des Raumes
        """
        if len(self.rooms)  - 1< id:
            print(f"Raum {id} existiert nicht")
            return None

        return self.rooms[id]
    
    def get_player(self) -> Player:
        return self.player
