__author__ = 'psheppard16'
from Screens.screen import Screen
from tkinter import *

class MainMenu(Screen):
    def __init__(self, window):
        super().__init__(window, "mainMenu")
        self.searchB = Button(self.window.root, text="Search for host", command=self.search, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.searchB.pack(in_=self.f, pady=15)

        self.lobbyB = Button(self.window.root, text="Create lobby", command=self.lobby, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.lobbyB.pack(in_=self.f, pady=15)

        self.instructionsB = Button(self.window.root, text="Instructions", command=self.instructions, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.instructionsB.pack(in_=self.f, pady=15)

        self.optionsB = Button(self.window.root, text="Options", command=self.options, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.optionsB.pack(in_=self.f, pady=15)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def quit(self):
        self.window.root.destroy()

    def options(self):
        self.window.rMenu = "options"

    def search(self):
        self.window.rMenu = "searchScreen"

    def lobby(self):
        self.window.rMenu = "lobbyEngine"

    def instructions(self):
        self.window.rMenu = "instructions"