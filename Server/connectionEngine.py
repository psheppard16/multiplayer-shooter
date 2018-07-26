import threading
from Server.connection import Connection
class ConnectionEngine:
    def __init__(self, window):
        self.window = window

        self.connection = Connection(self.window, self.window.searchScreen.nameVar.get(), self.window.searchScreen.IPVar.get(), 10004)

    def run(self):
        if not self.connection.waiting:
            self.connection.sendMessage()
            self.connection.waiting = True