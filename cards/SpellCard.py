#import Position


class SpellCard(Card):
  def __init__(self, name, description, hp, attack, defense, luck, speed, attRange):
    Card.__init__(self, name, description)
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.luck = luck
    self.speed = speed
    self.attRange = attRange
  
  #Getters
  def getHp(self):
    return self.hp
  
  def getAttack(self):
    return self.attack

  def getDefense(self):
    return self.defense

  def getLuck(self):
    return self.luck

  def getSpeed(self):
    return self.speed

  def getAttackRange(self):
    return self.attRange

  #Spell Card Effects
  def applyEffects(self, Character):
    #Chracter will call this function
    #This call other apply functions
    pass

  def applyHP(self, Character):
    pass

  def applyAttack(self, Character):
    pass

  def applyDefense(self, Character):
    pass

  def applyLuck(self, Character):
    pass
    
  def applySpeed(self, Character):
    pass

  def applyAttackRange(self, Character):
    pass









    




