import pygame

from pygame.locals import*

from CObject import *


class CBullet(CObject):

    def __init__(self, color, initialPos, size, pictureName):

        CObject.__init__(self, color, initialPos, size, pictureName)

       

    def Update(self, surface):

        pass


    def Render(self, deltaTime, surface):

        CObject.Render(self, deltaTime, surface)

