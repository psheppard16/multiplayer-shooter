from GameObjects.mobile import Mobile
class CircleDisplay(Mobile):
    def __init__(self, window, x, y, radius, color):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.radius = radius
        self.color = color