from Screens.screen import Screen
from tkinter import *
class Instructions(Screen):
    def __init__(self, window):
        super().__init__(window, "instructions")
        instructions = """Objective:
Mechanics:
Controls:
"""

        self.descriptionL = Label(window.root, text=instructions, justify=CENTER, bg="#%02x%02x%02x" % (121, 202, 249), compound=CENTER, wraplength=self.window.width // 1.25, font="Helvetica 15 bold")
        self.descriptionL.pack(in_=self.f, side=TOP, pady=10)

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=15)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def quit(self):
        self.window.root.destroy()

    def cancel(self):
        if self.window.saveSelected:
            self.window.rMenu = "mainMenu"
        else:
            self.window.rMenu = "startScreen"
