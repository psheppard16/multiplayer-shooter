import threading
from Server.host import Host
class HostEngine:
    def __init__(self, window):
        self.window = window

        self.messages = []
        self.host = Host(self.window)

        self.hostThread = threading.Thread(target=self.host.receiveMessages, daemon=True) #daemon is True so the thread closes with the window
        self.hostThread.start()

    def run(self):
        for user in self.host.userList:
            if user.lastMessageTime + user.timeout < self.host.getTime():
                self.host.userList.remove(user)