__author__ = 'python'
class PlayerPacket:
    def __init__(self, connection):
        self.moveUp = connection.moveUp
        self.moveDown = connection.moveDown
        self.moveRight = connection.moveRight
        self.moveLeft = connection.moveLeft
        self.shooting = connection.shooting
        self.mouseAngle = connection.mouseAngle