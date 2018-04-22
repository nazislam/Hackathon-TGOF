import random
import os




file = open('card_catalog/spellCard.txt', 'r')
file_r = file.read()
end_num = file_r.count("\n") + 1
random.seed()
picked_line = random.randrange(0,end_num)
file.close()

file = open('card_catalog/spellCard.txt', 'r')
file_r = file.read()
end_num = file_r.count("\n") + 1
random.seed()
picked_line = random.randrange(1,end_num)
file.close()

file = open('card_catalog/spellCard.txt', 'r')
lineList = ""
count = 0
for line in file:
    if count == picked_line:
        lineList = line.strip().split("|")
        break
    count += 1
file.close()

print(lineList)



