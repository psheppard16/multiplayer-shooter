from Map.continent import Continent
class Map():
    def __init__(self, window):
        self.window = window
        self.tileList = []
        self.continentList = []
        self.CONTINENT_SIZE = 1000
        self.CONTINENT_NUMBER = 3
        self.TILE_ALTITUDE = 20
        self.generateMap()

    def generateMap(self):
        for i in range(self.CONTINENT_NUMBER):
            newContinent = Continent(self.window, self.TILE_ALTITUDE, self.CONTINENT_SIZE)
            self.continentList.append(newContinent)