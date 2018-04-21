#import Position
from card import Card


class MoveCard(Card):
    def __init__(self, name, description, step):
        Card.__init__(self, name, description)
        self.step = step


    def getStep(self):
        return self.step
