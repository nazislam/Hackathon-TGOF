class Weapon:
  def __init__(self, name, description, attRange, attack, speed, defense):
    self.attRange = attRange
    self.attack = attack
    self.speed = speed
    self.defense = defense
  
  def getAttackRange(self):
      return self.attRange
      
  def getAttack(self):
      return self.attack

  def getSpeed(self):
      return self.speed  

  def getDefense(self):
      return self.defense

  def applyAttackRange(self, character):
      pass
      character.setAttackRange(getAttackRange() + self.getAttackRange)
      character.increaseAttackRange(self.getAttackRange())

  def applyAttack(self, character):
      pass
      character.setAttack(getAttack() + self.getAttack)
      character.increaseAttack(self.getAttack())

  def applySpeed(self, character):
      pass
      character.setSpeed(getSpeed() + self.getSpeed)
      character.increaseSpeed(self.getSpeed())

  def applyDefense(self, character):
      pass
      character.setDefense(getDefense() + self.getDefense)
      character.increaseDefense(self.getDefense())


class Armor:
  def __init__(self, name, description, defense):
    self.defense = defense
 

  def getDefense(self):
      return self.defense


  def applyDefense(self, character):
      pass
      character.setDefense(getDefense() + self.getDefense)
      character.increaseDefense(self.getDefense())


class Boot:
  def __init__(self, name, description, speed):
    self.speed = speed
 

  def getSpeed(self):
      return self.speed


  def applySpeed(self, character):
      pass
      character.setSpeed(getSpeed() + self.getSpeed)
      character.increaseSpeed(self.getSpeed())

