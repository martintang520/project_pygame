import pygame

from pygame.locals import*

from CButton import *





class CTower(CButton):


    def __init__(self, color, initialPos, size, pictureName,Towertype):

        CObject.__init__(self, color, initialPos, size, pictureName)

        self.nTowerType=Towertype
        self.attacktimer = 2
        self.GameInit()

    def GameInit(self):
        self.rangeTower = 192
        if self.nTowerType>0:
            self.nAttackPoint = 10*(self.nTowerType/3+1)

    def Update(self, deltaTime):
        self.attacktimer += deltaTime
        pass


    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)

    def GetPosition(self):
        return self.tulPos

    def GetSize(self):
        return self.tulSize
