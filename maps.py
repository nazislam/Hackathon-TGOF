import random

import terrain
from position import Position
import card
class Pair:
    def __init__(self, obj, terrain):
        self.obj = obj
        self.terrain = terrain

    def get_terrain(self):
        return self.terrain

    def get_obj(self):
        return self.obj

    def set_terrain(self, terrain):
        self.terrain = terrain

    def set_obj(self, obj):
        self.obj = obj

class Maps:
    def __init__(self):
        self.coordinate = []
        self.maxx = 36
        self.maxy = 96
        self.picture = []
        for i in range(self.maxx):
            self.coordinate.append([])
            #self.picture.append([])
            for j in range(self.maxy):
                self.coordinate[i].append(Pair(None, terrain.Terrain()))
                #self.picture[i].append(".")

    def print_map(self):
        file = open("map2/map.txt", "w")
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

    def set_obj(self, times):
        for i in range(times):
            card = card.Card.generateCard()
            x = random.randint(0, self.maxx - 1)
            y = random.randint(0, self.maxy - 1)
            self.coordinate[x][y].set_obj(card)



if __name__ == '__main__':
    pass
    #map = Maps()
    #map.print_map()
    #map.create_map()
    #map.print_terrain()