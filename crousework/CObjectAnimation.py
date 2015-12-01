import pygame
from pygame.locals import*
from CObject import *

class CObjectAnimation(CObject):


    def __init__(self, color, initialPos, size, pictureName, width, farmeNumber,
                 playSpeed = 0.05, loop = False):

        self.tulSize = size
        self.tulPos = initialPos
        self.fTimePerFrame = playSpeed
        self.fSinceLastFrame = 0
        self.nCurrentFrame = 0
        self.nFarmeNumber = farmeNumber
        self.bLoop = loop
        self.bFinish = False
        self.LoadImage(pictureName, width, farmeNumber)
        self.image = self.images[self.nCurrentFrame]


    def Update(self, deltaTime):

        self.fSinceLastFrame += deltaTime
        if self.fSinceLastFrame >= self.fTimePerFrame:
            self.nCurrentFrame += 1
            self.fSinceLastFrame = 0
            if self.nCurrentFrame > self.nFarmeNumber - 1:
                if self.bLoop:
                    nCurrentFrame = 0
                else:
                    self.bFinish = True
                    return
            self.image = self.images[self.nCurrentFrame]


    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)


    def LoadImage(self, fileName, width, number):
        myImage = pygame.image.load(fileName).convert_alpha()
        
        height = myImage.get_height()

        self.images = [myImage.subsurface(Rect((i * width, 0), (width, height))
                    ) for i in range(number)]
