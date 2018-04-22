from items import *
from itemBox import *
from character import *


#hp, level, speed, luck, attack, defense, weapon, armor, boots, attackRange, position, characterType
#def __init__(self, hp, level, speed, luck, attack, defense, attackRange, position, characterType):
testCharacter = Character(200, 12, 10, 10, 10, 10, 10, 10, "Archer")

testBox = WeaponBox()
testBox.geneWeapon(testCharacter)
charWeapon = testBox.getWeapon()

testCharacter.setWeapon(charWeapon)
print(testCharacter.getAttackRange())
print(charWeapon.getAttackRange())