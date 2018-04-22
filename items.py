class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description


class Weapon:
    def __init__(self, level, attack, defense, speed, attRange):
        self.level = level
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.attRange = attRange

    def getLevel(self):
        return self.level

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getSpeed(self):
        return self.speed

    def getAttackRange(self):
        return self.attRange

class Armor:
    def __init__(self, armorType, armorLevel, defense):
        self.defense = defense

    def getDefense(self):
        return self.defense


class Boot:
    def __init__(self, bootName, bootLevel, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed
