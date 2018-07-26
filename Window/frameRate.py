__author__ = 'psheppard16'
import time
class FrameRate:
    def __init__(self, window):
        self.window = window
        self.VARIABLE_FRAMERATE = True
        self.UPDATE_TIME = .25
        self.nextFrameCalc = 0
        self.tickSum = 0
        self.tickStartTime = 0
        self.renderTime = 1 / 20
        self.renderedFrame = True
        self.requestedFrameRate = 1 / 30
        self.nextTick = 0
        self.TICK_SPEED = 1 / 30
        self.loadTime = 1
        self.time = 0
        self.startTime = 0
        self.longestTaskTime = 0
        self.longestTask = "null"
        self.sum = 0
        self.number = 0
        self.allTasks = []

    def update(self):
        self.nextTick += self.TICK_SPEED
        if self.window.save.smoothFrames:
            if self.VARIABLE_FRAMERATE:
                tickTime = self.getTime() - self.tickStartTime #time it takes for the program to run one tick
                if not self.renderedFrame:
                    tickTime += self.renderTime
                self.tickSum += tickTime
                if self.getTime() > self.nextFrameCalc:
                    self.nextFrameCalc += self.UPDATE_TIME
                    if self.getTime() > self.nextTick:
                        catchUpTime = (self.getTime() - self.nextTick) ** .5 / 30
                    else:
                        catchUpTime = -(self.nextTick - self.getTime()) ** .5 / 30
                    self.TICK_SPEED = self.tickSum / (self.UPDATE_TIME / self.TICK_SPEED) + catchUpTime
                    self.tickSum = 0
            if self.TICK_SPEED < 1 / 120:
               self.TICK_SPEED = 1 / 120
            if self.TICK_SPEED > 1:
                self.TICK_SPEED = 1
            self.UPDATE_TIME = self.TICK_SPEED ** .3 #this works but i dont know why; simply multiplying by ten doesnt
            if self.TICK_SPEED < 1 / 120:
               self.TICK_SPEED = 1 / 120
        else:
            self.TICK_SPEED = self.getTime() - self.nextTick
        if self.window.cMenu == "serverEngine" and self.TICK_SPEED < .5:
            self.loadTime -= self.TICK_SPEED

    def getTime(self):
        self.time = time.clock()
        return self.time

    def startTimer(self, task):
        self.startTime = self.getTime()
        self.task = task

    def timeChange(self):
        timeChange = self.getTime() - self.startTime

        if timeChange > self.longestTaskTime:
            self.longestTask = self.task
            self.longestTaskTime = timeChange

        if len(self.allTasks) < 1000:
            self.allTasks.append((timeChange, self.task))

    def getLongestTask(self):
        if self.longestTaskTime != 0:
            print("frame rate:", str(1 / self.TICK_SPEED))
            print("Longest task:", self.longestTask, "Percent:", str(self.longestTaskTime / self.TICK_SPEED * 100) + "%" , "Time:", str(self.longestTaskTime))
        self.longestTask = "null"
        self.longestTaskTime = 0

    def getAllTasks(self):
        print(self.allTasks)
        self.allTasks.clear()


