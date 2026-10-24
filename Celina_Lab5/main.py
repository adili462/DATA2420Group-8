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
 
    

def main():
    attacker = Fighter("Aisha",100, 5)
    target = Fighter("Celina", 20, 5)
    weapon = MagicWeapon("wand", 5,5,2)
    distance = 5

    attack(attacker, weapon, target, distance)
    print(f'Target Health: {target.health}')
    if target.health < 0:
        print(f'Target has been knocked out')