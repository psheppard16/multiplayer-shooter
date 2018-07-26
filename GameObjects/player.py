__author__ = 'psheppard16'
import math
from GameObjects.mobile import Mobile
from GameObjects.bullet import Bullet
class Player(Mobile):
    def __init__(self, window, x, y, name, IP):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.IP = IP
        self.radius = 25
        self.name = name
        self.speed = 500
        self.rateOfFire = .05
        self.bulletCD = self.rateOfFire
        self.maxHealth = 100
        self.health = 100
        self.bulletList = []
        self.moveUp = False
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = False
        self.shooting = False
        self.mouseAngle = 0

    def run(self):
        self.move()

        if self.moveUp:
            self.changePosition(0, self.speed)
        if self.moveDown:
            self.changePosition(0, -self.speed)
        if self.moveRight:
            self.changePosition(self.speed, 0)
        if self.moveLeft:
            self.changePosition(-self.speed, 0)

        self.shoot()

        self.collide()

    def setKeyCommands(self, moveUp, moveDown, moveLeft, moveRight, shooting, mouseAngle, IP):
        if IP == self.IP:
            self.moveUp = moveUp
            self.moveDown = moveDown
            self.moveRight = moveRight
            self.moveLeft = moveLeft
            self.shooting = shooting
            self.mouseAngle = mouseAngle

    def shoot(self):
        self.bulletCD -= self.window.frameRate.TICK_SPEED
        if self.shooting and self.bulletCD < 0:
            self.bulletCD = self.rateOfFire
            bulletSpeed = 2000
            xVel = bulletSpeed * math.cos(self.mouseAngle)
            yVel = bulletSpeed * math.sin(self.mouseAngle)
            self.bulletList.append(Bullet(self.window, self.x, self.y, xVel, yVel, 5, 5, 2, self.IP))

    def collide(self):
        for circle in self.window.serverEngine.circleList:
            if circle.isTouching(self.x, self.y, self.radius):
                xComponent = self.x - circle.x
                yComponent = self.y - circle.y
                angle = math.atan2(yComponent, xComponent)
                hypotenuse = self.distanceToSelf(circle.x, circle.y)
                distanceToMove = self.radius + circle.radius - hypotenuse
                distanceX = distanceToMove * math.cos(angle)
                distanceY = distanceToMove * math.sin(angle)
                self.x += distanceX
                self.y += distanceY

        if self.y + self.radius / 2 > self.window.serverEngine.arenaSize:
            self.shiftPosition(0, self.window.serverEngine.arenaSize - self.y - self.radius / 2)
        if self.y - self.radius / 2 < -self.window.serverEngine.arenaSize:
            self.shiftPosition(0, -self.window.serverEngine.arenaSize - self.y + self.radius / 2)
        if self.x + self.radius / 2 > self.window.serverEngine.arenaSize:
            self.shiftPosition(self.window.serverEngine.arenaSize - self.x - self.radius / 2, 0)
        if self.x - self.radius / 2 < -self.window.serverEngine.arenaSize:
            self.shiftPosition(-self.window.serverEngine.arenaSize - self.x + self.radius / 2, 0)

    def isTouching(self, x, y, radius):
        if self.distanceToSelf(x, y) < self.radius * .9 + radius:
            return True
        else:
            return False

    def distance(self, x1, y1, x2, y2):
        xD = x1 - x2
        yD = y1 - y2
        return math.sqrt(xD ** 2 + yD ** 2)

