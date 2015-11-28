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

    def OnButton(self,event):

        if event.pos[0]>self.tulPos[0] and event.pos[0]<(self.tulPos[0]+self.tulSize[0])and event.pos[1]>self.tulPos[1] and event.pos[1]<(self.tulPos[1]+self.tulSize[1]):

            return True
        else:
            return False
