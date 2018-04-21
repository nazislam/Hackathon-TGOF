#import Position


class SpellCard(Card):
  def __init__(self, name, description, hp, attack, defend, luck, speed, attRange):
    Card.__init__(self, name, description)
    self.hp = hp
    self.attack = attack
    self.defend = defend
    self.luck = luck
    self.speed = speed
    self.attRange = attRange

  def applyEffects(self, Character):
    #This call other apply functions
    pass

  def applyHP(self, Character):
    pass

  def applyAttack(self, Character):
    pass

  def applyDefend(self, Character):
    pass

  def applyLuck(self, Character):
    pass
    
  def applySpeed(self, Character):
    pass

  def applyAttackRange(self, Character):
    pass









    




