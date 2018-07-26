__author__ = 'psheppard16'
from Screens.screen import Screen
from tkinter import *
class SearchScreen(Screen):
    def __init__(self, window):
        super().__init__(window, "searchScreen")

        self.nameVar = StringVar()
        self.entryName = Entry(self.window.root, textvariable=self.nameVar, bg="#%02x%02x%02x" % (255, 165, 0), fg="#%02x%02x%02x" % (255, 255, 255), font="Helvetica 15 bold", width=12, justify=CENTER)
        self.entryName.pack(in_=self.f, pady=15)

        self.IPVar = StringVar()
        self.entryIP = Entry(self.window.root, textvariable=self.IPVar, bg="#%02x%02x%02x" % (255, 165, 0), fg="#%02x%02x%02x" % (255, 255, 255), font="Helvetica 15 bold", width=12, justify=CENTER)
        self.entryIP.pack(in_=self.f, pady=15)

        self.search = Button(self.window.root, text="Accept", command=self.search, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.search.pack(in_=self.f, pady=15)

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=25)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def search(self):
        self.window.rMenu = "searchEngine"

    def quit(self):
        self.window.root.destroy()

    def cancel(self):
        self.window.rMenu = "mainMenu"