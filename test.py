import random
import os
import card

file = open("map3/map.txt", "r")
char = file.read(1)

for i in range(14):
    for k in range(27):
        if char == "\n":
            char = file.read(1)
            continue
        print(char, end= "|")
        char = file.read(1)

    print()