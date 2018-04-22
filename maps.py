import random

import terrain
from position import Position
import itemBox
import card
maxx = 36
maxy = 96
class Pair:
    def __init__(self, obj, terrain, type = "nothing"):
        self.obj = obj
        self.terrain = terrain
        self.type = type

    def get_terrain(self):
        return self.terrain

    def get_obj(self):
        return self.obj

    def get_type(self):
        return self.type

    def set_terrain(self, terrain):
        self.terrain = terrain

    def set_obj(self, obj, type = "nothing"):
        self.obj = obj
        self.type = type

    def set_type(self, type):
        self.type = type

class Maps:
    def __init__(self):
        self.coordinate = []
        self.maxx = maxx
        self.maxy = maxy
        self.picture = []
        for i in range(self.maxx):
            self.coordinate.append([])
            #self.picture.append([])
            for j in range(self.maxy):
                self.coordinate[i].append(Pair(None, terrain.Terrain()))
                #self.picture[i].append(".")

    def print_map(self):
        file = open("map2/map1.txt", "w")
        for i in range(self.maxx):
            for j in range(self.maxy):
                file.write(self.picture[i][j])
            file.write("\n")

    def create_map(self):
        file = open("map2/map.txt", "r")
        row = 0
        for line in file:
            self.picture.append(line)
            for i in range(len(line)):
                if line[i] == '.':
                    self.coordinate[row][i].set_terrain(terrain.Grass())
                if line[i] == '^':
                    self.coordinate[row][i].set_terrain(terrain.Mountain())
                if line[i] == '*':
                    self.coordinate[row][i].set_terrain(terrain.River())
                if line[i] == '-':
                    self.coordinate[row][i].set_terrain(terrain.Swamp())
            row += 1

    def delete(self, x, y):
        self.coordinate[x][y].set_obj(None)
        self.coordinate[x][y].set_type("nothing")
        sign = "."
        if self.coordinate[x][y].terrain.get_type() == "Grass":
            sign = "."
        if self.coordinate[x][y].terrain.get_type() == "Mount":
            sign = "^"
        if self.coordinate[x][y].terrain.get_type() == "River":
            sign = "*"
        if self.coordinate[x][y].terrain.get_type() == "Swamp":
            sign = "-"
        self.picture[x] = self.picture[x][:y - 1] + sign + self.picture[x][y:]

    def get_terrain(self):
        return self.coordinate

    def get_map(self):
        return self.picture

    def print_terrain(self):
        file = open("map2/terrain.txt", "w")
        for i in range(self.maxx):
            for j in range(self.maxy):
                terrain = self.coordinate[i][j].get_terrain()
                file.write(terrain.get_type())
            file.write("\n")

    def set_random_card(self, times):
        for i in range(times):
            my_card = card.generateCard()
            x = random.randint(0, self.maxx - 1)
            y = random.randint(0, self.maxy - 1)
            self.coordinate[x][y].set_obj(my_card, "Card")
            self.coordinate[x][y].terrain.stepable = False
            self.picture[x] = self.picture[x][:y - 1] + "C" + self.picture[x][y:]

    def set_random_box(self, times):
        for i in range(times):
            my_box = itemBox.generateBox()
            x = random.randint(0, self.maxx - 1)
            y = random.randint(0, self.maxy - 1)
            self.coordinate[x][y].set_obj(my_box, "Box")
            self.coordinate[x][y].terrain.stepable = False
            self.picture[x] = self.picture[x][:y - 1] + "B" + self.picture[x][y:]


if __name__ == '__main__':
    pass
    #map = Maps()
    #map.print_map()
    #map.create_map()
    #map.print_terrain()