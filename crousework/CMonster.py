import pygame
from pygame.locals import*
from CObject import *
import copy

class StuProperty:   ## Property of monster
    def __init__(self, monsterType, HP, speed, pictureName, endPos, gameMap):
        self.nType          = monsterType     ## type
        self.nHP            = HP              ## Hp
        self.nSpeed         = speed           ## speed
        self.strPictureName = pictureName     ## picture name
        self.tupEndPos      = endPos          ## end position
        self.listMap        = gameMap         ## game map

class CMonster(CObject):

    Direction = {0:(1, 0), 1:(0, 1), 2:(-1, 0), 3:(0, -1)}

    def __init__(self, color, initialPos, size, monsterProperty):
               
        self.tulSize = size
        self.tulPos = initialPos
        self.nOrder = 0
        self.DataInit(monsterProperty)

        self.nStepsPerTile = 4. ## How many step walking though a tile 
        self.nFrames = 4.  ## numbers of frames
        self.fTimePerFrame = self.nSpeed / self.nStepsPerTile / self.nFrames

        self.fSinceLastFrame = 0.
        self.nCurrentFrame = 0
        self.nCurrentStep = 0
        self.tupVelocity = (0,0)
        self.tupTileSize = (64,64)
        
        self.bWalking = False
        self.tupCurrentPos = self.PosConvert(initialPos)
        self.tupTargetPos = self.tupCurrentPos
        self.tupVelocity = (0, 0)

        self.tupNext = (0,0)
        self.bchangeDirection = False ##Change Frame picture

        ## suicide attack
        self.bSuicideAttack = False


    def DataInit(self, monsterProperty):
        
        self.LoadImage(monsterProperty.strPictureName, 64, 8)
        self.image = self.images[self.nOrder]
        
        self.nType = monsterProperty.nType
        self.nHP = monsterProperty.nHP
        self.nSpeed = monsterProperty.nSpeed
        self.tupEndPos = monsterProperty.tupEndPos
        self.listMap = copy.deepcopy(monsterProperty.listMap)


    def Update(self, deltaTime):

        if not self.bWalking:
            self.Next()
            return

        ## move and walking animation
        self.fSinceLastFrame += deltaTime
        if self.fSinceLastFrame >= self.fTimePerFrame * (
            self.nCurrentStep * self.nFrames + self.nCurrentFrame):
            self.tulPos = (self.tulPos[0] + self.tupVelocity[0],
                           self.tulPos[1] + self.tupVelocity[1])

            if self.bchangeDirection == True:
                self.image = self.images[self.nCurrentFrame]
            else:
                self.image = self.images[self.nCurrentFrame + 4]
            
            self.nCurrentFrame += 1
            if self.nCurrentFrame >= self.nFrames:
                self.nCurrentStep += 1
                self.nCurrentFrame = 0
            if self.nCurrentStep >= self.nStepsPerTile:
                self.tupCurrentPos = self.tupTargetPos
                self.bWalking = False
            

    def Render(self, deltaTime, surface):

        CObject.Render(self, deltaTime, surface)

    def PosConvert(self, pos):
        return (pos[0] // 64, pos[1] // 64)


    ## monster walk to one adjacent cell
    def WalkTo(self, row, col):
        ## cannot move more than one cell one time
        if (abs(row - self.tupCurrentPos[1]) + abs(
            col - self.tupCurrentPos[0]) > 1):
            return

        ## get vector from current position to target
        if self.tupCurrentPos[0] != col or self.tupCurrentPos[1] != row:
            self.bWalking = True
            self.tupTargetPos = (col, row)

            self.fSinceLastFrame = 0
	    self.nCurrentFrame = 0
	    self.nCurrentStep = 0

	    x1 = ((self.tupTargetPos[0] - self.tupCurrentPos[0])
                  * self.tupTileSize[0] / self.nStepsPerTile / self.nFrames)
	    y1 = ((self.tupTargetPos[1] - self.tupCurrentPos[1])
                  * self.tupTileSize[1] / self.nStepsPerTile / self.nFrames)
	    self.tupVelocity = (x1, y1)

    ## only path can be pass
    def CanPass(self, pos):
        if self.listMap[pos[1]][pos[0]] == 1:
            return True
        ## reach Eiffel Tower
        elif self.listMap[pos[1]][pos[0]] == 5:
            self.bSuicideAttack = True
        else:
            return False
        
    
    def Next(self):
        ## change the map number as the path have been passed
        self.listMap[self.tupCurrentPos[1]][self.tupCurrentPos[0]] = -1
        for i in range(4):
            if (self.tupCurrentPos[0] + CMonster.Direction[i][0] >= 0 and
                self.tupCurrentPos[0] + CMonster.Direction[i][0] < 14 and
                self.tupCurrentPos[1] + CMonster.Direction[i][1] >= 0 and
                self.tupCurrentPos[1] + CMonster.Direction[i][1] < 14):
                
                self.tupNext = (self.tupCurrentPos[0] + CMonster.Direction[i][0],
                                self.tupCurrentPos[1] + CMonster.Direction[i][1])

                if self.CanPass(self.tupNext):
                    if CMonster.Direction[i][0] < 0:
                        self.bchangeDirection = False
                    else:
                        self.bchangeDirection = True
                        
                    self.WalkTo(self.tupNext[1], self.tupNext[0])


    def LoadImage(self, fileName, width, number):
        myImage = pygame.image.load(fileName).convert_alpha()
        
        height = myImage.get_height()

        self.images = [myImage.subsurface(Rect((i * width, 0), (width, height))
                    ) for i in range(number)]
            
