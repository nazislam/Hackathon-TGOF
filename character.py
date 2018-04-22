import random

from position import Position
import card
import maps
from item import *


def createAcher():
    x = random.randint(0, maps.maxx - 1)
    y = random.randint(0, maps.maxy - 1)
    return Character(50, 1, 5, 20, 30, 40, 4, Position(3, 6), 'Archer')


def createMage():
    x = random.randint(0, maps.maxx)
    y = random.randint(0, maps.maxy)
    return Character(100, 2, 5, 20, 34, 40, 40, Position(6, 7), 'Mage')


def createKnight():
    x = random.randint(0, maps.maxx)
    y = random.randint(0, maps.maxy)
    return Character(80, 1, 50, 35, 70, 40, 40, Position(x, y), 'Knight')


def createWarrior():
    x = random.randint(0, maps.maxx)
    y = random.randint(0, maps.maxy)
    return Character(50, 3, 10, 20, 30, 40, 40, Position(x, y), 'Warrior')

class Character():
    def __init__(self, hp, level, speed, luck, attack, defense, attackRange, position, characterType):
        self.hp = hp
        self.level = level
        self.speed = speed
        self.luck = luck
        self.attack = attack
        self.defense = defense
        self.attackRange = attackRange
        self.position = position
        self.type = characterType
        self.hand = []
        for i in range(6):
            self.addCard(card.generateCard())
        self.buff = [] #Store Spell Cards

        if self.type == "Archer":
            self.weapon = Weapon("Bow", "", 0, 0, 0, 0, 10)
            self.armor = Armor("Leather Armor", "", 0, 0)
            self.boots = Boots("Warboots", "", 0, 0)
        elif self.type == "Mage":
            self.weapon = Weapon("Staff", "", 0, 0, 0, 0, 5)
            self.armor = Armor("Cloth Armor", "", 0, 0)
            self.boots = Boots("Warboots", "", 0, 0)
        elif self.type == "Knight":
            self.weapon = Weapon("Sword", "", 0, 0, 0, 0, 1)
            self.armor = Armor("Chain Armor", "", 0, 0)
            self.boots = Boots("Warboots", "", 0, 0)
        else:
            self.weapon = Weapon("Hammer", "", 0, 0, 0, 0, 1)
            self.armor = Armor("Plate Armor", "", 0, 0)
            self.boots = Boots("Warboots", "", 0, 0)

    """def genereateMoveCards(self, numOfCards):
        fs = open('./card_catalog/moveCard', 'r')
        f1 = fs.readlines()
        for i in numOfCards:
            for j in f1:
                x = fs.split('|')
                self.name = x[0]
                self.step = x[1]
                self.description = x[2]"""

    def addCard(self, card):
        self.hand.append(card)

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
        return self.attackRange + buffAttackRange + self.weapon.getAttackRange()
    
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
        rangemv = moveCard.getStep() + self.getSpeed()
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
                if terrain.get_terrain().get_type() == "Mount" or terrain.get_type() == "Player" or terrain.get_type() == "Card":
                    passed.append(new_position)
                elif terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step <= rangemv - 1:
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
                if terrain.get_terrain().get_type() == "Mount" or terrain.get_type() == "Player" or terrain.get_type() == "Card":
                    passed.append(new_position)
                elif terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step <= rangemv - 1:
                    passed.append(new_position)
                    elements.append(new_position)
                    steps.append(rangemv)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                    top += 1
            tryx = position.getx() - 1
            tryy = position.gety()
            new_position = Position(tryx, tryy)
            if tryx >= 0 and tryx < map.maxx and tryy >= 0 and tryy < map.maxy and not(new_position in passed):
                terrain = map.coordinate[tryx][tryy]
                if terrain.get_terrain().get_type() == "Mount" or terrain.get_type() == "Player" or terrain.get_type() == "Card":
                    passed.append(new_position)
                elif terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step <= rangemv - 1:
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
                if terrain.get_terrain().get_type() == "Mount" or terrain.get_type() == "Player" or terrain.get_type() == "Card":
                    passed.append(new_position)
                elif terrain.get_terrain().get_type() == "Grass" and cur_step + 1 <= rangemv:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step + 2 <= rangemv:
                    passed.append(new_position)
                    elements.append(new_position)
                    top += 1
                    steps.append(cur_step + 2)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                elif terrain.get_terrain().get_type() == "Swamp" and cur_step <= rangemv - 1:
                    passed.append(new_position)
                    elements.append(new_position)
                    steps.append(rangemv)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
                    top += 1
            bottom += 1
        file = open("map2/map_move.txt", "w")
        for i in modified_map:
            file.write(i)
        return elements

    def useMoveCard(self, moveCard, map):
        places = self.find_where_can_go(moveCard, map)
        cant_go = []
        for i in range(1, len(places)):
            pos = places[i]
            x = pos.x
            y = pos.y
            if map.coordinate[x][y].get_type() == "Player":
                cant_go.append(Position(x, y))
        print("You can't go to", len(cant_go), "points")
        for i in cant_go:
            print(i)
        x, y = input("please enter the coordinate you want to go to").strip().split()
        x = int(x)
        y = int(y)
        desired_position = Position(x, y)
        map.coordinate[self.getPosition().x][self.getPosition().y].terrain.stepable = True
        map.coordinate[x][y].terrain.stepable = True
        if map.coordinate[x][y].get_type() == "Card":
            self.addCard(map.coordinate[x][y].get_obj())
            map.coordinate[x][y].set_obj(None, "nothing")
        self.setPosition(desired_position)

    def useSpellCard(self,card):
        self.buff.append(card)
        if card.getHp() != 0: # Gain/lose HP from the Spell Card
            self.setHp(self.getHp() + card.getHp())

    def find_where_can_attack(self, map):
        rangeatk = self.getAttackRange()
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
            char = "0"
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                if cur_step + 1 <= rangeatk:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
            tryx = position.getx()
            tryy = position.gety() + 1
            new_position = Position(tryx, tryy)
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                if cur_step + 1 <= rangeatk:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
            tryx = position.getx() - 1
            tryy = position.gety()
            new_position = Position(tryx, tryy)
            if tryx >= 0 and tryx < map.maxx and tryy >= 0 and tryy < map.maxy and not(new_position in passed):
                if cur_step + 1 <= rangeatk:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
            tryx = position.getx()
            tryy = position.gety() - 1
            new_position = Position(tryx, tryy)
            if tryx > 0 and tryx < map.maxx and tryy > 0 and tryy < map.maxy and not(new_position in passed):
                if cur_step + 1 <= rangeatk:
                    passed.append(new_position)
                    top += 1
                    elements.append(new_position)
                    steps.append(cur_step + 1)
                    modified_map[tryx] = modified_map[tryx][:tryy - 1] + "0" + modified_map[tryx][tryy:]
            bottom += 1
        file = open("map2/map_attack.txt", "w")
        for i in modified_map:
            file.write(i)
        return elements

    def useAttackCard(self, card, map):
        places = self.find_where_can_attack(map)
        atk = card.getAttack() + self.getAttack()
        can_attack = []
        for i in range(1, len(places)):
            pos = places[i]
            x = pos.x
            y = pos.y
            if map.coordinate[x][y].get_type() == "Player":
                can_attack.append(Position(x, y))
        print("You can attack", len(can_attack), "targer")
        for i in can_attack:
            print(i)
        x, y = input("please enter the coordinate you want to attack").strip().split()
        x = int(x)
        y = int(y)
        obj = map.coordinate[x][y].get_obj()
        obj.setHp(obj.getHp() - atk)