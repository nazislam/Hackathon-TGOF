class Weapon:
  def __init__(self, weaponType, weaponLevel, attRange, attack, speed, defense):
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


class Armor:
  def __init__(self, armorType, armorLevel, defense):
    self.defense = defense
 

  def getDefense(self):
      return self.defense



class Boot:
  def __init__(self, bootName, bootLevel, speed):
    self.speed = speed
 

  def getSpeed(self):
      return self.speed


