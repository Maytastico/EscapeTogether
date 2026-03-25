from template.interactable import Interactable

class Tisch(Interactable):

    def __init__(self,items):
        super().__init__()
        self.items=items
    def use(self)->list:
        print("Du öffnest die schublade und findest ")
        for item in self.items:
         print(f"- {item.name:}: {item.description}")
        return self.items