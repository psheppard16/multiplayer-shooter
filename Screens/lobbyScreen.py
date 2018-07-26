__author__ = 'psheppard16'
from Screens.screen import Screen
from tkinter import *
class LobbyScreen(Screen):
    def __init__(self, window):
        super().__init__(window, "lobby")
        self.accept = Button(self.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.f, pady=15)

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=25)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def accept(self):
        self.window.rMenu = "gameEngine"

    def quit(self):
        self.window.root.destroy()

    def cancel(self):
        self.window.rMenu = "mainMenu"