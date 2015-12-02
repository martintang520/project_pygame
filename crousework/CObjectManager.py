import pygame
from pygame.locals import *
from CObject import *
from CObjectAnimation import *
from CButton import *
from CTower import *
from CMonster import *
from CBullet import *
from CExplosion import *


class CObjectManager():
    def __init__(self):
        self.dictObject = {}
        self.index = 0

    ## update all object
    def UpdateList(self, deltaTime):
        if len(self.dictObject) > 0:
            for key in self.dictObject:
                self.dictObject[key].Update(deltaTime)
                
    ## render all object
    def RenderList(self, deltaTime, surface):
        if len(self.dictObject) > 0:
            for key in self.dictObject:
                self.dictObject[key].Render(deltaTime, surface)
        
    ## push a object node into object dictionary
    ## For each kind of object subclass should have different creat node meathod
    ## to guarantee override function and additional function can be called
    def CreateObjectNode(self, color, pos, size, pirtureName):
        newObject = CObject(color, pos, size, pirtureName)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    def CreateButtonNode(self, color, pos, size, pirtureName):
        newObject = CButton(color, pos, size, pirtureName)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    
    def CreateTowerNode(self, color, pos, size, TowerType):
        newObject = CTower(color, pos, size, TowerType)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    def CreateMonsterNode(self, color, pos, size, monsterProperty):
        newObject = CMonster(color, pos, size, monsterProperty)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    def CreateBulletNode(self, color, pos, size, pirtureName):
        newObject = CBullet(color, pos, size, pirtureName)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    def CreateObjectAnimationNode(self, color, initialPos, size, pictureName,
                                  width, farmeNumber):
        newObject = CObjectAnimation(color, initialPos, size, pictureName,
                                  width, farmeNumber)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    def CreateExplosionNode(self, color, initialPos, size, pictureName,
                                  width, farmeNumber):
        newObject = CExplosion(color, initialPos, size, pictureName,
                                  width, farmeNumber)
        self.dictObject[self.index] = newObject
        self.index += 1

        return self.index - 1

    ## delect the node in dictionary
    def DeleteObjectNode(self, index):

        if self.dictObject.has_key(index):
            delObj = self.dictObject.pop(index)
            del delObj

    def GetObject(self, index):
        if self.dictObject.has_key(index):
            return self.dictObject[index]
        else:
            return None

    def HaveKey(self, index):
        if self.dictObject.has_key(index):
            return True
        else:
            return False


    def ClearObjectDict(self):
        pass
