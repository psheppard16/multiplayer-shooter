__author__ = 'psheppard16'
class ScaleEngine:
    def __init__(self, window):
        self.window = window
        self.scale = 1.0
        self.requestedScale = 1.0
        self.scaleUp = False
        self.scaleDown = False
        self.smoothScale = True

    def run(self):
        if self.scaleUp:
            self.requestedScale += 2.5 * self.window.frameRate.TICK_SPEED * self.requestedScale
        if self.scaleDown:
            self.requestedScale -= 2.5 * self.window.frameRate.TICK_SPEED * self.requestedScale
        if self.smoothScale:
            self.scale += (self.requestedScale - self.scale) / 6
        else:
            self.scale = self.requestedScale
        lowerLimit = .1
        upperLimit = 100
        if self.requestedScale < lowerLimit:
            self.requestedScale = lowerLimit
        if self.requestedScale > upperLimit:
            self.requestedScale = upperLimit
        if self.scale < lowerLimit:
            self.scale = lowerLimit
        if self.scale > upperLimit:
            self.scale = upperLimit

    def getScale(self):
        return self.scale