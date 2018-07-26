__author__ = 'python'
from tkinter import *
from PIL import ImageTk
class Screen:
    def __init__(self, window, name, backgroundPath="none"):
        self.window = window
        self.window.screenList.append(self)

        self.name = name

        self.f = Frame(self.window.root, bg="blue", width=self.window.width, height =self.window.width)
        self.f.pack_propagate(0)

        if backgroundPath == "none":
            self.hasBackground = False
        else:
            self.hasBackground = True
            self.backgroundImage= ImageTk.PhotoImage(file=backgroundPath)
            self.backgroundLabel = Label(self.window.root, image=self.backgroundImage)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def setUp(self):
        if self.hasBackground:
            self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.f.pack(side=LEFT)

    def hide(self):
        if self.hasBackground:
            self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()