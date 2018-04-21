class Terrain:
    def __init__(self):
        self.stepable = True
        self.speed_rate = 1
        self.type = "Error"

    def get_type(self):
        return self.type

    def __str__(self):
        return self.type

class Grass(Terrain):
    def __init__(self):
        Terrain.__init__(self)
        self.type = "Grass"

    def get_type(self):
        return self.type

class Swamp(Terrain):
    def __init__(self):
        Terrain.__init__(self)
        self.type = "Swamp"
        self.speed_rate = 0.5


class Mountain(Terrain):
    def __init__(self):
        Terrain.__init__(self)
        self.type = "Mount"
        self.stepable = False


class River(Terrain):
    def __init__(self):
        Terrain.__init__(self)
        self.type = "River"
        self.stepable = True


if __name__ == '__main__':
    terrain = Grass()
    print(terrain.get_type())
