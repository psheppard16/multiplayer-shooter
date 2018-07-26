from GameObjects.circle import Circle
from GameObjects.player import Player
from GameObjects.circleDisplay import CircleDisplay
from GameObjects.playerDisplay import PlayerDisplay
import random
import math
class ServerEngine:
    def __init__(self, window):
        self.window = window
        self.player = Player(self.window, 1280 / 2, 720 / 2, self.window.hostEngine.host.name, self.window.hostEngine.host.IP)
        self.playerList = []
        self.circleList = []
        self.arenaSize = 1000
        for user in self.window.hostEngine.host.userList:
            notValid = True
            x = 0
            y = 0
            while notValid:
                notValid = False
                x = random.randint(-self.arenaSize * .9, self.arenaSize * .9)
                y = random.randint(-self.arenaSize * .9, self.arenaSize * .9)
                for player in self.playerList:
                    if self.distance(x, y, player.x, player.y) < 500:
                        notValid = True
            self.playerList.append(Player(self.window, x, y, user.name, user.IP))
        self.spawnCircles()

    def runGame(self):
        mouseX = (self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()) / self.window.drawingEngine.scale
        mouseY = (self.window.height - self.window.root.winfo_pointery() + self.window.root.winfo_rooty()) / self.window.drawingEngine.scale
        xComponent = mouseX - self.window.width / 2 / self.window.drawingEngine.scale
        yComponent = mouseY - self.window.height / 2 / self.window.drawingEngine.scale
        self.player.mouseAngle = math.atan2(yComponent, xComponent)

        self.runPlayers()
        self.runBullets()

        self.window.drawingEngine.playerDisplayList.clear()
        for player in self.playerList:
            x = player.x
            y = player.y
            radius = player.radius
            health = player.health
            IP = player.IP
            name = player.name
            bulletList = []
            for bullet in player.bulletList:
                bulletList.append((bullet.x, bullet.y, bullet.radius, IP))
            playerDisplay = PlayerDisplay(self.window, x, y, radius, health, bulletList, name, IP)
            self.window.drawingEngine.playerDisplayList.append(playerDisplay)
        x = self.player.x
        y = self.player.y
        radius = self.player.radius
        health = self.player.health
        name = self.player.name
        IP = self.player.IP
        bulletList = []
        for bullet in self.player.bulletList:
            bulletList.append((bullet.x, bullet.y, bullet.radius, IP))
        self.window.drawingEngine.player = PlayerDisplay(self.window, x, y, radius, health, bulletList, name, IP)

        self.window.drawingEngine.circleDisplayList.clear()
        for circle in self.circleList:
            self.window.drawingEngine.circleDisplayList.append(CircleDisplay(self.window, circle.x, circle.y, circle.radius, circle.color))

        self.window.drawingEngine.arenaSize = self.arenaSize

    def runPlayers(self):
        for player in self.playerList:
            if player.health >= 0:
                player.run()
            else:
                for user in self.window.hostEngine.host.userList:
                    if user.IP == player.IP:
                        self.playerList.remove(player)
                        self.window.hostEngine.host.userList.remove(user)
        if self.player.health >= 0:
            self.player.run()
        else:
            self.player.x = 100000
            self.player.y = 100000

    def runBullets(self):
        for player in self.playerList:
            for bullet in player.bulletList:
                bullet.run()
                if not bullet.alive:
                    player.bulletList.remove(bullet)
                    del bullet
        for bullet in self.player.bulletList:
            bullet.run()
            if not bullet.alive:
                self.player.bulletList.remove(bullet)
                del bullet

    def spawnCircles(self):
        numberOfBlobs = int(self.arenaSize ** 2 / 50000)
        lowestRadius = int(self.arenaSize / 100)
        maxRadius = lowestRadius * 5
        for i in range(numberOfBlobs):
            x = random.randint(-self.arenaSize + maxRadius * 2, self.arenaSize - maxRadius * 2)
            y = random.randint(-self.arenaSize + maxRadius * 2, self.arenaSize - maxRadius * 2)
            radius = random.randint(lowestRadius, maxRadius)
            self.circleList.append(Circle(self.window, x, y, radius))

    def kp(self, event):
        if event.keysym == "space":
            self.player.shooting = True
        elif event.keysym == "w":
            self.player.moveUp = True
        elif event.keysym == "s":
            self.player.moveDown = True
        elif event.keysym == "a":
            self.player.moveLeft = True
        elif event.keysym == "d":
            self.player.moveRight = True

    def kr(self, event):
        if event.keysym == "space":
            self.player.shooting = False
        elif event.keysym == "w":
            self.player.moveUp = False
        elif event.keysym == "s":
            self.player.moveDown = False
        elif event.keysym == "a":
            self.player.moveLeft = False
        elif event.keysym == "d":
            self.player.moveRight = False

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)





