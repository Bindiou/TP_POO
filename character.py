import logging
import random

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """To implement"""
    def __init__(self, name:str, life: float = 100.0, attack: float = 20.0, defense: float = 0.1):
        self._name = name
        self._life = life
        self._attack = attack
        self._defense = defense

    def take_damages(self, damage_value:float):
        damage_taken = damage_value * (1 - self._defense)
        self._life -= damage_taken
    
    def attack(self, target: "Character"):
        target.take_damages(self._attack)

    def __str__(self):
        return f"{self._name} <{self._life:.3f}>"
    
    @property
    def name(self):
        return self._name

    @property
    def is_dead(self):
        return self._life <= 0

class Weapon:
    """To implement"""
    def __init__(self, name:str, attack:float):
        self._name = name
        self.attack = attack
    
    @classmethod
    def default(cls):
        return cls("Wood stick", 1.0)

    @property
    def name(self):
        return self._name


class Warrior(Character):
    """To implement"""
    def __init__(self, name, weapon=None):
        super().__init__(name, life=100 * 1.5, attack=20, defense=0.1 * 1.2)
        self.weapon = weapon if weapon is not None else Weapon.default()
        """self._attack += self.weapon.attack"""

    @property
    def is_raging(self):
        return self._life < (100 * 1.5 * 0.2)
    
    def attack(self, target: "Character"):
        damage = self._attack + self.weapon.attack
        if self.is_raging:
            damage *= 1.2
        target.take_damages(damage)


class Magician(Character):
    """To implement"""
    def __init__(self, name:str):
        super().__init__(name, life=100 * 0.8, attack=20 * 2, defense=0.1)

    def _activate_magical_shield(self):
        return random.random() < 1/3
        """return random.randint(1, 3) == 1"""
        
    def take_damages(self, damage_value: float):
        if self._activate_magical_shield():
            log.debug(f"{self.name} activated magical shield and took no damage!")
            return
        super().take_damages(damage_value)
