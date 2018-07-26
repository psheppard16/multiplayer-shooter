__author__ = 'psheppard16'
import math
from GameObjects.mobile import Mobile
class Bullet(Mobile):
    def __init__(self, window, x, y, xVel, yVel, radius, damage, despawnTime, IP):
        super().__init__(window, x, y, xVel, yVel)
        self.IP = IP
        self.window = window
        self.radius = radius
        self.damage = damage
        self.despawnTime = despawnTime
        self.alive = True

    def run(self):
        self.despawnTime -= self.window.frameRate.TICK_SPEED
        self.move()
        self.aliveCheck()

    def aliveCheck(self):
        for circle in self.window.serverEngine.circleList:
            if circle.isTouching(self.x, self.y, self.radius):
                self.alive = False
        for player in self.window.serverEngine.playerList:
            if player.isTouching(self.x, self.y, self.radius) and self.IP != player.IP and self.alive:
                player.health -= self.damage
                self.alive = False
        player = self.window.serverEngine.player
        if player.isTouching(self.x, self.y, self.radius) and self.IP != player.IP and self.alive:
            player.health -= self.damage
            self.alive = False
        if self.despawnTime < 0:
            self.alive = False
        if self.y + self.radius / 2 > self.window.serverEngine.arenaSize:
            self.alive = False
        if self.y - self.radius / 2 < -self.window.serverEngine.arenaSize:
            self.alive = False
        if self.x + self.radius / 2 > self.window.serverEngine.arenaSize:
            self.alive = False
        if self.x - self.radius / 2 < -self.window.serverEngine.arenaSize:
            self.alive = False

    def distance(self, x1, y1, x2, y2):
        xD = x1 - x2
        yD = y1 - y2
        return math.sqrt(xD ** 2 + yD ** 2)