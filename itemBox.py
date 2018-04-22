from items import Weapon
from items import Armor
from items import Boot
from random import random

class WeaponBox:
    def __init__(self):
        self.weapon = "Has Not Been Generated"
        self.type = "Weapon"

    def getWeapon(self):
        return self.weapon

    def geneWeapon(self, character):

        weaponType = ""
        weapon = ""
        if character.getType() == "Archer":
            weaponType = "Bow"
        elif character.getType() == "Mage":
            weaponType = "Staff"
        elif character.getType() == "Knight":
            weaponType = "Sword"
        else:
            weaponType = "Hammer"
        

        weaponLevel = ""
        for weaponLevel in range(1,3):
            random_level = random()
            if random_level < 0.70:
                weaponLevel = "I"
            elif 0.70 < random_level and random_level < 0.90:
                weaponLevel = "II"
            else:
                weaponLevel = "III"

        if weaponType == "Bow":
            if weaponLevel == "I":
                weapon = Weapon(weaponType, weaponLevel, 5, 0, 0, 0)
            elif weaponLevel == "II":
                weapon = Weapon(weaponType, weaponLevel, 10, 0, 0, 0)
            elif weaponLevel == "III":
                weapon = Weapon(weaponType, weaponLevel, 15, 0, 0, 0)

        if weaponType == "Staff":
            if weaponLevel == "I":
                weapon = Weapon(weaponType, weaponLevel, 5, 0, 0, 0)
            elif weaponLevel == "II":
                weapon = Weapon(weaponType, weaponLevel, 10, 0, 0, 0)
            elif weaponLevel == "III":
                weapon = Weapon(weaponType, weaponLevel, 15, 0, 0, 0)

        if weaponType == "Sword":
            if weaponLevel == "I":
                weapon = Weapon(weaponType, weaponLevel, 5, 0, 0, 0)
            elif weaponLevel == "II":
                weapon = Weapon(weaponType, weaponLevel, 10, 0, 0, 0)
            elif weaponLevel == "III":
                weapon = Weapon(weaponType, weaponLevel, 15, 0, 0, 0)      

        if weaponType == "Hammer":
            if weaponLevel == "I":
                weapon = Weapon(weaponType, weaponLevel, 5, 0, 0, 0)
            elif weaponLevel == "II":
                weapon = Weapon(weaponType, weaponLevel, 10, 0, 0, 0)
            elif weaponLevel == "III":
                weapon = Weapon(weaponType, weaponLevel, 15, 0, 0, 0)  

        self.weapon = weapon


class ArmorBox:
    def __init__(self, armor):
        self.armor = "Has Not Been Generated"
        self.type = "Armor"

    def getArmor(self):
        return self.armor
    
    def geneArmor(self, character):

        armorType = ""
        armor = ""
        if character.getType() == "Archer":
            armorType = "Leather Armor"
        elif character.getType() == "Mage":
            armorType = "Cloth Armor"
        elif character.getType() == "Knight":
            armorType = "Chain Armor"
        else:
            armorType = "Plate Armor"
        

        armorLevel = ""
        for armorLevel in range(1,3):
            random_level = random()
            if random_level() < 0.70:
                armorLevel = "I"
            elif 0.70 < random_level and random_level < 0.90:
                armorLevel = "II"
            else:
                armorLevel = "III"

        if armorType == "Leather Armor":
            if armorLevel == "I":
                armor = Armor(armorType, armorLevel, 5)
            elif armorLevel == "II":
                armor = Armor(armorType, armorLevel, 6)
            elif armorLevel == "III":
                armor = Armor(armorType, armorLevel, 7)

        if armorType == "Cloth Armor":
            if armorLevel == "I":
                armor = Armor(armorType, armorLevel, 3)
            elif armorLevel == "II":
                armor = Armor(armorType, armorLevel, 4)
            elif armorLevel == "III":
                armor = Armor(armorType, armorLevel, 5)

        if armorType == "Chain Armor":
            if armorLevel == "I":
                armor = Armor(armorType, armorLevel, 7)
            elif armorLevel == "II":
                armor = Armor(armorType, armorLevel, 8)
            elif armorLevel == "III":
                armor = Armor(armorType, armorLevel, 9)      

        if armorType == "Plate Armor":
            if armorLevel == "I":
                armor = Armor(armorType, armorLevel, 9)
            elif armorLevel == "II":
                armor = Armor(armorType, armorLevel, 10)
            elif armorLevel == "III":
                armor = Armor(armorType, armorLevel, 11)  

        self.armor = armor


class BootBox:
    def __init__(self, boot):
        self.armor = "Has Not Been Generated"
        self.type = "Armor"

    def getBoot(self):
        return self.boot   

    def geneBoot(self, character):


        bootName = "Warboots"

        bootLevel = ""
        for bootLevel in range(1,3):
            random_level = random()
            if random_level() < 0.70:
                bootLevel = "I"
            elif 0.70 < random_level and random_level < 0.90:
                bootLevel = "II"
            else:
                bootLevel = "III"

        if bootLevel == "I":
            boot = Boot(bootName, bootLevel, 3)
        elif bootLevel == "II":
            boot = Boot(bootName, bootLevel, 5)
        elif bootLevel == "III":
            boot = Boot(bootName, bootLevel, 7)

        self.boot = boot