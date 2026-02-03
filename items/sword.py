from template.weapon import Weapon

class Sword(Weapon):

    def __init__(self):
        super().__init__(
            name="Schwert", 
            description="Ein langes und scharfes Schwert",
            attack_power=10
        )