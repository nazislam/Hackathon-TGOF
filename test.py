import random
import os

file = open('card_catalog/spellCard.txt', 'r')
line = file.readline().strip()
lineList = line.split("|")
print(lineList)
