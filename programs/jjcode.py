
from template.program import Program

class JJCode(Program):
    def __init__(self):
        super().__init__()
        self.cmd = "jjcode"
        self.name = "JanJansenCode tm"

    def execute(self,pc):
        print("\n Willkommen zu JJCode!")

        print(" Tschüss zu JJCode!\n")