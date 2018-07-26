import random
import util2D
import math
from Map.tile import Tile
class Continent():
    def __init__(self, window, tileAltitude, continentSize):
        self.window = window
        self.tileList = []
        self.tileAltitude = tileAltitude
        self.directionList = ["north", "south", "east", "west", "north west", "north east", "south west", "south east"]
        self.continentSize = continentSize
        self.generate()

    def generate(self):
        self.tileList.clear()
        startX = random.randint(0, 1280 / self.tileAltitude) * self.tileAltitude
        startY = random.randint(0, 720 / self.tileAltitude) * self.tileAltitude
        self.tileList.append(Tile(self.window, startX, startY, self.tileAltitude))
        for ii in range(self.continentSize):
            self.nextX = startX
            self.nextY = startY
            nextDirection = random.choice(self.directionList)
            if nextDirection == "north":
                self.nextY += self.tileAltitude * 2
            elif nextDirection == "south":
                self.nextY -= self.tileAltitude * 2
            elif nextDirection == "east":
                self.nextX += self.tileAltitude * 2
            elif nextDirection == "west":
                self.nextX -= self.tileAltitude * 2
            elif nextDirection == "north west":
                self.nextY += self.tileAltitude * 2
                self.nextX -= self.tileAltitude * 2
            elif nextDirection == "north east":
                self.nextY += self.tileAltitude * 2
                self.nextX += self.tileAltitude * 2
            elif nextDirection == "south west":
                self.nextY -= self.tileAltitude * 2
                self.nextX -= self.tileAltitude * 2
            elif nextDirection == "south east":
                self.nextY -= self.tileAltitude * 2
                self.nextX += self.tileAltitude * 2
            canGenerate = True
            for tile in self.tileList:
                if tile.x == self.nextX and tile.y == self.nextY:
                    canGenerate = False
            if canGenerate:
                self.tileList.append(Tile(self.window, self.nextX, self.nextY, self.tileAltitude))
            else:
                ii -= 1
            spawnTile = random.choice(self.tileList)
            startX = spawnTile.x
            startY = spawnTile.y
