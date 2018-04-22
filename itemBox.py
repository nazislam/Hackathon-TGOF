from item import *
import random

def generateBox():
    chance = random.randint(0, 100) % 3
    if chance == 0:
        return WeaponBox()
    elif chance == 1:
        return ArmorBox()
    else:
        return bootsBox()

class Box:
    def __init__(self):
        pass

    def generate(self):
        pass


class WeaponBox(Box):
    def __init__(self):
        self.weapon = "Has Not Been Generated"
        self.type = "Weapon"

    def getWeapon(self):
        return self.weapon

    def setWeapon(self, weapon):
        self.weapon = weapon

    def generate(self, character):
        weaponDict = {
            "Archer": "Bow",
            "Mage": "Staff",
            "Knight": "Sword",
            "Warrior": "Hammer"
        }

        characterType = character.getType()
        weaponName = weaponDict[characterType]

        """
        if characterType == "Archer":
            weaponType = "Bow"
        elif characterType == "Mage":
            weaponType = "Staff"
        elif characterType == "Knight":
            weaponType = "Sword"
        else:
            weaponType = "Hammer"
        """

        weaponLevel = 0
        
        random_level = random.random()
        if random_level < 0.70:
            weaponLevel = 1
        elif 0.70 < random_level and random_level < 0.90:
            weaponLevel = 2
        else:
            weaponLevel = 3

        if weaponName == "Bow":
            if weaponLevel == 1:
                weapon = bowLV1
            elif weaponLevel == 2:
                weapon = bowLV2
            elif weaponLevel == 3:
                weapon = bowLV3

        if weaponName == "Staff":
            if weaponLevel == 1:
                weapon = staffLV0
            elif weaponLevel == 2:
                weapon = staffLV2
            elif weaponLevel == 3:
                weapon = staffLV3

        if weaponName == "Sword":
            if weaponLevel == 1:
                weapon = swordLV1
            elif weaponLevel == 2:
                weapon = swordLV2
            elif weaponLevel == 3:
                weapon = swordLV3

        if weaponName == "Hammer":
            if weaponLevel == 1:
                weapon = hammerLV1
            elif weaponLevel == 2:
                weapon = hammerLV2
            elif weaponLevel == 3:
                weapon = hammerLV3

        self.setWeapon(weapon)


class ArmorBox(Box):
    def __init__(self):
        self.armor = "Has Not Been Generated"
        self.type = "Armor"

    def getArmor(self):
        return self.armor

    def setArmor(self, armor):
        self.armor = armor

    def generate(self, character):
        armorDict = {
            "Archer": "Leather Armor",
            "Mage": "Cloth Armor",
            "Knight": "Chain Armor",
            "Warrior": "Plate Armor"
        }

        characterType = character.getType()
        armorName = armorDict[characterType]


        """
        if characterType == "Archer":
            armorName = "Leather Armor"
        elif characterType == "Mage":
            armorName = "Cloth Armor"
        elif characterType == "Knight":
            armorName = "Chain Armor"
        else:
            armorName = "Plate Armor"
        """

        armorLevel = 0
        
        random_level = random.random()
        if random_level() < 0.70:
            armorLevel = 1
        elif 0.70 < random_level and random_level < 0.90:
            armorLevel = 2
        else:
            armorLevel = 3

        if armorName == "Leather Armor":
            if armorLevel == 1:
                armor = Armor(armorName, armorLevel, "Great Leather Armor for Archer",5)
            elif armorLevel == 2:
                armor = Armor(armorName, armorLevel, "Ultra Leather Armor for Archer",6)
            elif armorLevel == 3:
                armor = Armor(armorName, armorLevel, "Ultimate Leather Armor for Archer",7)

        if armorName == "Cloth Armor":
            if armorLevel == 1:
                armor = Armor(armorName, armorLevel, "Great Cloth Armor for Mage",3)
            elif armorLevel == 2:
                armor = Armor(armorName, armorLevel, "Ultra Cloth Armor for Mage",4)
            elif armorLevel == 3:
                armor = Armor(armorName, armorLevel, "Ultimate Cloth Armor for Mage",5)

        if armorName == "Chain Armor":
            if armorLevel == 1:
                armor = Armor(armorName, armorLevel, "Great Chain Armor for Knight",7)
            elif armorLevel == 2:
                armor = Armor(armorName, armorLevel, "Ultra Chain Armor for Knight",8)
            elif armorLevel == 3:
                armor = Armor(armorName, armorLevel, "Ultimate Chain Armor for Knight",9)

        if armorName == "Plate Armor":
            if armorLevel == 1:
                armor = Armor(armorName, armorLevel, "Great Plate Armor for Warrior",9)
            elif armorLevel == 2:
                armor = Armor(armorName, armorLevel, "Ultra Plate Armor for Warrior",10)
            elif armorLevel == 3:
                armor = Armor(armorName, armorLevel, "Ultimate Plate Armor for Warrior",11)

        self.setArmor(armor)


class bootsBox(Box):
    def __init__(self):
        self.boots = "Has Not Been Generated"
        self.type = "Boots"

    def getBoots(self):
        return self.boots

    def setBoots(self, boots):
        self.boots = boots

    def generate(self, character):

        bootsName = "Warboots"
        bootsLevel = 0
        
        random_level = random.random()
        if random_level() < 0.70:
            bootsLevel = 1
        elif 0.70 < random_level and random_level < 0.90:
            bootsLevel = 2
        else:
            bootsLevel = 3

        if bootsLevel == 1:
            boots = Boots(bootsName, bootsLevel, "Great Boots for the Character",3)
        elif bootsLevel == 2:
            boots = Boots(bootsName, bootsLevel, "Ultra Boots for the Character",5)
        elif bootsLevel == 3:
            boots = Boots(bootsName, bootsLevel, "Ultimate Boots for the Character",7)

        self.setBoots(boots)