from abc import ABC, abstractmethod
class Item(ABC):
    
    def __init__(self, name: str, description: str=""):
        super().__init__()
        self.name: str = name
        self.description: str = description

    
    def inspect(self):
        print(self.description)
