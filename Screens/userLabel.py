__author__ = 'python'
from tkinter import *
class UserLabel(PanedWindow):
    def __init__(self, window, user, userBar, userList, *args, **kwargs):
        super(UserLabel, self).__init__(*args, **kwargs)
        self.bind("<Enter>", self.mouseEnter)
        self.bind("<Leave>", self.mouseLeave)
        self.userBar = userBar
        self.userList = userList
        self.user = user
        self.window = window
        self.isReady = True
        self.userList.append(self)
        self.name = Label(self, text=user.name, bg="red")
        self.add(self.name, width=150)

        self.kick = Button(self.window.root, text="Kick", command=self.kick, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.add(self.kick, width=100)

        self.config(orient=HORIZONTAL)
        self.pack(in_=self.userBar, fill=BOTH)

    def update(self):
        if self.isReady:
            self.name.config(bg="green")
        else:
            self.name.config(bg="red")

    def mouseEnter(self, event):
        pass

    def mouseLeave(self, event):
        pass

    def kick(self):
        self.pack_forget()
        self.window.hostEngine.host.userList.remove(self.user)
        self.userList.remove(self)