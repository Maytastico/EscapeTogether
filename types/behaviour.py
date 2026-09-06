from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from types.action import Action
    from typing import List

   

class Behaviour():
    def __init__(self, text: str, actions: List["Action"]):
        self.text = text
        self.actions = actions

    def act(self, action_index: int) -> "Behaviour":
        if 0 <= action_index < len(self.actions):
            action = self.actions[action_index]
            return action.behaviour
        else:
            return None

    def __str__(self) -> str:
        return self.text
