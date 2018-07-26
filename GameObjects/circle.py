__author__ = 'psheppard16'
import random
import math
from GameObjects.mobile import Mobile
class Circle(Mobile):
    def __init__(self, window, x, y, radius, color=None):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.radius = radius
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (0, 255, 255), (128, 0, 255), (255, 0, 255)]
        if color == None:
            self.color = random.choice(self.colors)
        else:
            self.color = color
        self.alive = True

    def isTouching(self, x, y, radius):
        if self.distanceToSelf(x, y) < self.radius + radius:
            return True
        else:
            return False