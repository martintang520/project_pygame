import pygame

from pygame.locals import*

from CButton import *





class CTower(CButton):
    dictTowerName={-1:"picture/cross.png",0:"picture/blank.png",1:"picture/tower1.png",2:"picture/tower2.png",4:"picture/tower4.png",5:"picture/tower5.png"}
    dictTowerAttackPoint = {1:10,2:5,4:20,5:10}

    def __init__(self, color, initialPos, size,Towertype):

        CObject.__init__(self, color, initialPos, size, self.dictTowerName[Towertype])

        self.nTowerType=Towertype
        self.attacktimer = 2
        self.GameInit()

    def GameInit(self):
        self.rangeTower = 192
        if self.nTowerType>0:
            self.nAttackPoint = self.dictTowerAttackPoint[self.nTowerType]

    def Update(self, deltaTime):
        self.attacktimer += deltaTime
        pass


    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)

    def GetPosition(self):
        return self.tulPos

    def GetSize(self):
        return self.tulSize

    def SetType(self,Towertype):
        self.nTowerType=Towertype
        self.SetImage(self.dictTowerName[Towertype])
        if self.nTowerType>0:
            self.nAttackPoint = self.dictTowerAttackPoint[self.nTowerType]


