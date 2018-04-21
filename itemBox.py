from random import random

class Item:
    def __init__(self, weapon, armor, boot):
        self.weapon = weapon
        self.armor = armor
        self.boot = boot

    def getWeaponBox(self, weaponBox, character):
        self.weaponBox = weaponBox

        weaponName = ""
        for weaponName in len(range(0, 4)):
            if character.getType() == "Archer":
                weaponName = "Arch"
            elif character.getType() == "Mage":
                weaponName = "Staff"
            elif character.getType() == "Knight":
                weaponName = "Sword"
            else:
                weaponName = "Hammer"
        

        weaponLevel = ""
        for weaponLevel in range(1,3):
            if random() < 0.70:
                weaponLevel = "I"
            elif random() < 0.20:
                weaponLevel = "II"
            else:
                weaponLevel = "III"

        weaponBox = {weaponName:weaponLevel}
        return weaponBox
            
        
    def getArmorBox(self, armorBox, character):
        self.armorBox = armorBox

        armorName = ""
        for armorName in len(range(0, 4)):
            if character.getType() == "Archer":
                armorName = "Leather Armor"
            elif character.getType() == "Mage":
                armorName = "Cloth Armor"
            elif character.getType() == "Knight":
                armorName = "Chain Armor"
            else:
                armorName = "Plate Armor"
        

        armorLevel = ""
        for armorLevel in range(1,3):
            if random() < 0.70:
                armorLevel = "I"
            elif random() < 0.20:
                armorLevel = "II"
            else:
                armorLevel = "III"

        armorBox = {armorName:armorLevel}
        return armorBox
    
    def getBootBox(self, bootBox):
        self.bootBox = bootBox

        bootName = "Warboots"

        bootLevel = ""
        for bootLevel in range(1,3):
            if random() < 0.70:
                bootLevel = "I"
            elif random() < 0.20:
                bootLevel = "II"
            else:
                bootLevel = "III"

        bootBox = {bootName:bootLevel}
        return bootBox