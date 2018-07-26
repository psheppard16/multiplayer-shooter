__author__ = 'psheppard16'
from GameObjects.mobile import Mobile
from GameObjects.bulletDisplay import BulletDisplay
class PlayerDisplay(Mobile):
    def __init__(self, window, x, y, radius, health, bulletList, name, IP):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.radius = radius
        self.name = name
        self.IP = IP
        self.maxHealth = 100
        self.health = health
        self.bulletDisplayList = []
        for bullet in bulletList:
            self.bulletDisplayList.append(BulletDisplay(self.window, bullet[0], bullet[1], bullet[2], bullet[3]))