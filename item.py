import sys
sys.path.insert(0, './Hackathon-TGOF/characters') 
from character.py import Character
from random import random

class Item(Character):
    def __init__(self, weapon, armor, boot):
        Character.__init__(self,character)
        self.weapon = weapon
        self.armor = armor
        self.boot = boot
        self.character = character


    def getWeaponBox(self, weaponBox):
        self.weaponBox = weaponBox

        weaponName = ""
        for weaponName in len(range(0, 4)):
            if character == "Archer":
                weaponName = "Arch"
            elif character == "Mage":
                weaponName = "Staff"
            elif character == "Knight":
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
            
        
    def getArmorBox(self, armorBox):
        self.armorBox = armorBox

        armorName = ""
        for armorName in len(range(0, 4)):
            if character == "Archer":
                armorName = "Leather Armor"
            elif character == "Mage":
                armorName = "Cloth Armor"
            elif character == "Knight":
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