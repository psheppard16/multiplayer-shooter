from tkinter import *
from Screens.screen import Screen
from Screens.userLabel import UserLabel
import socket
class LobbyEngine(Screen):
    def __init__(self, window):
        super().__init__(window, "lobbyEngine")
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

        self.IPLabel = Label(self.window.root, text="IP: " + socket.gethostbyname(socket.gethostname()), bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.IPLabel.pack(in_=self.options, pady=15)

        self.accept = Button(self.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.options, pady=15)

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.options, pady=25)

        self.quitB = Button(self.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.options, pady=15)

    def run(self):
        if self.window.hosting:
            self.checkForNewUser()
            self.removeUserLabels()
            self.updateLabels()

    def checkForNewUser(self):
        for user in self.window.hostEngine.host.userList:
            if user.new:
                self.userLabelList.append(UserLabel(self.window, user, self.userBar, self.userLabelList, self.window.root))
                user.new = False

    def removeUserLabels(self):
        for userLabel in self.userLabelList:
            userExists = False
            for user in self.window.hostEngine.host.userList:
                if user == userLabel.user:
                    userExists = True
            if not userExists:
                userLabel.pack_forget()
                self.userLabelList.remove(userLabel)

    def updateLabels(self):
        for userLabel in self.userLabelList:
            userLabel.update()

    def accept(self):
        self.window.rMenu = "gameEngine"

    def quit(self):
        self.window.root.destroy()

    def cancel(self):
        self.window.rMenu = "mainMenu"