# -*- coding: cp936 -*-
import pygame
from pygame.locals import*
from CStage import *
from CObjectManager import *
from CMap import *

class CStageGame(CStage):
    
    def __init__(self, surface,sound):
        self.surface = surface
        self.myGameMap = CMap()
        self.myObjManger = CObjectManager()
        self.font = pygame.font.SysFont("Arial",20)  ## Font

        self.boolIsBuild=True

        self.dictTowerIndex = {}
        self.dictTowerType = {}

        self.currentIndex=[]
        self.currentTower=[]

        self.nMoney=200
        
        #self.Position=[]
        self.typeUpgrade ={1:4,2:5,4:4,5:5}
        
        self.GameInit()
        self.MusicInit(sound)

    ## game date init
    def GameInit(self):
        
        self.nMapNumber = 0
        self.listMap = self.myGameMap.listMapGroup[self.nMapNumber]
        self.myObjManger.CreateObjectNode((0, 0, 0), (0, 0),
                    self.surface.get_size(), "picture/background.png")
        self.DrawMap();

        ##test
        self.nOrder = 0
        self.nMonsterNumber = 0
        self.fInterval = 0.
        self.fGap = 0.
        self.listMonsterIndex = []
        self.listExplosionIndex = []
        self.dictBulletindex = {} ## bullet list
        self.listCreatMonster = [(0, 5, 5), (0, 3, 1), (1, 3, 5), (1, 6, 5),
                                 (0, 2, 1), (1, 2, 2), (2, 2, 5), (1, 4, 1),
                                 (2, 3, 5), (0, 5, 1), (2, 5, 5), (1, 7, 2),
                                 (2, 7, 5), (0, 0, 0)]
        self.dictMonsterType = {0:StuProperty(1, 30, 1.5, "picture/monster1.png",
                                            (0,1), self.listMap),
                                1:StuProperty(2, 30, 1., "picture/monster2.png",
                                            (0,1), self.listMap),
                                2:StuProperty(2, 50, 1.5, "picture/monster3.png",
                                            (0,1), self.listMap)}

        ## game over
        self.bGameWin = False
        self.bGameOver = False
        self.nLife = 10
        self.nOKIndex = -1


    def MusicInit(self, sound):
        self.SoundDeath = sound[0]
        self.SoundGold = sound[1]
        self.SoundExplore = sound[2]
        
    def Update(self,deltaTime):

        ## Game over break
        if self.GameOver():
            return
        
        self.myObjManger.UpdateList(deltaTime)

        self.MonsterCreater(deltaTime)
        self.GameOver()

        self.detection(deltaTime)
        self.bulletMovement(deltaTime)
        self.RemoveBullet()
        self.RemoveMonster()
        self.RemoveExplosion()

    
    def Render(self, deltaTime):
        self.myObjManger.RenderList(deltaTime, self.surface)
        self.surface.blit(self.font.render("Money : {} ".format(int(self.nMoney)),1,
                                               pygame.color.THECOLORS["white"]),(100, 0))
        self.surface.blit(self.font.render("Life : {} ".format(int(self.nLife)),1,
                                               pygame.color.THECOLORS["white"]),(230, 0))

        
    def DrawMap(self):
        self.listBuildingIndex = [] ## building list
        categoryPicture = {
            1 : "picture/path.png",
            2 : "picture/tree.png",
            3 : "picture/house.png",
            4 : "picture/blank.png",
            5 : "picture/path.png"}
        
        for x in range(0, 15):
            for y in range(0, 10):
                if self.listMap[y][x] == 0 or self.listMap[y][x] == 5:
                    continue
                else:
                    mapIndex = self.myObjManger.CreateObjectNode((0, 0, 0), (x * 64, y * 64),
                                 (64, 64), categoryPicture[self.listMap[y][x]])
                    if self.listMap[y][x] == 3:  ## record building list
                        self.listBuildingIndex.append(mapIndex)
                        
        self.myObjManger.CreateObjectNode((0, 0, 0), (8 * 64, 2 * 64),
                                 (128, 128), "picture/EiffelTower.png")
                    
    #create monster in update
    def MonsterCreater(self, deltaTime):
        if self.listCreatMonster[self.nOrder][2] == 0:
            return
            
        
        if self.nMonsterNumber < self.listCreatMonster[self.nOrder][1]:
            if self.fGap >= 1:
                monsterIndex = (self.myObjManger.CreateMonsterNode((0, 0, 0),
                    (0, 64), self.surface.get_size(),
                    self.dictMonsterType[self.listCreatMonster[self.nOrder][0]]))
                self.listMonsterIndex.append(monsterIndex)
                self.nMonsterNumber += 1
                self.fGap = 0
            else:
                self.fGap += deltaTime
            
        else:
            if self.fInterval >= self.listCreatMonster[self.nOrder][2]:
                self.fInterval = 0
                self.nMonsterNumber = 0
                self.nOrder += 1
            else:
                self.fInterval += deltaTime


    # to detect game win or lose
    def GameOver(self):
        
        if not (self.bGameWin or self.bGameOver):
            
            if (self.listCreatMonster[self.nOrder][2] == 0
                and len(self.listMonsterIndex) <= 0):
                self.myObjManger.CreateObjectNode((0, 0, 0), ((960 - 550) / 2, (640 - 366) / 2),
                    self.surface.get_size(), "picture/background2.png")
                self.myObjManger.CreateObjectNode((0, 0, 0), ((960 - 361) / 2, (640 - 100) / 2),
                    self.surface.get_size(), "picture/YouWin.png")
                ##return button
                self.nOKIndex = self.myObjManger.CreateButtonNode((0, 0, 0),
                    ((960 - 100) / 2, (640 - 100) / 2 + 100),(100,100), "picture/OKButton1.png")

                self.bGameWin = True

            if self.nLife <= 0:
                self.myObjManger.CreateObjectNode((0, 0, 0), ((960 - 550) / 2, (640 - 366) / 2),
                    self.surface.get_size(), "picture/background2.png")
                self.myObjManger.CreateObjectNode((0, 0, 0), ((960 - 447) / 2, (640 - 100) / 2),
                    self.surface.get_size(), "picture/GameOver.png")
                ##return button
                self.nOKIndex = self.myObjManger.CreateButtonNode((0, 0, 0),
                    ((960 - 100) / 2, (640 - 100) / 2 + 100),(100,100), "picture/OKButton1.png")
                self.bGameOver = True

        return self.bGameWin or self.bGameOver
    

    #start to build or update tower
    def MouseButtonDown(self,event):
        
        ## Game over break
        if self.GameOver():
            if self.myObjManger.HaveKey(self.nOKIndex):
                if self.myObjManger.dictObject[self.nOKIndex].OnButton(event):
                    CStage.SetStage(1)
            return

        clickPoint =  (event.pos[0] // 64, event.pos[1] // 64)
        
#player can build the tower by two mouse operations
#first click is to open the list of towers
#second click, after chosen, to build the chosen tower on blank
#self.boolIsBuild is to judge the state of click state,true means first click
#false means second click
        
        if self.boolIsBuild:
            self.boolIsBuild=False
            
            # get the blank of click position like(7,2) the total mape is a 15*10 metrix 
            self.tulCurrentPoint = self.GetPoint(event.pos)
            
            # if the click place is blank ,that means it can put a tower, else the place
            # is on tower, that means it can upgrade this tower
            # all situations can show a list of the build option 
            if self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
                self.Build(event)
            elif self.myGameMap.IsTower(self.nMapNumber, clickPoint):
                self.Upgrade(event)
        else:
            self.boolIsBuild=True
            self.unBuild()#close the list of tower
            
            if self.myGameMap.IsBlank(self.nMapNumber, self.tulCurrentPoint):
            # the current mouse click is on a blank box so the player can build a tower
            
                if self.BuildDecision(event,self.currentTower) !=-1:
                #-1 means player click other place to close the list
                    
                    if self.nMoney >= 100:
                    #nMoney is current money
                        
                        #build a tower and add the index of tower to the index dictionary
                        self.myGameMap.BuildTower(self.nMapNumber, self.tulCurrentPoint)             
                        self.AddIndex(self.myObjManger.CreateTowerNode((0, 0, 0),
                                                                       (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),
                                                                       (64,64),  self.BuildDecision(event,self.currentTower)+1),
                                     self.BuildDecision(event,self.currentTower)+1,self.tulCurrentPoint)
                        self.nMoney = self.nMoney -100
                    else:
                        if self.SoundGold.soundState():
                            self.SoundGold.play(1) # if the money is not enough and the soundstate is opened ,play sound1
                self.DeleteIndex()#clean the current index
                    
            elif self.myGameMap.IsTower(self.nMapNumber, self.tulCurrentPoint):
            #the mouse click is on a exist tower
                
                if self.UpgradeDecision(event,self.currentTower)!=-1:
                #-1 means player click other place to close the list
                    
                    if self.UpgradeDecision(event,self.currentTower)==1:
                    #1 means delete the tower
                        
                        self.deleteBuild(self.dictTowerIndex[self.tulCurrentPoint])
                        #delete the record of target tower in index dictionary and type dictionary
                        
                        self.dictTowerIndex.pop(self.tulCurrentPoint)
                        self.dictTowerType.pop(self.tulCurrentPoint)
                        self.myGameMap.DeleteTower(self.nMapNumber, self.tulCurrentPoint)
                        
                        # when player delete the tower, a blank box can instead the old one
                        self.myObjManger.CreateTowerNode((0, 0, 0), (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),(64,64),0)
                        self.nMoney += 50
                        
                    elif self.UpgradeDecision(event,self.currentTower)==2:
                    #2 means upgrade
                        
                        if self.nMoney >= 100:
                            #get the instance of tower by position ()and update
                            self.myObjManger.dictObject[self.dictTowerIndex[self.tulCurrentPoint]].SetType(self.typeUpgrade[self.dictTowerType[self.tulCurrentPoint]])
                            self.nMoney = self.nMoney -100
                        else:
                            if self.SoundGold.soundState():
                                self.SoundGold.play(1)
                                
                #finish the operation and clean the operation cache
                self.DeleteIndex()
                
    # mouse movement
    def MouseMotion(self,event):
        
        if self.GameOver():
            if self.myObjManger.HaveKey(self.nOKIndex):
                if self.myObjManger.dictObject[self.nOKIndex].OnButton(event):
                    self.myObjManger.dictObject[self.nOKIndex].SetImage("picture/OKButton2.png")
                else :
                    self.myObjManger.dictObject[self.nOKIndex].SetImage("picture/OKButton1.png")
            

    #build tower list
    def Build(self,event):

        ntower1=self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                                       (64,64),1)
        ntower2=self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),
                                                                       (64,64),2)
        self.AddNewIndex(ntower1)
        self.AddNewIndex(ntower2)
        
    #judge the player choice for build tower -1 means click other place
    def BuildDecision(self, event, tower):
        
        for n in range(len(tower)):
            if tower[n].OnButton(event) :
                
                return n
        return -1
    
    #judge the player choice for upgrade or delete tower 1 means delete
    def UpgradeDecision(self,event,tower):
        if tower[0].OnButton(event) :
            return 1
        elif tower[1].OnButton(event):
            return 2
        return -1

    
    # delete every the tower object of the list
    def unBuild(self):
        for n in self.currentIndex:
            self.myObjManger.DeleteObjectNode(n)
            
    #delete the object from objectmanage
    def deleteBuild(self,index):
        self.myObjManger.DeleteObjectNode(index)

    #update tower
    def Upgrade(self,event):
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                           (64,64),-1))
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),(64,64),
                                                           self.typeUpgrade[self.dictTowerType[self.tulCurrentPoint]]))
    ## for build or upgrade
    def AddNewIndex(self,index):
        
        self.currentIndex = self.currentIndex + [index]

        self.currentTower = self.currentTower + [self.myObjManger.GetObject(index)]
        
    #delete the list cache list
    def DeleteIndex(self):
        self.currentIndex=[]
        self.currentTower=[]

    ##get the box's left and top

    def GetPoint(self,position):
        return (position[0]//64,position[1]//64)
    
    def GetPointLeft(self,position):
        tulLeft=self.GetPoint(position)[0]*64
        return tulLeft

    
    def GetPointTop(self,position):
        tulTop=self.GetPoint(position)[1]*64
        return tulTop


    ## after build or upgrade, update the index and type dictionary in stagegame
    def AddIndex(self,index,buildtype,position):
        self.dictTowerIndex[position]=index
        self.dictTowerType[position]=buildtype


## finish to build or update


    #Each town can detects all of the monsters with using a equation of a Circle
    def detection(self,deltaTime):

        for tower in self.dictTowerIndex:
            for monster in self.listMonsterIndex:
                oTowner = self.myObjManger.dictObject[self.dictTowerIndex[tower]]
                oMonster =self.myObjManger.dictObject[monster]
                
                attackTime = oTowner.attacktimer
                # If the towner can dectect a monster, it will excute bulletAttack()
                if ((oMonster.tulPos[0] - oTowner.tulPos[0] + 32) ** 2 +
                         (oMonster.tulPos[1] - oTowner.tulPos[1] - 32) ** 2 <= oTowner.rangeTower ** 2 
                          and attackTime > 2):
                    self.myObjManger.dictObject[self.dictTowerIndex[tower]].attacktimer = 0
                    self.bulletAttack(self.dictTowerIndex[tower], monster)

    #Generate a bullet
    def bulletAttack(self, towerIndex, monsterIndex):

        newBullet = self.myObjManger.CreateBulletNode((0, 0, 0),
            self.myObjManger.dictObject[towerIndex].tulPos, (64, 64), "picture/bullet.png")
        self.dictBulletindex[newBullet] = (monsterIndex, towerIndex)
        self.myObjManger.dictObject[newBullet].nAttackPoint = self.myObjManger.dictObject[towerIndex].nAttackPoint

        #decelerated attack
        towerType = self.myObjManger.dictObject[towerIndex].nTowerType
        if towerType == 2 or towerType == 5:
            self.myObjManger.dictObject[newBullet].nAttackType = 1 

    # the movement of bullet
    def bulletMovement(self,deltaTime):
        
        for bullet in self.dictBulletindex:
            #the target exist or not
            if self.myObjManger.HaveKey(self.dictBulletindex[bullet][0]):
                self.myObjManger.dictObject[bullet].MoveUpdate(deltaTime,
                    self.myObjManger.dictObject[self.dictBulletindex[bullet][0]].tulPos)
            else:
                self.myObjManger.dictObject[bullet].bBomb = True

    #removw the bullet
    def RemoveBullet(self):

        key = -1
        
        for bullet in self.dictBulletindex:
            if self.myObjManger.dictObject[bullet].bBomb == True:
                # hp
                if self.myObjManger.HaveKey(self.dictBulletindex[bullet][0]):
                    self.myObjManger.dictObject[(self.dictBulletindex[bullet][0]
                        )].nHP -= (self.myObjManger.dictObject[bullet].nAttackPoint)

                    ##Deceleration
                    if self.myObjManger.dictObject[bullet].nAttackType == 1:
                        self.myObjManger.dictObject[self.dictBulletindex[bullet][0]].Decelerating()
                    
                key = bullet
                break
        # remove bullet
        if self.dictBulletindex.has_key(key):
            self.dictBulletindex.pop(key)
            self.myObjManger.DeleteObjectNode(key)

    # remove the monster
    def RemoveMonster(self):

        key = -1
        # When the monster die
        for monster in self.listMonsterIndex:
            if self.myObjManger.dictObject[monster].nHP <=0:
                # play the effect sound
                if self.SoundDeath.soundState():
                            self.SoundDeath.play(1)
                # earn money
                self.nMoney += 20
                key = monster
                break

            # a monster arrives the Eiffel Tower
            if self.myObjManger.dictObject[monster].bSuicideAttack == True:
                key = monster
                self.nLife -= 1
                
                ## demolish one building(life)
                for building in self.listBuildingIndex:

                    explosionPos = self.myObjManger.dictObject[building].tulPos
                    newExplosion = self.myObjManger.CreateExplosionNode((0, 0, 0),
                        explosionPos, (896, 64),"picture/explosion.png", 64, 14)
                    self.listExplosionIndex.append(newExplosion)
                    if self.SoundExplore.soundState():
                            self.SoundExplore.play(1)
                    
                    self.listBuildingIndex.remove(building)
                    self.myObjManger.DeleteObjectNode(building)
                                        
                    break
                    

        if key != -1:
            self.listMonsterIndex.remove(key)
            self.myObjManger.DeleteObjectNode(key)

    # remove the ecplosion
    def RemoveExplosion(self):

        key = -1
        
        for explosion in self.listExplosionIndex:
            if self.myObjManger.dictObject[explosion].bFinish == True:
                key = explosion
                self.listExplosionIndex.remove(key)
                self.myObjManger.DeleteObjectNode(key)
                break             



















