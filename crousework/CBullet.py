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

             
        self.tupMonsterSpeed = [0,0] #Monster Speed, tup type#
        self.nBulletSpeed = 0 #Bullet Speed, int type#
        self.nMonsterSpeed = 0 #Monster speed, int type#
        self.tupCloseSpeed = [0,0] #Close speed, tup type#
        self.tupTargetPos = [0,0] #the target monster position, tup type#
        self.tupTargetDistance = [0,0]  #the target distance, tup type#
        self.tulPos = initialPos #the initial position of Bullet, is also the Bullet position#
        self.tupBulletUpPos = [0,0] #the current position of Bullet#

    def Update(self, deltaTime):       
        pass        


    def Render(self, deltaTime, surface):

        CObject.Render(self, deltaTime, surface)
    #bullet Update#   
    def MoveUpdate(self,deltaTime,MonsterPos):
        
        if (self.bDecide == True):
            self.tupMonsterPos =  MonsterPos #Monster Position, tup type#
            self.fDeltaTime = deltaTime #deltaTime# 
            self.bDecide = False 
            self.tupMonsterOldPos = self.tupMonsterPos #Old position equal current Position#
              
        self.tupMonsterPos =  MonsterPos #The Monster Position, tup type#
        self.fDeltaTime = deltaTime 
        self.tupBulletSpeed = [150,150]  #The speed of Bullet, tup type#   

        #The speed of Monster, distance divide time#                   
        self.tupMonsterSpeed[0] = (self.tupMonsterPos[0]-self.tupMonsterOldPos[0])/self.fDeltaTime 
        self.tupMonsterSpeed[1] = (self.tupMonsterPos[1]-self.tupMonsterOldPos[1])/self.fDeltaTime          
        self.tupMonsterOldPos = self.tupMonsterPos

        #The Close speed, Bullet speed minus monsterSpeed,tup type#
        self.tupCloseSpeed[0] = abs(self.tupBulletSpeed[0] - self.tupMonsterSpeed[0]) 
        self.tupCloseSpeed[1] = abs(self.tupBulletSpeed[1] - self.tupMonsterSpeed[1])

        #The Close Distance,Monster Position minus Bullet position#     
        self.nCloseDistance1=(self.tupMonsterPos[0]-self.tulPos[0])*(self.tupMonsterPos[0]-self.tulPos[0])+(self.tupMonsterPos[1]-self.tulPos[1])*(self.tupMonsterPos[1]-self.tulPos[1])
        self.nCloseDistance =math.sqrt(self.nCloseDistance1)

        #The Close speed, int type#      
        self.nCloseSpeed1 =self.tupCloseSpeed[0]*self.tupCloseSpeed[0]+self.tupCloseSpeed[1]*self.tupCloseSpeed[1]
        self.nCloseSpeed = math.sqrt(self.nCloseSpeed1)

        #The Close Time equals Close Distance divide Closespeed#                
        self.nCloseTime=self.nCloseDistance/self.nCloseSpeed 

        #Target Position equals init position add move distance#
        self.tupTargetPos[0] = self.tupMonsterPos[0] + self.tupMonsterSpeed[0]*self.nCloseTime
        self.tupTargetPos[1] = self.tupMonsterPos[1] + self.tupMonsterSpeed[1]*self.nCloseTime

        #Target distance,target position minus init position#
        self.tupTargetDistance[0] = self.tupTargetPos[0] - self.tulPos[0]
        self.tupTargetDistance[1] = self.tupTargetPos[1] - self.tulPos[1]

        #Calculate current BulletSpeed#
        self.tupBulletSpeed[0] = (self.tupTargetDistance[0]/self.nCloseTime)*deltaTime
        self.tupBulletSpeed[1] = (self.tupTargetDistance[1]/self.nCloseTime)*deltaTime

        #The monster current Position#
        self.tupBulletUpPos[0] = self.tulPos[0] + self.tupBulletSpeed[0]              
        self.tupBulletUpPos[1] = self.tulPos[1] + self.tupBulletSpeed[1]
        self.tulPos = self.tupBulletUpPos
        
        #Wether shot target#      
        if abs(self.tulPos[0] - self.tupMonsterPos[0]) + abs(self.tulPos[1] - self.tupMonsterPos[1]) < 10:
            self.bBomb = True
              
              
