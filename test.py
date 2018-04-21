import random
import os
import string


file = open('card_catalog/spellCard.txt', 'r')
line = file.read()
print(line)

def get_word():
    # Get a random line number
    words = open('resources/words.txt','r')
    file = words.read()
    lines = file.count("\n") + 1
    random.seed()
    picked_word = random.randrange(0,lines)
    words.close()

    # Get the word at the random line
    words = open('resources/words.txt','r')
    word = ""
    count = 0
    for line in words:
        if count == picked_word:
            word = line
        count += 1
    words.close()
    return word.strip()

word = get_word()

print(word)