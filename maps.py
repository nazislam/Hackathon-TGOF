import terrain
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
        self.picture = []
        for i in range(64):
            self.coordinate.append([])
            self.picture.append([])
            for j in range(96):
                self.coordinate[i].append(Pair(None, terrain.Terrain()))
                self.picture[i].append(".")

    def print_map(self):
        file = open("maps/map.txt", "w")
        for i in range(64):
            for j in range(96):
                file.write(self.picture[i][j])
            file.write("\n")

    def create_map(self):
        file = open("maps/map.txt", "r")
        row = 0
        for line in file:
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

    def print_terrain(self):
        file = open("terrain.txt", "w")
        for i in range(64):
            for j in range(96):
                terrain = self.coordinate[i][j].get_terrain()
                file.write(terrain.get_type())
            file.write("\n")

if __name__ == '__main__':
    map = Maps()
    map.print_map()
    #map.create_map()
    #map.print_terrain()