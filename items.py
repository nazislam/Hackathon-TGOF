class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

class Weapon:
    def __init__(self, name, description, level, attack, defense, speed,
                 attRange):
        Item.__init__(self, name, description)
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
    def __init__(self, name, description, level, defense):
        Item.__init__(self, name, description)
        self.level = level
        self.defense = defense

    def getLevel(self):
        return self.level

    def getDefense(self):
        return self.defense

class Boot:
    def __init__(self, name, description, level, speed):
        Item.__init__(self, name, description)
        self.level = level
        self.speed = speed

    def getLevel(self):
        return self.level

    def getSpeed(self):
        return self.speed
