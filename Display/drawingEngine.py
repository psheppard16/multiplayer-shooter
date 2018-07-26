import math
from PIL import Image, ImageTk
import PIL
try:
    import pygame
except:
    pass
from tkinter import Canvas, NW
import os
import platform
from Screens.screen import Screen
from GameObjects.playerDisplay import PlayerDisplay
class DrawingEngine(Screen):
    def __init__(self, window):
        super().__init__(window, "gameEngine")
        os.environ['SDL_WINDOWID'] = str(self.f.winfo_id())
        if platform.system() == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'
            self.usePygame = True
            self.display = pygame.display.set_mode((self.window.width, self.window.height))
            self.display.fill((255,255,255))
            pygame.display.init()
            pygame.font.init()
        else:
            self.usePygame = False
            self.canvas = Canvas(self.window.root, bg="white", width=self.window.width, height = self.window.height)
            self.canvas.pack(in_=self.f)
        self.tkImageList = [] #images must maintain a reference in order to appear on the canvas

        self.arenaSize = 1000
        self.mapSize = self.window.width * .2
        self.mapScale = .1
        self.mapX = self.window.width - self.mapSize / 2
        self.mapY = self.window.height - self.mapSize / 2
        self.wallWidth = 50
        self.circleDisplayList = []
        self.playerDisplayList = []
        self.player = PlayerDisplay(self.window, 0, 0, 10, 100, [], "name", "00.00.00")

        self.scale = self.window.width / 1280 / 1.5
        self.screenX = self.window.width / 2 / self.scale
        self.screenY = self.window.height / 2 / self.scale

    def render(self):
        largestDistance = 0
        for player in self.playerDisplayList:
            distance = math.sqrt((self.player.x - player.x) ** 2 + (self.player.y - player.y) ** 2)
            distance *= 16 / 9 * 2
            if distance > largestDistance:
                largestDistance = distance
        #if largestDistance >= 1280:
        #    self.scale = self.window.width / largestDistance
        #else:
        #    self.scale = self.window.width / 1280

        self.screenX = self.window.width / 2 / self.scale
        self.screenY = self.window.height / 2 / self.scale

        self.window.frameRate.startTimer("clear")
        if self.usePygame:
            self.display.fill((121, 202, 249))
        else:
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, self.window.width, self.window.height, fill = "#%02x%02x%02x" % (121, 202, 249))
            self.tkImageList.clear()
        self.window.frameRate.timeChange()

        self.showWalls()

        self.showCircles()

        self.showPlayer()

        self.showEnemies()

        self.showBullets()

        self.showGUI()

        self.window.frameRate.startTimer("update")
        if self.usePygame:
            pygame.display.update()
            self.window.root.update() #must update while in canvas in pygame but not in tkinter
        else:
            self.canvas.update()
        self.window.frameRate.timeChange()

    def showWalls(self):
        x1 = self.getScreenX(self.arenaSize + self.wallWidth / 2)
        y1 = self.getScreenY(self.arenaSize + self.wallWidth)
        x2 = self.getScreenX(self.arenaSize + self.wallWidth / 2)
        y2 = self.getScreenY(-self.arenaSize - self.wallWidth)
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.scale)

        x1 = self.getScreenX(self.arenaSize + self.wallWidth)
        y1 = self.getScreenY(-self.arenaSize - self.wallWidth / 2)
        x2 = self.getScreenX(-self.arenaSize - self.wallWidth)
        y2 = self.getScreenY(-self.arenaSize - self.wallWidth / 2)
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.scale)

        x1 = self.getScreenX(-self.arenaSize - self.wallWidth / 2)
        y1 = self.getScreenY(-self.arenaSize - self.wallWidth)
        x2 = self.getScreenX(-self.arenaSize - self.wallWidth / 2)
        y2 = self.getScreenY(self.arenaSize + self.wallWidth)
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.scale)

        x1 = self.getScreenX(-self.arenaSize - self.wallWidth)
        y1 = self.getScreenY(self.arenaSize + self.wallWidth / 2)
        x2 = self.getScreenX(self.arenaSize + self.wallWidth)
        y2 = self.getScreenY(self.arenaSize + self.wallWidth / 2)
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.scale)

    def showPlayer(self):
        self.showCircle(self.player.radius * self.scale, (self.getScreenX(self.player.x), self.getScreenY(self.player.y)), (0, 0, 255))
        healthWidth = 100
        healthHeight = 15
        healthOffset = self.player.radius + 15
        self.showRectangle(self.getScreenX(self.player.x - healthWidth / 2), self.getScreenY(self.player.y + healthOffset - healthHeight / 2),
                           self.getScreenX(self.player.x + healthWidth / 2), self.getScreenY(self.player.y + healthOffset + healthHeight / 2), (0, 255, 0), width=1)
        healthPercent = 1 - self.player.health / self.player.maxHealth
        self.showRectangle(self.getScreenX(self.player.x + healthWidth / 2 - healthPercent * healthWidth), self.getScreenY(self.player.y - healthHeight / 2 + healthOffset),
                           self.getScreenX(self.player.x + healthWidth / 2), self.getScreenY(self.player.y + healthHeight / 2 + healthOffset), (255, 0, 0), width=1)

    def showBullets(self):
        for bullet in self.player.bulletDisplayList:
            self.showCircle(bullet.radius * self.scale, (self.getScreenX(bullet.x), self.getScreenY(bullet.y)), (0, 0, 255))
        for player in self.playerDisplayList:
            for bullet in player.bulletDisplayList:
                self.showCircle(bullet.radius * self.scale, (self.getScreenX(bullet.x), self.getScreenY(bullet.y)), (255, 0, 0))

    def showEnemies(self):
        for player in self.playerDisplayList:
            self.showCircle(player.radius * self.scale, (self.getScreenX(player.x), self.getScreenY(player.y)), (255, 0, 0))
            healthWidth = 100
            healthHeight = 15
            healthOffset = player.radius + 15
            self.showRectangle(self.getScreenX(player.x - healthWidth / 2), self.getScreenY(player.y + healthOffset - healthHeight / 2),
                               self.getScreenX(player.x + healthWidth / 2), self.getScreenY(player.y + healthOffset + healthHeight / 2), (0, 255, 0), width=1)
            healthPercent = 1 - player.health / player.maxHealth
            self.showRectangle(self.getScreenX(player.x + healthWidth / 2 - healthPercent * healthWidth), self.getScreenY(player.y - healthHeight / 2 + healthOffset),
                               self.getScreenX(player.x + healthWidth / 2), self.getScreenY(player.y + healthHeight / 2 + healthOffset), (255, 0, 0), width=1)
            self.showText(player.name, (self.getScreenX(player.x), self.getScreenY(player.y + healthOffset + healthHeight + 25 * self.scale / 2)), (255, 0, 0), fontSize=int(25 * self.scale), bold=True, anchorCenter=True, outlineWidth=2)


    def showGUI(self):
        self.showRectangle(self.window.width - self.mapSize, self.window.height - self.mapSize, self.window.width, self.window.height, (121, 202, 249), 5)
        self.showCircle(self.player.radius * self.mapScale, (self.getMiniMapX(self.player.x), self.getMiniMapY(self.player.y)), (0, 0, 255))

        for circle in self.circleDisplayList:
            x = self.getMiniMapX(circle.x)
            y = self.getMiniMapY(circle.y)
            radius = circle.radius * self.mapScale
            if self.isInMiniMap(x, y, radius):
                self.showCircle(radius, (x, y), circle.color)

        for player in self.playerDisplayList:
            x = self.getMiniMapX(player.x)
            y = self.getMiniMapY(player.y)
            radius = player.radius * self.mapScale
            if self.isInMiniMap(x, y, radius):
                self.showCircle(radius, (x, y), (255, 0, 0))


        x1 = self.getMiniMapX(self.arenaSize + self.wallWidth / 2)
        y1 = self.getMiniMapY(self.arenaSize + self.wallWidth / 2)
        x2 = self.getMiniMapX(self.arenaSize + self.wallWidth / 2)
        y2 = self.getMiniMapY(-self.arenaSize - self.wallWidth / 2)
        if x1 < self.mapX - self.mapSize / 2:
            x1 += self.mapX - self.mapSize / 2 - x1
        if x1 > self.mapX + self.mapSize / 2:
            x1 += self.mapX + self.mapSize / 2 - x1
        if y1 < self.mapY - self.mapSize / 2:
            y1 += self.mapY - self.mapSize / 2 - y1
        if y1 > self.mapY + self.mapSize / 2:
            y1 += self.mapY + self.mapSize / 2 - y1
        if x2 < self.mapX - self.mapSize / 2:
            x2 += self.mapX - self.mapSize / 2 - x2
        if x2 > self.mapX + self.mapSize / 2:
            x2 += self.mapX + self.mapSize / 2 - x2
        if y2 < self.mapY - self.mapSize / 2:
            y2 += self.mapY - self.mapSize / 2 - y2
        if y2 > self.mapY + self.mapSize / 2:
            y2 += self.mapY + self.mapSize / 2 - y2
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.mapScale)

        x1 = self.getMiniMapX(self.arenaSize + self.wallWidth / 2)
        y1 = self.getMiniMapY(-self.arenaSize - self.wallWidth / 2)
        x2 = self.getMiniMapX(-self.arenaSize - self.wallWidth / 2)
        y2 = self.getMiniMapY(-self.arenaSize - self.wallWidth / 2)
        if x1 < self.mapX - self.mapSize / 2:
            x1 += self.mapX - self.mapSize / 2 - x1
        if x1 > self.mapX + self.mapSize / 2:
            x1 += self.mapX + self.mapSize / 2 - x1
        if y1 < self.mapY - self.mapSize / 2:
            y1 += self.mapY - self.mapSize / 2 - y1
        if y1 > self.mapY + self.mapSize / 2:
            y1 += self.mapY + self.mapSize / 2 - y1
        if x2 < self.mapX - self.mapSize / 2:
            x2 += self.mapX - self.mapSize / 2 - x2
        if x2 > self.mapX + self.mapSize / 2:
            x2 += self.mapX + self.mapSize / 2 - x2
        if y2 < self.mapY - self.mapSize / 2:
            y2 += self.mapY - self.mapSize / 2 - y2
        if y2 > self.mapY + self.mapSize / 2:
            y2 += self.mapY + self.mapSize / 2 - y2
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.mapScale)

        x1 = self.getMiniMapX(-self.arenaSize - self.wallWidth / 2)
        y1 = self.getMiniMapY(-self.arenaSize - self.wallWidth / 2)
        x2 = self.getMiniMapX(-self.arenaSize - self.wallWidth / 2)
        y2 = self.getMiniMapY(self.arenaSize + self.wallWidth / 2)
        if x1 < self.mapX - self.mapSize / 2:
            x1 += self.mapX - self.mapSize / 2 - x1
        if x1 > self.mapX + self.mapSize / 2:
            x1 += self.mapX + self.mapSize / 2 - x1
        if y1 < self.mapY - self.mapSize / 2:
            y1 += self.mapY - self.mapSize / 2 - y1
        if y1 > self.mapY + self.mapSize / 2:
            y1 += self.mapY + self.mapSize / 2 - y1
        if x2 < self.mapX - self.mapSize / 2:
            x2 += self.mapX - self.mapSize / 2 - x2
        if x2 > self.mapX + self.mapSize / 2:
            x2 += self.mapX + self.mapSize / 2 - x2
        if y2 < self.mapY - self.mapSize / 2:
            y2 += self.mapY - self.mapSize / 2 - y2
        if y2 > self.mapY + self.mapSize / 2:
            y2 += self.mapY + self.mapSize / 2 - y2
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.mapScale)

        x1 = self.getMiniMapX(-self.arenaSize - self.wallWidth / 2)
        y1 = self.getMiniMapY(self.arenaSize + self.wallWidth / 2)
        x2 = self.getMiniMapX(self.arenaSize + self.wallWidth / 2)
        y2 = self.getMiniMapY(self.arenaSize + self.wallWidth / 2)
        if x1 < self.mapX - self.mapSize / 2:
            x1 += self.mapX - self.mapSize / 2 - x1
        if x1 > self.mapX + self.mapSize / 2:
            x1 += self.mapX + self.mapSize / 2 - x1
        if y1 < self.mapY - self.mapSize / 2:
            y1 += self.mapY - self.mapSize / 2 - y1
        if y1 > self.mapY + self.mapSize / 2:
            y1 += self.mapY + self.mapSize / 2 - y1
        if x2 < self.mapX - self.mapSize / 2:
            x2 += self.mapX - self.mapSize / 2 - x2
        if x2 > self.mapX + self.mapSize / 2:
            x2 += self.mapX + self.mapSize / 2 - x2
        if y2 < self.mapY - self.mapSize / 2:
            y2 += self.mapY - self.mapSize / 2 - y2
        if y2 > self.mapY + self.mapSize / 2:
            y2 += self.mapY + self.mapSize / 2 - y2
        self.showLine((x1, y1), (x2, y2), (0, 0, 0), self.wallWidth * self.mapScale)


    def showCircles(self):
        for circle in self.circleDisplayList:
            self.showCircle(circle.radius * self.scale, (self.getScreenX(circle.x), self.getScreenY(circle.y)), circle.color)

    def showRectangle(self, x1, y1, x2, y2, color, width=0):
        if self.usePygame:
            pygame.draw.rect(self.display, color, ((x1, y1), (x2 - x1, y2 - y1)))
            if width != 0:
                pygame.draw.rect(self.display, (0, 0, 0), ((x1, y1), (x2 - x1, y2 - y1)), width)
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=tk_rgb, width=width)

    def showLine(self, position1, position2, color, width):
        if self.usePygame:
            pygame.draw.line(self.display, color, (int(position1[0]), int(position1[1])), (int(position2[0]), int(position2[1])), int(width))
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_line(position1[0], position1[1], position2[0], position2[1],
                                    fill=tk_rgb, width=width)

    def showText(self, text, position, color, fontName="Times", fontSize=12, bold=False, italic=False, anchorCenter=False, shadowWidth=0, secondaryColor=(0, 0, 0), outlineWidth=0):
        if self.usePygame:
            if outlineWidth!= 0:
                font = pygame.font.SysFont(fontName, fontSize, bold, italic)
                screenText = font.render(text, 1, secondaryColor)
                if anchorCenter:
                    textW = screenText.get_width()
                    textH = screenText.get_height()
                else:
                    textW = 0
                    textH = 0

                for angle in range(0, 361, int(8 / math.sqrt(outlineWidth)) + 1):
                    x = outlineWidth * math.sin(angle)
                    y = outlineWidth * math.cos(angle)
                    self.display.blit(screenText, (int(position[0] - textW / 2) + x, int(position[1] - textH / 2) + y))
            elif shadowWidth != 0:
                font = pygame.font.SysFont(fontName, fontSize, bold, italic)
                screenText = font.render(text, 1, secondaryColor)
                if anchorCenter:
                    textW = screenText.get_width()
                    textH = screenText.get_height()
                else:
                    textW = 0
                    textH = 0
                for shift in range(shadowWidth):
                    self.display.blit(screenText, (int(position[0] - textW / 2) + shift, int(position[1] - textH / 2)))
            font = pygame.font.SysFont(fontName, fontSize, bold, italic)
            screenText = font.render(text, 1, color)
            if anchorCenter:
                textW = screenText.get_width()
                textH = screenText.get_height()
            else:
                textW = 0
                textH = 0
            self.display.blit(screenText, (int(position[0] - textW / 2), int(position[1] - textH / 2)))

        else:
            tk_rgb = "#%02x%02x%02x" % color
            fontString = fontName + " " + str(fontSize)
            if bold:
                fontString += " bold"
            if italic:
                fontString += " italic"
            if anchorCenter:
                if outlineWidth!= 0:
                    secondary_tk_rgb = "#%02x%02x%02x" % secondaryColor
                    for angle in range(0, 361, int(8 / math.sqrt(outlineWidth)) + 1):
                        x = outlineWidth * math.sin(angle)
                        y = outlineWidth * math.cos(angle)
                        self.canvas.create_text(position[0] + x, position[1] + y, fill=secondary_tk_rgb, font=fontString, text=text)
                elif shadowWidth != 0:
                    secondary_tk_rgb = "#%02x%02x%02x" % secondaryColor
                    for shift in range(shadowWidth):
                        self.canvas.create_text(position[0] + shift, position[1], fill=secondary_tk_rgb, font=fontString, text=text)
                self.canvas.create_text(position[0], position[1], fill=tk_rgb, font=fontString, text=text)
            else:
                if outlineWidth!= 0:
                    secondary_tk_rgb = "#%02x%02x%02x" % secondaryColor
                    for angle in range(0, 361, int(8 / math.sqrt(outlineWidth)) + 1):
                        x = outlineWidth * math.sin(angle)
                        y = outlineWidth * math.cos(angle)
                        self.canvas.create_text(position[0] + x, position[1] + y, fill=secondary_tk_rgb, font=fontString, text=text, anchor=NW)
                elif shadowWidth != 0:
                    secondary_tk_rgb = "#%02x%02x%02x" % secondaryColor
                    for shift in range(shadowWidth):
                        self.canvas.create_text(position[0] + shift, position[1], fill=secondary_tk_rgb, font=fontString, text=text, anchor=NW)
                self.canvas.create_text(position[0], position[1], fill=tk_rgb, font=fontString, text=text, anchor=NW)


    def showImage(self, image, position, anchorCenter=False):
        if self.usePygame:
            if anchorCenter:
                imageW = image.get_width()
                imageH = image.get_height()
            else:
                imageW = 0
                imageH = 0
            self.display.blit(image, (int(position[0] - imageW / 2), int(position[1] - imageH / 2)))
        else:
            image = ImageTk.PhotoImage(image)
            self.tkImageList.append(image)
            if not anchorCenter:
                imageW = image.width()
                imageH = image.height()
            else:
                imageW = 0
                imageH = 0
            self.canvas.create_image((position[0] + imageW / 2, position[1] + imageH / 2), image=image)

    def showPolygon(self, pointList, color, position=(0, 0)):
        points = []
        for index in range(len(pointList)):
            points.append((pointList[index][0] + position[0], pointList[index][1] + position[1]))
        if self.usePygame:
            pygame.draw.polygon(self.display, color, points)
            pygame.draw.polygon(self.display, (0, 0, 0), points, 2)
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_polygon(points, outline='black', fill=tk_rgb, width=2)

    def showCircle(self, radius, position, color):
        try:
            if self.usePygame:
                pygame.draw.circle(self.display, color, (int(position[0]), int(position[1])), int(radius))
                pygame.draw.circle(self.display, (0, 0, 0), (int(position[0]), int(position[1])), int(radius), 2)
            else:
                tk_rgb = "#%02x%02x%02x" % color
                self.canvas.create_oval(position[0] - radius, position[1] - radius,
                                        position[0] + radius, position[1] + radius, fill=tk_rgb)
        except ValueError:
            pass

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)
        if self.usePygame:
            self.diplay = pygame.display.set_mode((self.window.width, self.window.height))
        else:
            self.canvas.config(width=self.window.width, height=self.window.height)

    def scaleImage(self, image, scale):
        newWidth = image.size[0] * scale
        wPercent = (newWidth/float(image.size[0]))
        hSize = int((float(image.size[1])*float(wPercent)))
        scaledImage = image.resize((int(newWidth), int(hSize)), PIL.Image.ANTIALIAS)
        return scaledImage

    def rotate(self, image, angle):
        if self.usePygame:
            return pygame.transform.rotate(image, angle)
        else:
            return self.rotatePIL(image, angle)

    def rotatePIL(self, image, angle):
        startSize = image.size
        imageString = image.convert('RGBA')
        rotatedImage = imageString.rotate(angle, expand=0).resize(startSize)
        finalImage = Image.new("RGBA", startSize, (255, 255, 255, 0))
        finalImage.paste(rotatedImage, (0, 0), rotatedImage)
        return finalImage

    def convertToDisplayFormat(self, image):
        if self.usePygame:
            imageBytes = image.convert('RGBA').tobytes("raw", 'RGBA')
            convertedImage = pygame.image.fromstring(imageBytes, image.size, 'RGBA')
        else:
            convertedImage = image
        return convertedImage

    def manipulateImage(self, image, scale, angle):
        scaledImage = self.scaleImage(image, scale)
        rotatedImage = self.rotatePIL(scaledImage, angle)
        finalImage = self.convertToDisplayFormat(rotatedImage)
        return finalImage

    def getScreenX(self, x):
        return (-self.player.x + self.screenX + x) * self.scale

    def getScreenY(self, y):
        return (self.player.y + self.screenY - y) * self.scale

    def getMiniMapX(self, x):
        return (-self.player.x + x) * self.mapScale + self.mapX

    def getMiniMapY(self, y):
        return (self.player.y - y) * self.mapScale + self.mapY

    def isInMiniMap(self, x, y, radius):
        if x - radius > self.mapX - self.mapSize / 2 and x + radius < self.mapX + self.mapSize / 2:
            if y - radius > self.mapY - self.mapSize / 2 and y + radius < self.mapY + self.mapSize / 2:
                return True
        return False