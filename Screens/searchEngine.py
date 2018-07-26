from tkinter import *
from Screens.screen import Screen
from Screens.userLabel import UserLabel
import socket
class SearchEngine(Screen):
    def __init__(self, window):
        super().__init__(window, "searchEngine")
        self.window = window
        self.f = Frame(self.window.root, bg="blue", width=self.window.width, height =self.window.height)
        self.f.pack_propagate(0)

        self.pane = PanedWindow(orient=HORIZONTAL)
        self.pane.pack(in_=self.f, fill=BOTH, expand=2)

        self.userBar = Label(self.window.root, bg="light grey")
        self.titleLabel = Label(self.window.root, text="Lobby:", bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10, width=250)
        self.titleLabel.pack(in_=self.userBar)
        self.pane.add(self.userBar, width=250)

        self.userLabelList = []

        self.options = Label(self.window.root, bg="light blue")
        self.pane.add(self.options)

        self.IPLabel = Label(self.window.root, text="IP: ", bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.IPLabel.pack(in_=self.options, pady=15)

        self.accept = Button(self.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.options, pady=15)

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.options, pady=25)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.options, pady=15)

    def run(self):
        pass
        self.IPLabel.config(text="searching for IP: " + self.window.searchScreen.IPVar.get())

    def accept(self):
        self.window.rMenu = "gameEngine"

    def quit(self):
        self.window.root.destroy()

    def cancel(self):
        self.window.rMenu = "mainMenu"