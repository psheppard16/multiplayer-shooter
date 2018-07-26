from Screens.screen import Screen
from tkinter import *
class Options(Screen):
    def __init__(self, window):
        super().__init__(window, "options")
        self.resolutionF = StringVar()
        self.resolutionF.set("Resolution: " + self.window.save.resolution)
        self.resolutionB = Button(self.window.root, textvariable=self.resolutionF, command=self.resolution, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.resolutionB.pack(in_=self.f, pady=15)

        self.frameF = StringVar()
        if self.window.save.smoothFrames == True:
            self.frameF.set("Smooth framerate transitions on")
        else:
            self.frameF.set("Smooth framerate transitions off")
        self.frameB = Button(self.window.root, textvariable=self.frameF, command=self.frame, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.frameB.pack(in_=self.f, pady=15)

        self.accept = Button(self.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.f, pady=15)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def quit(self):
        self.window.root.destroy()

    def setUp(self):
        if self.window.save.smoothFrames == True:
            self.frameF.set("Smooth framerate transitions on")
        else:
            self.frameF.set("Smooth framerate transitions off")

        self.resolutionF.set("Resolution: " + self.window.save.resolution)

        self.f.pack(side=LEFT)

    def accept(self):
        self.window.rMenu = "mainMenu"

    def resolution(self):
        if self.window.save.resolution == "1280x720":
            self.window.save.resolution = "1366x768"
            self.resolutionF.set("Resolution: " + "1366x768")
        elif self.window.save.resolution == "1366x768":
            self.window.save.resolution = "1600x900"
            self.resolutionF.set("Resolution: " + "1600x900")
        elif self.window.save.resolution == "1600x900":
            self.window.save.resolution = "1920x1080"
            self.resolutionF.set("Resolution: " + "1920x1080")
        elif self.window.save.resolution == "1920x1080":
            self.window.save.resolution = "2048x1152"
            self.resolutionF.set("Resolution: " + "2048x1152")
        elif self.window.save.resolution == "2048x1152":
            self.window.save.resolution = "2560x1440"
            self.resolutionF.set("Resolution: " + "2560x1440")
        elif self.window.save.resolution == "2560x1440":
            self.window.save.resolution = "1280x720"
            self.resolutionF.set("Resolution: " + "1280x720")

    def frame(self):
        if self.window.save.smoothFrames:
            self.window.save.smoothFrames = False
            self.frameF.set("Smooth framerate transitions off")
        else:
            self.window.save.smoothFrames = True
            self.frameF.set("Smooth framerate transitions on")