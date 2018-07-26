__author__ = 'python'
import math
class Tile():
    def __init__(self, window, x, y, altitude):
        self.window = window
        self.x = x
        self.y = y
        self.altitude = altitude
        self.outline = []
        for angle in range(45, 405, 90):
            x = self.altitude * math.sin(math.radians(angle)) * math.tan(math.radians(30)) * 2
            y = self.altitude * math.cos(math.radians(angle)) * math.tan(math.radians(30)) * 2
            self.outline.append((self.x + x, self.y + y))