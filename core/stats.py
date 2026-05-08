class Stats:
    def __init__(self, hp: int = 0, strength: int = 0, defense: int = 0, speed: int = 0, bananig: bool = False):
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.bananig = bananig

    def __add__(self, other: 'Stats'):
        """Ermöglicht das Addieren von zwei Stats-Objekten: stats1 + stats2"""
        if not self.bananig:
            banana = other.bananig
        else:
            banana = True
        return Stats(
            hp=self.hp + other.hp,
            strength=self.strength + other.strength,
            defense=self.defense + other.defense,
            speed=self.speed + other.speed,
            bananig=banana
        )

    def __repr__(self):
        return f"Stats(HP: {self.hp}, STR: {self.strength}, DEF: {self.defense}, SPD: {self.speed}, BANANIG {self.bananig})"
