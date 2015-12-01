import pygame
from pygame.locals import*
from CObjectAnimation import *

class CExplosion(CObjectAnimation):


    def __init__(self, color, initialPos, size, pictureName, width, farmeNumber,
                 playSpeed = 0.2, loop = False):

        CObjectAnimation.__init__(self, color, initialPos, size, pictureName,
                                  width, farmeNumber)


    def Update(self, deltaTime):
        CObjectAnimation.Update(self, deltaTime)


    def Render(self, deltaTime, surface):
        CObjectAnimation.Render(self, deltaTime, surface)
