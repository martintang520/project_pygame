import pygame
from pygame.locals import*
from CObject import *


class CButton(CObject):
    def __init__(self, color, initialPos, size, pictureName):
        CObject.__init__(self, color, initialPos, size, pictureName)


    def Update(self, surface):
        pass

    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)

    def GetPosition(self):
        return self.tulPos

    def GetSize(self):
        return self.tulSize
