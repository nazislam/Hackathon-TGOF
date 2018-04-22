import pygame 

class Game:
  def __init__(self):
    self.title = "Whisper of War"
    self.pause = False
    self.screenW = 1280
    self.screenH = 720
    self.state = "intro"

  def getScreenW(self):
    return self.screenW
  
  def getScreenH(self):
    return self.screenH

  def getState(self):
    return self.state

  def isPause(self):
    return self.pause

  def getScreenResolution(self):
    return (self.getScreenW(),self.getScreenH())

  