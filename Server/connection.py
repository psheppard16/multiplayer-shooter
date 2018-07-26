__author__ = 'python'
import socket
import pickle
from Server.playerPacket import PlayerPacket
from GameObjects.playerDisplay import PlayerDisplay
from GameObjects.circleDisplay import CircleDisplay
import math
import threading
class Connection:
    def __init__(self, window, name, hostIP, port):
        """
        Creates an object to send/receive messages to/from a host.
        :param name: the name for the user to identify as
        :param tempHost: the hostname to connect to
        :param tempPort: the port number to connect to
        :return: none
        """
        self.shooting = False
        self.moveLeft = False
        self.moveRight = False
        self.moveDown = False
        self.moveUp = False
        self.mouseAngle = 0
        self.playerList = []

        self.window = window
        self.name = name
        socket.setdefaulttimeout(5)
        self.hostIP = hostIP
        self.IP = socket.gethostbyname(socket.gethostname())
        self.port = int(port) #needs to be the same as that of the host, otherwise connection denied
        self.waiting = False

        self.sendingTries = 1000
        self.senderBound = True
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
        while not self.senderBound and self.sendingTries > 0:
            try:
                self.sender.bind(('', self.port))
                self.sender.close()
                self.senderBound = True
            except ImportError:
                print("retrying sending, tries: " + str(1000 - self.sendingTries))
                self.sendingTries -= 1
                self.window.closePorts()

        self.acceptingTries = 1000
        self.acceptorBound = False
        self.acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while not self.acceptorBound and self.acceptingTries > 0:
            try:
                self.acceptor.bind((self.IP, self.port))
                self.acceptorBound = True
            except ImportError:
                print("retrying accept, tries: " + str(1000 - self.acceptingTries))
                self.acceptingTries -= 1
                self.window.closePorts()

        self.connectionThread = threading.Thread(target=self.receiveMessages, daemon=True)
        self.connectionThread.start()


    def sendMessage(self):
        mouseX = (self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()) / self.window.drawingEngine.scale
        mouseY = (self.window.height - self.window.root.winfo_pointery() + self.window.root.winfo_rooty()) / self.window.drawingEngine.scale
        xComponent = mouseX - self.window.width / 2 / self.window.drawingEngine.scale
        yComponent = mouseY - self.window.height / 2 / self.window.drawingEngine.scale
        self.mouseAngle = math.atan2(yComponent, xComponent)
        if self.senderBound:
            try:
                self.sender = socket.create_connection((self.hostIP, self.port)) #re-connects to the host
                packet = PlayerPacket(self)
                info = [self.IP, self.port, self.name, packet]
                data = pickle.dumps(info) #serializes the message
                self.sender.send(data) #sends the message
                self.sender.close()
            except ConnectionRefusedError:
                print("connection refused")

    def receiveMessages(self):
        if self.acceptorBound:
            self.acceptor.listen(5)
            fails = 0
            while True and fails < 1000:
                try:
                    c, addr = self.acceptor.accept()
                    received = c.recv(4096)
                    c.close()
                    try:
                        message = pickle.loads(received)
                        hostPacket = message[3]
                        self.window.drawingEngine.playerDisplayList.clear()
                        for player in hostPacket.playerList:
                            x = player[0]
                            y = player[1]
                            radius = player[2]
                            health = player[3]
                            bulletList = player[4]
                            IP = player[5]
                            playerDisplay = PlayerDisplay(self.window, x, y, radius, health, bulletList, self.name, IP)
                            if playerDisplay.IP != self.IP:
                                self.window.drawingEngine.playerDisplayList.append(playerDisplay)
                            else:
                                self.window.drawingEngine.player = playerDisplay

                        self.window.drawingEngine.circleDisplayList.clear()
                        for circle in hostPacket.circleList:
                            self.window.drawingEngine.circleDisplayList.append(CircleDisplay(self.window, circle[0], circle[1], circle[2], circle[3]))

                        self.window.drawingEngine.arenaSize = hostPacket.arenaSize
                    except EOFError:
                        fails += 1
                        print("Too much data to process")
                    fails = 0
                except OSError:
                    fails += 1
                    print("Error in receiving data, failures: " + str(fails))
                self.waiting = False

    def kp(self, event):
        if event.keysym == "space":
            self.shooting = True
        elif event.keysym == "w":
            self.moveUp = True
        elif event.keysym == "s":
            self.moveDown = True
        elif event.keysym == "a":
            self.moveLeft = True
        elif event.keysym == "d":
            self.moveRight = True

    def kr(self, event):
        if event.keysym == "space":
            self.shooting = False
        elif event.keysym == "w":
            self.moveUp = False
        elif event.keysym == "s":
            self.moveDown = False
        elif event.keysym == "a":
            self.moveLeft = False
        elif event.keysym == "d":
            self.moveRight = False