from Screens.screen import Screen
from tkinter import *
class SaveScreen(Screen):
    def __init__(self, window):
        super().__init__(window, "saveScreen")
        self.save1B = Button(self.window.root, text="Save file 1", command=self.save1, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.save1B.pack(in_=self.f, pady=25)

        self.save2B = Button(self.window.root, text="save file 2", command=self.save2, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.save2B.pack(in_=self.f, pady=25)

        self.save3B = Button(self.window.root, text="save file 3", command=self.save3, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.save3B.pack(in_=self.f, pady=25)

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=25)

    def save1(self):
        self.window.saveSelected = True
        self.window.saveNumber = 1
        self.window.loadChar(1)
        self.window.rMenu = "mainMenu"

    def save2(self):
        self.window.saveSelected = True
        self.window.saveNumber = 2
        self.window.loadChar(3)
        self.window.rMenu = "mainMenu"

    def save3(self):
        self.window.saveSelected = True
        self.window.saveNumber = 3
        self.window.loadChar(3)
        self.window.rMenu = "mainMenu"

    def cancel(self):
        self.window.rMenu = "startScreen"