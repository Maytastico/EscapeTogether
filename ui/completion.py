from typing import TYPE_CHECKING, List
from prompt_toolkit.completion import Completer, Completion

if TYPE_CHECKING:
    from core.gamestate import GameState
    from interactables.terminal import Terminal


class GameCompleter(Completer):
    """Vervollständigt die Hauptbefehle sowie die Namen von Interactables/NPCs
    des aktuellen Raums (z.B. 'use fun<TAB>' -> 'use funkgerät')."""

    COMMANDS = ["inspect", "use", "talk", "inv", "exit", "back", "quit", "help", "jump"]

    def __init__(self, state: "GameState"):
        self.state = state

    def get_completions(self, document, complete_event):
        words = document.text_before_cursor.split(" ")

        if len(words) <= 1:
            word = words[0] if words else ""
            for cmd in self.COMMANDS:
                if cmd.startswith(word.lower()):
                    yield Completion(cmd, start_position=-len(word))
            return

        command = words[0].lower()
        current_word = words[-1]
        room = self.state.get_current_room()

        options: List[str] = []
        if command in ("inspect", "use"):
            options = list(room.interactables.keys())
        elif command == "talk":
            options = list(room.npcs.keys())
        elif command == "jump":
            options = [str(i) for i in range(len(self.state.rooms))]

        for option in options:
            if option.lower().startswith(current_word.lower()):
                yield Completion(option, start_position=-len(current_word))


class TerminalCompleter(Completer):
    """Vervollständigt Befehle sowie Ordner-/Dateinamen innerhalb eines Terminal-Interactables."""

    COMMANDS = ["ls", "cd", "pwd", "cat", "help", "exit"]

    def __init__(self, terminal: "Terminal"):
        self.terminal = terminal

    def get_completions(self, document, complete_event):
        words = document.text_before_cursor.split(" ")

        if len(words) <= 1:
            word = words[0] if words else ""
            for cmd in self.COMMANDS:
                if cmd.startswith(word.lower()):
                    yield Completion(cmd, start_position=-len(word))
            return

        command = words[0].lower()
        current_word = words[-1]
        entries = self.terminal.files.get(self.terminal.path, [])

        options: List[str] = []
        if command == "cd":
            options = [".."] + [name[1:] for name in entries if name.startswith("/")]
        elif command == "cat":
            options = [name for name in entries if not name.startswith("/")]

        for option in options:
            if option.lower().startswith(current_word.lower()):
                yield Completion(option, start_position=-len(current_word))
