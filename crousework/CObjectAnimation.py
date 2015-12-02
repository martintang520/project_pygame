import pygame
from pygame.locals import*
from CObject import *

class CObjectAnimation(CObject):


    def __init__(self, color, initialPos, size, pictureName, width, farmeNumber,
                 playSpeed = 0.05, loop = False):

        self.tulSize = size #size of picture#
        self.tulPos = initialPos #initPosition#
        self.fTimePerFrame = playSpeed #number of seconds for each frame#
        self.fSinceLastFrame = 0
        self.nCurrentFrame = 0
        self.nFarmeNumber = farmeNumber #total number frame of every picture#
        self.bLoop = loop #whether Loop#
        self.bFinish = False #whether finish#
        self.LoadImage(pictureName, width, farmeNumber)
        self.image = self.images[self.nCurrentFrame]


    def Update(self, deltaTime):

        
        self.fSinceLastFrame += deltaTime

        #if time equal speed then next frame#
        if self.fSinceLastFrame >= self.fTimePerFrame:
            self.nCurrentFrame += 1 
            self.fSinceLastFrame = 0 #lastframe become zero#
            #one loop finish#
            if self.nCurrentFrame > self.nFarmeNumber - 1:
                if self.bLoop:
                    nCurrentFrame = 0
                else:
                    self.bFinish = True
                    return
            self.image = self.images[self.nCurrentFrame]


    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)

    #function Loadimage#
    def LoadImage(self, fileName, width, number):
        #change image to transtion channel#
        myImage = pygame.image.load(fileName).convert_alpha()

        #get image height#
        height = myImage.get_height()

        #separate a long image to several images, then make a list#
        self.images = [myImage.subsurface(Rect((i * width, 0), (width, height))
                    ) for i in range(number)]
