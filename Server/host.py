__author__ = 'Norman Delorey'
__version__ = '0.2'
"""
    This contains two classes (User and Host) to send and receive text messages.
"""
import socket
import pickle
from GameObjects.player import Player
from Server.hostPacket import HostPacket
import time
from Server.user import User
class Host:
    def __init__(self, window):
        self.window = window

        self.IP = socket.gethostbyname(socket.gethostname())
        self.port = 10004
        self.hostName = socket.gethostname()
        self.userList = [] #the de-serialized messages
        self.name = "server"

        self.sendingTries = 1000
        self.senderBound = False
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
        while not self.senderBound and self.sendingTries > 0:
            try:
                self.sender.bind(('', self.port))
                self.sender.close()
                self.senderBound = True
            except OSError:
                print("retrying")
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

    def sendMessage(self):
        if self.senderBound:
            if self.window.serverEngine != None:
                for user in self.userList:
                    try:
                        self.sender = socket.create_connection((user.IP, self.port)) #connects to the user
                        hostPacket = HostPacket(self.window.serverEngine.player, self.window.serverEngine.playerList, self.window.serverEngine.circleList, self.window.serverEngine.arenaSize)
                        info = [self.IP, self.port, self.name, hostPacket]
                        data = pickle.dumps(info) #serializes the message
                        self.sender.send(data)
                        self.sender.close()
                    except ConnectionRefusedError:
                        print("connection refused")
            else:
                for user in self.userList:
                    try:
                        self.sender = socket.create_connection((user.IP, self.port)) #connects to the user
                        hostPacket = HostPacket(Player(self.window, 0, 0, "host", self.IP), [], [], 1000)
                        info = [self.IP, self.port, self.name, hostPacket]
                        data = pickle.dumps(info) #serializes the message
                        self.sender.send(data)
                        self.sender.close()
                    except ConnectionRefusedError:
                        print("connection refused")

    def receiveMessages(self):
        """
        Accepts messages from clients
        :return: none
        """
        if self.acceptorBound:
            self.acceptor.listen(5)                 # Now wait for client connection.

            while True:
                c, addr = self.acceptor.accept()     # Establish connection with client.
                receivedData = c.recv(4096) #receives data
                message = pickle.loads(receivedData) #de-serializes the message

                newUser = True
                for user in self.userList:
                    if addr[0] == user.IP:
                        newUser = False
                        user.lastMessageTime = self.getTime()
                if newUser and self.window.cMenu == "lobbyEngine":
                    self.userList.append(User(self.window, addr[0], message[2])) #adds any new users to the user list

                playerPacket = message[3]
                moveUp = playerPacket.moveUp
                moveDown = playerPacket.moveDown
                moveLeft = playerPacket.moveLeft
                moveRight = playerPacket.moveRight
                shooting = playerPacket.shooting
                mouseAngle = playerPacket.mouseAngle
                IP = message[0]
                if self.window.serverEngine != None:
                    for player in self.window.serverEngine.playerList:
                        player.setKeyCommands(moveUp, moveDown, moveLeft, moveRight, shooting, mouseAngle, IP)

                c.close()                # Close the connection

                self.sendMessage()

    def getTime(self):
        self.time = time.clock()
        return self.time




