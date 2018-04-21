#import Position


class SpellCard(Card):
  def __init__(self, name, description, step, hp, attack, defend, luck, attRange):
    Card.__init__(self, name, description)
    self.step = step
    self.hp = hp
    self.attack = attack
    self.defend = defend
    self.luck = luck
    self.attRange = attRange

  def applyHP(self, Character):



    




