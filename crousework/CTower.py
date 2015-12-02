import pygame
from pygame.locals import*
from CButton import *

class CTower(CButton):
    
#Tower name dictionary
    dictTowerName={-1:"picture/cross.png",0:"picture/blank.png",
                   1:"picture/tower1.png",2:"picture/tower2.png",
                   4:"picture/tower4.png",5:"picture/tower5.png"}

#Tower Attack Point
    dictTowerAttackPoint = {1:10,2:5,4:20,5:10}

    def __init__(self, color, initialPos, size, Towertype):

        CObject.__init__(self, color, initialPos, size, self.dictTowerName[Towertype])

        self.nTowerType = Towertype
        self.attacktimer = 2
        self.GameInit()

    def GameInit(self):
        self.rangeTower = 192 #tower attack range 192 are 3 block
        #set attack point
        if self.nTowerType > 0:
            self.nAttackPoint = self.dictTowerAttackPoint[self.nTowerType]

    def Update(self, deltaTime):
        self.attacktimer += deltaTime
        pass


    def Render(self, deltaTime, surface):
        CObject.Render(self, deltaTime, surface)
        
#position tulple like (300,100)
    def GetPosition(self):
        return self.tulPos
    
#Size tulple like (64,64)
    def GetSize(self):
        return self.tulSize
    
# set tower type. like type 1 type 2 type 3 type 4
    def SetType(self, Towertype):
        self.nTowerType = Towertype
        self.SetImage(self.dictTowerName[Towertype])
        if self.nTowerType > 0:
            self.nAttackPoint = self.dictTowerAttackPoint[self.nTowerType]


