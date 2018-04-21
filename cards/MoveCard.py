#import Position


class MoveCard(Card):
  def __init__(self, name, description, step):
    Card.__init__(self, name, description)
    self.step = step

  def getStep(self):
    return self.step

  def moveCharacter(self, Character, Position):








