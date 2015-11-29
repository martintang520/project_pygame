import pygame

from pygame.locals import*

from CButton import *





class CTower(CButton):


    def __init__(self, color, initialPos, size, pictureName,rangeTower):

        CObject.__init__(self, color, initialPos, size, pictureName)

        self.rangeTower=rangeTower


    def Update(self, surface):
        pass


    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)

    def GetPosition(self):
        return self.tulPos

    def GetSize(self):
        return self.tulSize
