from GameObjects.mobile import Mobile
class BulletDisplay(Mobile):
    def __init__(self, window, x, y, radius, IP):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.radius = radius
        self.IP = IP
        self.bulletList = []