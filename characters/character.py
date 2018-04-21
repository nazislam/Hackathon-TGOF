import position

class Character():
    def __init__(self, hp, level, speed, luck, attack, defend, weapon, armor, boots, attackRange, position):
        self.hp = hp
        self.level = level
        self.speed = speed
        self.luck = luck
        self.attack = attack
        self.defend = defend
        self.weapon = weapon
        self.armor = armor
        self.boots = boots
        self.attackRange = attackRange
        self.position = position


    # getter functions
    def getHp(self):
        return self.hp

    def getLevel(self):
        return self.level

    def getSpeed(self):
        return self.speed

    def getLuck(self):
        return self.luck

    def getAttack(self):
        return self.attack

    def getDefence(self):
        return self.defence

    def getWeapon(self):
        return self.weapon

    def getArmor(self):
        return self.armor
    
    def getBoots(self):
        return self.boots
    
    def getRange(self):
        return self.range
    
    def getPosition(self):
        return self.position

    # other functions
    def decreasePower(self, value):
        self.hp -= value

    def increasePower(self, value):
        self.hp += value

    def useSpellCard(self, spellCard):
        spellCard.applyEffects(self)

    def useMoveCard(self, moveCard):
        moveCard.moveCharacter(character, position)


archer = Character(50, 1, 5, 20, 30, 40, 'arch', 40, 10, 80, Position(3, 6))
mage = Character(30, 2, 5, 20, 34, 40, 'staff', 40, 10, 80, Position(3, 6))
knight = Character(80, 1, 50, 35, 70, 40, 'sword', 40, 0, 80, Position(3, 6))
warrior = Character(50, 3, 10, 20, 30, 40, 'hammer', 40, 10, 80, Position(3, 6))
