import pygame
from pygame.locals import*
from CObject import *

class StuProperty:   ## Property of monster
    def __init__(self, monsterType, HP, speed):
        self.nType   = monsterType     ## type
        self.nHP     = HP              ## Hp
        self.nSpeed  = speed           ## speed

class CMonster(CObject):

    def __init__(self, color, initialPos, size, pictureName, monsterProperty):
        CObject.__init__(self, color, initialPos, size, pictureName)
        self.DataInit(monsterProperty)


    def DataInit(self, monsterProperty):
        self.nType = monsterProperty.nType
        self.nHP = monsterProperty.nHP
        self.nSpeed = monsterProperty.nSpeed


    def Update(self, surface):

        pass



    def Render(self, deltaTime, surface):

        CObject.Render(self, deltaTime, surface)
