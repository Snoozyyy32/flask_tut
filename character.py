from weapon import fists
from health_bar import Health_bar

class Character:
    race = "human"

    def __init__(self, name: str, health: float) -> None:
        self.name = name
        self.health = health
        self.max_health  = health
        self.weapon= fists

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} delt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")
        

class Hero(Character):
    def __init__(self, name: str, health: float) -> None:
        super().__init__(name, health)
    
        self.default_weapon = self.weapon
        self.health_bar = Health_bar(self, colour="blue")

    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} eqquiped an {self.weapon.name}!")

    def droped_weapon(self):
        self.weapon = self.default_weapon

class Enemy(Character):
    def __init__(self, name: str, health: float, weapon) -> None:
        super().__init__(name, health)

        self.weapon = weapon
        self.health_bar = Health_bar(self, colour="red")