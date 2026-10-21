from characters import Character, Fighter, Mage
from weapons import Weapon, MeleeWeapon, RangedWeapon, MagicWeapon


def attack(attacker:Character, weapon: Weapon, target: Character, distance: int) -> None:

    if (isinstance(attacker, Fighter)) and (isinstance(weapon, MagicWeapon)):
        raise ValueError(f'Attacker cannot use a magic weapon!')
    
    if (distance > 0) and (isinstance(weapon, MeleeWeapon)):
        raise ValueError(f'Target is too far away to be able to use a melee weapon!')
    
    if weapon.range < distance:
        raise ValueError(f'Target is out of range of the weapon!')

    if isinstance(attacker,Mage):
        if isinstance(weapon, MagicWeapon):
            if attacker.mana < weapon.manacost:
                raise ValueError("Not enough mana for the magic weapon!")
        
    target.health -= weapon.damagescore
    

