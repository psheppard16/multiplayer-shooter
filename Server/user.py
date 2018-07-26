__author__ = 'python'
class User:
    def __init__(self, window, IP, name):
        self.window = window
        self.IP = IP
        self.name = name
        self.timeout = .5
        self.lastMessageTime = 0
        self.ready = False
        self.new = True


