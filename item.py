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

class Boots:
    def __init__(self, name, description, level, speed):
        Item.__init__(self, name, description)
        self.level = level
        self.speed = speed

    def getLevel(self):
        return self.level

    def getSpeed(self):
        return self.speed

bowLV0 = Weapon("Bow", "Basic Bow for Archer", 0, 1, 0, 0, 0)
bowLV1 = Weapon("Bow", "Great Bow for Archer", 1, 5, 0, 0, 0)
bowLV2 = Weapon("Bow", "Ultra Bow for Archer", 2, 10, 0, 0, 0)
bowLV3 = Weapon("Bow", "Ultimate Bow for Archer", 3, 20, 0, 0, 0)
staffLV0 = Weapon("Staff", "Basic Staff for Mage", 0, 1, 0, 0, 0)
staffLV1 = Weapon("Staff", "Great Staff for Mage", 1, 5, 0, 0, 0)
staffLV2 = Weapon("Staff", "Ultra Staff for Mage", 2, 10, 0, 0, 0)
staffLV3 = Weapon("Staff", "Ultimate Staff for Mage", 3, 20, 0, 0, 0)
swordLV0 = Weapon("Sword", "Basic Sword for Knight", 0, 1, 0, 0, 0)
swordLV1 = Weapon("Sword", "Great Sword for Knight", 1, 5, 0, 0, 0)
swordLV2 = Weapon("Sword", "Ultra Sword for Knight", 2, 10, 0, 0, 0)
swordLV3 = Weapon("Sword", "Ultimate Sword for Knight", 3, 20, 0, 0, 0)
hammerLV0 = Weapon("Hammer", "Basic Hammer for Warrior", 0, 1, 0, 0, 0)
hammerLV1 = Weapon("Hammer", "Great Hammer for Warrior", 1, 5, 0, 0, 0)
hammerLV2 = Weapon("Hammer", "Ultra Hammer for Warrior", 2, 10, 0, 0, 0)
hammerLV3 = Weapon("Hammer", "Ultimate Hammer for Warrior", 3, 20, 0, 0, 0)
