from template.programdisk import ProgramDisk
from programs.jjcode import JJCode
from colorama import *
from core.gamestate import GameState
from time import sleep as s

class JJCodeDisk(ProgramDisk): # "Code" auf Codiert

    def __init__(self):
        super().__init__(
            program=JJCode
        )
        self.name = "JanJansenCode tm"
    def interact(self, state: "GameState"):
        super().interact(state)
