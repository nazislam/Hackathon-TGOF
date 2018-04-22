from items import *
from itemBox import *
from character import *


#hp, level, speed, luck, attack, defense, weapon, armor, boots, attackRange, position, characterType
testCharacter = Character(200, 12, 10, 10, 10, 10, charWeapon, 10, 10, 10, 10, "Archer")
testBox = WeaponBox()
testBox.geneWeapon(testCharacter)
charWeapon = testBox.getWeapon()
testCharacter = Character(200, 12, 10, 10, 10, 10, charWeapon, 10, 10, 10, 10, "Archer")
print(testCharacter.getAttackRange())
print(charWeapon.getAttackRange())