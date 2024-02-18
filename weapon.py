class Weapon:
    def __init__(self,name: str, weapon_type: str, damage: float,value: float) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        pass


iron_sword = Weapon("Iron sword", "Sharp", 5, 10)
short_bow = Weapon("Short bow", "ranged", 4, 8)
fists = Weapon("Fists","blunt", 2, 0)