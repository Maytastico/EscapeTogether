from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.stats import Stats
    from core.player import Player
    from types.behaviour import Behaviour

class Action:
    def __init__(self, text: str, behaviour: 'Behaviour' = None):
        """Inizialisiert eine Aktion mit einem Text welcher die Aktion, die der Spieler ausführt beschreibt.
        Auf jede Aktion folgt ein Verhalten was die Reaktion des NPCs auf die Aktion beschreibt.
        Diese kann auch eine weitere Frage auf die Aktion des Spielers sein.
        Args:
            text (str): Der Text, der die Aktion beschreibt.
            behaviour (Behaviour, optional): Das Verhalten des NPCs nach der Aktion. Defaults to None.
        """
        self.text = text
        self.behaviour = behaviour

    def __str__(self):
        """
        Printet man die Aktion, wird der Text der Aktion zurückgegeben.
        """
        return self.text

    def is_action_performable(self, player: 'Player') -> bool:
        """Überprüft, ob die Aktion ausgeführt werden kann. Standardmäßig immer ausführbar."""
        return True
    

class StatBasedAction(Action):
    def __init__(self, text: str, behaviour: 'Behaviour' = None, stat: "Stats" = None, threshold: int = 0):
        """Initialisiert eine Aktion, die nur mit einem bestimmten Statwert des Spielers ausgeführt werden kann.
        Args:
            text (str): Der Text, der die Aktion beschreibt.
            behaviour (Behaviour, optional): Das Verhalten des NPCs nach der Aktion. Defaults to None.
            stat (Stats, optional): Der Statwert, der überprüft werden soll. Defaults to None.
            threshold (int, optional): Der Schwellenwert, den der Statwert erreichen muss, um die Aktion auszuführen. Defaults to 0.
        """
        super().__init__(text, behaviour)
        self.stat = stat
        self.threshold = threshold

    def is_action_performable(self, player):
        """Überprüft, ob die Aktion ausgeführt werden kann, basierend auf dem Statwert des Spielers."""
        if not super().is_action_performable(player):
            return False
        return getattr(player, self.stat) >= self.threshold