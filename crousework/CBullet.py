import pygame

from pygame.locals import*

from CObject import *

import math


class CBullet(CObject):

    def __init__(self, color, initialPos, size, pictureName):
        CObject.__init__(self,color, initialPos, size, pictureName)
        self.bDecide = True
        self.bBomb = False
        self.nAttackPoint = 0
        self.nAttackType = 0 ## decelerated attack

             
        self.tupMonsterSpeed = [0,0]
        self.nBulletSpeed = 0
        self.nMonsterSpeed = 0
        self.tupCloseSpeed = [0,0]
        self.tupTargetPos = [0,0]
        self.tupTargetDistance = [0,0]
        self.tulPos = initialPos
        self.tupBulletUpPos = [0,0]

    def Update(self, deltaTime):       
        pass        


    def Render(self, deltaTime, surface):

        CObject.Render(self, deltaTime, surface)

    def MoveUpdate(self,deltaTime,MonsterPos):
        
        if (self.bDecide == True):
            self.tupMonsterPos =  MonsterPos ##the position of Monster
            self.fDeltaTime = deltaTime
            self.bDecide = False
            self.tupMonsterOldPos = self.tupMonsterPos
              
        self.tupMonsterPos =  MonsterPos ##the position of Monster
        self.fDeltaTime = deltaTime
        self.tupBulletSpeed = [150,150]                     
        self.tupMonsterSpeed[0] = (self.tupMonsterPos[0]-self.tupMonsterOldPos[0])/self.fDeltaTime ##the speed of Monster
        self.tupMonsterSpeed[1] = (self.tupMonsterPos[1]-self.tupMonsterOldPos[1])/self.fDeltaTime
              
        self.tupMonsterOldPos = self.tupMonsterPos
        self.tupCloseSpeed[0] = abs(self.tupBulletSpeed[0] - self.tupMonsterSpeed[0]) ##Close Speed
        self.tupCloseSpeed[1] = abs(self.tupBulletSpeed[1] - self.tupMonsterSpeed[1])
              
        self.nCloseDistance1=(self.tupMonsterPos[0]-self.tulPos[0])*(self.tupMonsterPos[0]-self.tulPos[0])+(self.tupMonsterPos[1]-self.tulPos[1])*(self.tupMonsterPos[1]-self.tulPos[1])
        self.nCloseDistance =math.sqrt(self.nCloseDistance1)
              
        self.nCloseSpeed1 =self.tupCloseSpeed[0]*self.tupCloseSpeed[0]+self.tupCloseSpeed[1]*self.tupCloseSpeed[1]
        self.nCloseSpeed = math.sqrt(self.nCloseSpeed1)

                     
        self.nCloseTime=self.nCloseDistance/self.nCloseSpeed ##get Time
        self.tupTargetPos[0] = self.tupMonsterPos[0] + self.tupMonsterSpeed[0]*self.nCloseTime
        self.tupTargetPos[1] = self.tupMonsterPos[1] + self.tupMonsterSpeed[1]*self.nCloseTime
        self.tupTargetDistance[0] = self.tupTargetPos[0] - self.tulPos[0]
        self.tupTargetDistance[1] = self.tupTargetPos[1] - self.tulPos[1]

        self.tupBulletSpeed[0] = (self.tupTargetDistance[0]/self.nCloseTime)*deltaTime
        self.tupBulletSpeed[1] = (self.tupTargetDistance[1]/self.nCloseTime)*deltaTime
              
        self.tupBulletUpPos[0] = self.tulPos[0] + self.tupBulletSpeed[0]              
        self.tupBulletUpPos[1] = self.tulPos[1] + self.tupBulletSpeed[1]
        self.tulPos = self.tupBulletUpPos
              
        if abs(self.tulPos[0] - self.tupMonsterPos[0]) + abs(self.tulPos[1] - self.tupMonsterPos[1]) < 10:
            self.bBomb = True
              
              
