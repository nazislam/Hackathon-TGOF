import position

class Character():
    def __init__(self, hp, level, speed, luck, attack, defense, weapon, armor, boots, attackRange, position, characterType):
        self.hp = hp
        self.level = level
        self.speed = speed
        self.luck = luck
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.armor = armor
        self.boots = boots
        self.attackRange = attackRange
        self.position = position
        self.type = characterType



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

    def getDefense(self):
        return self.defense

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

    def getType(self):
        return self.characterType

    def setHp(self, value):
        self.hp = value

    def setLevel(self, value):
        self.level = value

    def setSpeed(self, value):
        self.speed = value

    def setLuck(self, value):
        self.luck = value

    def setAttack(self, value):
        self.attack = value

    def setDefense(self, value):
        self.defend = value

    def setWeapon(self, value):
        self.weapon = value

    def setArmor(self, value):
        self.armor = value

    def setBoots(self, value):
        self.boots = value

    def setRange(self, value):
        self.range = value

    def setPosition(self, value):
        self.position = value


    #####
    def decreaseHp(self, value):
        self.hp -= value

    def increaseHp(self, value):
        self.hp += value

    def useSpellCard(self, spellCard):
        spellCard.applyEffects(self)

    def useMoveCard(self, moveCard):
        moveCard.moveCharacter(character, position)


archer = Character(50, 1, 5, 20, 30, 40, 'arch', 40, 10, 80, Position(3, 6), 'Archer')
mage = Character(30, 2, 5, 20, 34, 40, 'staff', 40, 10, 80, Position(3, 6), 'Mage')
knight = Character(80, 1, 50, 35, 70, 40, 'sword', 40, 0, 80, Position(3, 6), 'Knight')
warrior = Character(50, 3, 10, 20, 30, 40, 'hammer', 40, 10, 80, Position(3, 6), 'Warrior')
