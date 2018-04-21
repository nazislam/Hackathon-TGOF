from position import Position
<<<<<<< HEAD
from card import Card, moveCard, spellCard
import file
import random
=======
import card
import maps
>>>>>>> a31fb51ba52a946e84efb5e901d5d2b429d04cd7

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
        self.buff = [] #Store Spell Cards
        self.hand = [  ]

    def genereateMoveCards(numOfCards):
      fs = open('./card_catalog/moveCard', 'r')
      f1 = fs.readlines()
      for i in numOfCards:
          for j in f1:
              x = fs.split('|')
              self.name = x[0]
              self.step = x[1]
              self.description = x[2]

    # getter functions
    def getHp(self):
        return self.hp

    def getLevel(self):
        return self.level

    def getLuck(self):
        buffLuck = 0
        for spell in self.buff:
            buffLuck += spell.getLuck()
        return self.luck + buffLuck

    def getAttack(self):
        buffAttack = 0
        for spell in self.buff:
            buffAttack += spell.getAttack()
        return self.attack + self.weapon.getAttack() + buffAttack

    def getDefense(self):
        buffDefense = 0
        for spell in self.buff:
            buffDefense += spell.getDefense()
        return self.defense + self.armor.getDefense() + buffDefense
    
    def getSpeed(self):
        buffSpeed = 0
        for spell in self.buff:
            buffSpeed += spell.getSpeed()
        return self.speed + self.boots.getSpeed() + buffSpeed

    def getWeapon(self):
        return self.weapon

    def getArmor(self):
        return self.armor
    
    def getBoots(self):
        return self.boots

    def getAttackRange(self):
        buffAttackRange = 0
        for spell in self.buff:
            buffAttackRange += spell.getAttackRange()
        return self.range + buffAttackRange
    
    def getPosition(self):
        return self.position

    def getType(self):
        return self.type

    #Setters
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

    def find_where_can_go(self, moveCard, map):
        rangemv = moveCard.getStep()
        position = self.getPosition()
        passed = []
        passed.append(position)
        elements = [position]
        steps = [0]
        top = 1
        bottom = 0
        modified_map = map.get_map()
        while bottom < top:
            position = elements[bottom]
            cur_step = steps[bottom]
            tryx = position.getx() + 1
            tryy = position.gety()
            new_position = Position(tryx, tryy)
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                terrain = map.coordinate[tryx][tryy]
                if terrain.get_terrain().get_type() == "Mount":
                    passed.append(new_position)
                if terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step <= 9:
                    passed.append(new_position)
                    elements.append(new_position)
                    steps.append(rangemv)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                    top += 1
            tryx = position.getx()
            tryy = position.gety() + 1
            new_position = Position(tryx, tryy)
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                terrain = map.coordinate[tryx][tryy]
                if terrain.get_terrain().get_type() == "Mount":
                    passed.append(new_position)
                if terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step <= 9:
                    passed.append(new_position)
                    elements.append(new_position)
                    steps.append(rangemv)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                    top += 1
            tryx = position.getx() - 1
            tryy = position.gety()
            new_position = Position(tryx, tryy)
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                terrain = map.coordinate[tryx][tryy]
                if terrain.get_terrain().get_type() == "Mount":
                    passed.append(new_position)
                if terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step <= 9:
                    passed.append(new_position)
                    elements.append(new_position)
                    steps.append(rangemv)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                    top += 1
            tryx = position.getx()
            tryy = position.gety() - 1
            new_position = Position(tryx, tryy)
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                terrain = map.coordinate[tryx][tryy]
                if terrain.get_terrain().get_type() == "Mount":
                    passed.append(new_position)
                if terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                if terrain.get_terrain().get_type() == "Swamp" and cur_step <= 9:
                    passed.append(new_position)
                    elements.append(new_position)
                    steps.append(rangemv)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                    top += 1
            bottom += 1
        file = open("maps/map2.txt", "w")
        for i in modified_map:
            file.write(i)
            file.write("\n")


    def useMoveCard(self, moveCard, map):
        self.find_where_can_go(moveCard, map)



    def useCard(self,card):
        if card.getType() == "Spell Card":
            self.buff.append(card)
            if card.getHp() != 0: # Gain/lose HP from the Spell Card
                self.setHp(self.getHp() + card.getHp())
        else:
            self.useMoveCard(card)


archer = Character(50, 1, 5, 20, 30, 40, 'arch', 40, 10, 80, Position(3, 6), 'Archer')
mage = Character(30, 2, 5, 20, 34, 40, 'staff', 40, 10, 80, Position(3, 6), 'Mage')
knight = Character(80, 1, 50, 35, 70, 40, 'sword', 40, 0, 80, Position(3, 6), 'Knight')
warrior = Character(50, 3, 10, 20, 30, 40, 'hammer', 40, 10, 80, Position(3, 6), 'Warrior')
