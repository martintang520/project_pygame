import pygame
from pygame.locals import*
from CObject import *

class StuProperty:   ## Property of monster
    def __init__(self, monsterType, HP, speed, pictureName):
        self.nType          = monsterType     ## type
        self.nHP            = HP              ## Hp
        self.nSpeed         = speed           ## speed
        self.strPictureName = pictureName     ## picture name

class CMonster(CObject):

    def __init__(self, color, initialPos, size, monsterProperty):
               
        self.tulSize = size
        self.tulPos = initialPos
        self.DataInit(monsterProperty)


    def DataInit(self, monsterProperty):
        self.image = pygame.image.load(monsterProperty.strPictureName
                                       ).convert_alpha() 
        self.nType = monsterProperty.nType
        self.nHP = monsterProperty.nHP
        self.nSpeed = monsterProperty.nSpeed


    def Update(self, surface):

        pass



    def Render(self, deltaTime, surface):

        CObject.Render(self, deltaTime, surface)
