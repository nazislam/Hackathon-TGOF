from items import *
from itemBox import *
from character import *


#hp, level, speed, luck, attack, defense, weapon, armor, boots, attackRange, position, characterType
testCharacter = Character(200, 12, 0, 0, 0, 0, "Bow", 0, 0, 0, 0, "Archer")
testBox = WeaponBox()
testBox.geneWeapon(testCharacter)
charWeapon = testBox.getWeapon()

print(charWeapon.getAttack())