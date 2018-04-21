from character import Character
from item import Item

class Weapon(Item):
    def __init__ (self, attRange, attack, speed, defend):
        Character.__init__(self, attack,)

        self.attRange = attRange
        self.attack = attack
        self.speed = speed
        self.defend = defend
    
    def recArch(self, Character):
        pass
    def recStaff(self, Character):
        pass
    def recSword(self, Character):
        pass
    def recHammer(self, Charcter):
        pass
    