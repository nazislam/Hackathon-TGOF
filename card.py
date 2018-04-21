class Card:
  def __init__(self, name, description):
    self.name = name
    self.type = "Error"
    self.description = description
  
  #Getters
  def getName(self):
    return self.name

  def getDescription(self):
    return self.description

  def getType(self):
    return self.type

class SpellCard(Card):
  def __init__(self, name, description, hp, attack, defense, luck, speed, attRange):
    Card.__init__(self, name, description)
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.luck = luck
    self.speed = speed
    self.attRange = attRange
    self.type = "Spell Card"
  
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

"""  No need
  #Spell Card Effects
  def applyEffects(self, character):
    #Chracter will call this function
    #This call other apply functions
    pass
    self.applyAttack(character)
    self.applyDefense(character)
    self.applyHP(character)
    self.applyLuck(character)
    self.applyAttackRange(character)
    self.applySpeed(character)


  def applyHP(self, character):
    pass
    character.increaseHp(self.getHp())

  def applyAttack(self, character):
    pass
    character.setAttack(character.getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())
    

  def applyDefense(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())

  def applyLuck(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())
    
  def applySpeed(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())

  def applyAttackRange(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())
"""


class MoveCard(Card):
  def __init__(self, name, description, step):
    Card.__init__(self, name, description)
    self.type = "Move Card"
    self.step = step

  #Getters
  def getStep(self):
    return self.step

  def moveCharacter(self, character, Position):
    pass

  def generateCard(self, cardCatalog):
      x = cardCatalog.split('|')
      for j in x:
          self.name = x[0]
          self.step = x[1]
          self.description = x[2]




