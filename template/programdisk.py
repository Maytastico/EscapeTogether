
from template.disk import Disk
from template.program import Program
from time import sleep as s

class ProgramDisk(Disk):

    def __init__(self,program:Program):
        super().__init__(
            name="Programm Disk",
            description="Eine Disk für das installieren von Programmen"
        )
        self.program = program

    def play(self,pc):
        print()

        has_program = False
        for i in pc.programs:
            if isinstance(i,self.program):
                has_program = True
        
        if has_program:
            print(f"{self.program().name} already installed!")
        else:
            print(f"Installing {self.program().name} ...")
            s(0.5)

            for i in range(0,11):
                print(f"[{"#"*i}{"."*(10-i)}] {i*10}%")
                s(1)
            
            s(1)
            print(f"Finished installing {self.program().name} !")
            pc.programs.append(self.program())

        print()