__author__ = 'psheppard16'
from Screens.screen import Screen
from tkinter import *
class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, "startScreen")
        self.startB = Button(self.window.root, text="Start", command=self.start, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.startB.pack(in_=self.f, pady=15)

        self.instructionsB = Button(self.window.root, text="Instructions", command=self.instructions, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.instructionsB.pack(in_=self.f, pady=15)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def quit(self):
        self.window.root.destroy()

    def start(self):
        self.window.rMenu = "saveScreen"

    def instructions(self):
        self.window.rMenu = "instructions"
