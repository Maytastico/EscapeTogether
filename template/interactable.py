from abc import ABC, abstractmethod
class Interactable(ABC):
    
    @abstractmethod
    def use(self):
        pass
    
    @abstractmethod
    def inspect(self):
        pass
