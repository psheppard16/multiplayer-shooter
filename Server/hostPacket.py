__author__ = 'python'
class HostPacket:
    def __init__(self, player, enemyList, circleList, arenaSize):
        self.healthChange = 0
        self.playerList = []
        for enemy in enemyList:
            x = enemy.x
            y = enemy.y
            radius = enemy.radius
            health = enemy.health
            IP = enemy.IP
            bulletList = []
            for bullet in enemy.bulletList:
                bulletList.append((bullet.x, bullet.y, bullet.radius, IP))
            self.playerList.append((x, y, radius, health, bulletList, IP))

        x = player.x
        y = player.y
        radius = player.radius
        health = player.health
        IP = player.IP
        bulletList = []
        for bullet in player.bulletList:
            bulletList.append((bullet.x, bullet.y, bullet.radius, IP))
        self.playerList.append((x, y, radius, health, bulletList, IP))


        self.circleList = []
        for circle in circleList:
            x = circle.x
            y = circle.y
            radius = circle.radius
            color = circle.color
            self.circleList.append((x, y, radius, color))

        self.arenaSize = arenaSize
