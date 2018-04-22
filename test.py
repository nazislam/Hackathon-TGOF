import random
import os
import card

"""file = open('card_catalog/attackCard.txt', 'r')
file_r = file.read()
end_num = file_r.count("\n") + 1
random.seed()
picked_line = random.randrange(1,end_num)
file.close()

file = open('card_catalog/attackCard.txt', 'r')
stats = ""
count = 0
for line in file:
    if count == picked_line:
        stats = line.strip().split("|")
        break
    count += 1
file.close()

print(stats)"""

testCard = card.generateSpell()
print(testCard)