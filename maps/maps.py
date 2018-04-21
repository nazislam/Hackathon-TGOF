import terrain
class Pair:
    def __init__(self, obj, terrain):
        self.obj = obj
        self.terrain = terrain

class Maps:
    def __init__(self):
        self.coordinate = []
        self.picture = []
        for i in range(64):
            self.coordinate.append([])
            self.picture.append([])
            for j in range(96):
                self.coordinate[i].append(Pair(None, terrain.Terrain))
                self.picture[i].append(".")

    def print_map(self):
        for i in range(64):
            for j in range(96):
                print(self.picture[i][j], end = "")
            print()

if __name__ == '__main__':
    map = Maps()
    file = open("map.txt", "w")
    file.write(map.print_map())