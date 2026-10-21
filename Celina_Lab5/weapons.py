from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name: str, damagescore: int):
        self.name = name
        self.damagescore = damagescore

    @abstractmethod
    def save(self, filename:str) -> None:
        pass

class MeleeWeapon(Weapon):
    def __init__(self, name: str, damagescore: int):
        self.name = name
        self.damagescore = damagescore

    def save(self, filename:str) -> None:
        pass

class RangedWeapon(Weapon):
    def __init__(self, name: str, damagescore: int, range: int):
        self.name = name
        self.damagescore = damagescore
        self.range = range

    def save(self, filename: str) -> None:
        pass

class MagicWeapon(Weapon):
    def __init__(self, name:str, damagescore: int, range: int, manacost: int):
        self.name = name
        self.damagescore = damagescore
        self.range = range
        self.manacost =  manacost

    def save (self, filename:str) -> None:
        pass
