import pygame
from pygame.locals import*
from CStage import *
from CObjectManager import *
from CMap import *

class CStageGame(CStage):
    
    def __init__(self, surface):
        self.surface = surface
        self.myGameMap = CMap()
        self.myObjManger = CObjectManager()

        self.boolIsBuild=True

        self.dictTowerIndex = {}
        self.dictTowerType = {}

        self.currentIndex=[]
        self.currentTower=[]

        #self.Position=[]
        self.typeUpgrade =[(1,4),(2,5),(3,6),(4,7),(5,8),(6,9),(7,7),(8,8),(9,9)]

        self.GameInit()
        ##self.MusicInit(sound)

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
        self.dictBulletindex = {} ## bullet list
        self.listCreatMonster = [(0, 5, 5), (0, 3, 3), (1, 3, 5), (0, 0, 0)]
        self.dictMonsterType = {0:StuProperty(1, 20, 1.5, "picture/monster1.png",
                                            (0,1), self.listMap),
                                1:StuProperty(2, 20, 1., "picture/monster2.png",
                                            (0,1), self.listMap)}

        ## game over
        self.bGameWin = False
        self.bGameOver = False
        self.nLife = 10

        self.myObjManger.CreateExplosionNode((0, 0, 0), (0, 0), (896, 64),
                        "picture/explosion.png", 64, 14)


    def MusicInit(self, sound):
        self.Sound = sound
        self.boolSound = self.Sound.soundState()
        self.Sound.play(1)
        
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

    
    def Render(self, deltaTime):
        self.myObjManger.RenderList(deltaTime, self.surface)

        
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
                    
    ##create monster in update
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
                print self.nMonsterNumber
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

    ## to detect game win or lose
    def GameOver(self):
        if (self.listCreatMonster[self.nOrder][2] == 0
            and len(self.listMonsterIndex) <= 0):
            self.bGameWin = True

        if self.nLife <= 0:
            self.bGameOver = True

        return self.bGameWin or self.bGameOver

##start to build or update tower
    def MouseButtonDown(self,event):

        ## Game over break
        if self.GameOver():
            return

        clickPoint =  (event.pos[0] // 64, event.pos[1] // 64)
        
        if self.boolIsBuild:
            self.boolIsBuild=False
            self.tulCurrentPoint = self.GetPoint(event.pos)
            
            if self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
                self.Build(event)
            elif self.myGameMap.IsTower(self.nMapNumber, clickPoint):
                self.Upgrade(event)
        else:
            self.boolIsBuild=True
            self.unBuild()
            if self.myGameMap.IsBlank(self.nMapNumber, self.tulCurrentPoint):
                if self.BuildDecision(event,self.currentTower) !=-1:
                    self.myGameMap.BuildTower(self.nMapNumber, self.tulCurrentPoint)
                    self.AddIndex(self.myObjManger.CreateTowerNode((0, 0, 0),
                                                                   (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),
                                                                   (64,64), "picture/tower"+str(self.BuildDecision(event,self.currentTower)+1)+".png",self.BuildDecision(event,self.currentTower)+1),
                                 self.BuildDecision(event,self.currentTower)+1,self.tulCurrentPoint)
                self.DeleteIndex()
                    
            elif self.myGameMap.IsTower(self.nMapNumber, self.tulCurrentPoint):
                if self.UpgradeDecision(event,self.currentTower)!=-1:
                    if self.UpgradeDecision(event,self.currentTower)==1:
                        
                        self.deleteBuild(self.dictTowerIndex[self.tulCurrentPoint])
                        self.dictTowerIndex.pop(self.tulCurrentPoint)
                        self.dictTowerType.pop(self.tulCurrentPoint)
                        self.myGameMap.DeleteTower(self.nMapNumber, self.tulCurrentPoint)
                        self.myObjManger.CreateTowerNode((0, 0, 0), (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),(64,64),
                                                           "picture/blank.png",0)
                    elif self.UpgradeDecision(event,self.currentTower)==2:
                        self.deleteBuild(self.dictTowerIndex[self.tulCurrentPoint])
                        self.AddIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),(64,64),
                                                                        "picture/tower"+str(self.typeUpgrade[self.dictTowerType[self.tulCurrentPoint]-1][1])+".png",self.dictTowerType[self.tulCurrentPoint]),
                                      self.typeUpgrade[self.dictTowerType[self.tulCurrentPoint]-1][1],self.tulCurrentPoint)
  
                self.DeleteIndex()

    ##build tower
    def Build(self,event):

        ntower1=self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower1.png",1)
        ntower2=self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower2.png",2)
        ntower3=self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)-64,self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower3.png",3)
        self.AddNewIndex(ntower1)
        self.AddNewIndex(ntower2)
        self.AddNewIndex(ntower3)

    def BuildDecision(self, event, tower):
        
        for n in range(len(tower)):
            if tower[n].OnButton(event) :
                
                return n
        return -1

    def unBuild(self):
        for n in self.currentIndex:
            self.myObjManger.DeleteObjectNode(n)
            
    def deleteBuild(self,index):
        self.myObjManger.DeleteObjectNode(index)

    ##update tower
    def Upgrade(self,event):
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                           (64,64), "picture/cross.png",-1))
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),(64,64),
                                                           "picture/tower"+str(self.typeUpgrade[self.dictTowerType[self.tulCurrentPoint]-1][1])+".png",self.typeUpgrade[self.dictTowerType[self.tulCurrentPoint]-1][1]))          


    ## for build or upgrade
    def AddNewIndex(self,index):

        self.currentIndex = self.currentIndex + [index]

        self.currentTower = self.currentTower + [self.myObjManger.GetObject(index)]
    
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


    ## after build or upgrade 
    def AddIndex(self,index,buildtype,position):
        self.dictTowerIndex[position]=index
        self.dictTowerType[position]=buildtype


    def UpgradeDecision(self,event,tower):
        if tower[0].OnButton(event) :
            return 1
        elif tower[1].OnButton(event):
            return 2
        return -1

## finish to build or update


#Each town detects all of the monsters
    def detection(self,deltaTime):

        for k in self.dictTowerIndex:
            for j in self.listMonsterIndex:
                oTowner = self.myObjManger.dictObject[self.dictTowerIndex[k]]
                oMonster =self.myObjManger.dictObject[j]
                
                attackTime = oTowner.attacktimer
                if ((oMonster.tulPos[0] - oTowner.tulPos[0] + 32) ** 2 +
                         (oMonster.tulPos[1] - oTowner.tulPos[1] - 32) ** 2 <= oTowner.rangeTower ** 2 
                          and attackTime > 2):
                    self.myObjManger.dictObject[self.dictTowerIndex[k]].attacktimer = 0
                    self.bulletAttack(self.dictTowerIndex[k], j)


    def bulletAttack(self, towerIndex, monsterIndex):

        newBullet = self.myObjManger.CreateBulletNode((0, 0, 0),
            self.myObjManger.dictObject[towerIndex].tulPos, (64, 64), "picture/bullet.png")
        self.dictBulletindex[newBullet] = (monsterIndex, towerIndex)


    def bulletMovement(self,deltaTime):
        
        for bullet in self.dictBulletindex:
            if self.myObjManger.HaveKey(self.dictBulletindex[bullet][0]):
                self.myObjManger.dictObject[bullet].MoveUpdate(deltaTime,
                    self.myObjManger.dictObject[self.dictBulletindex[bullet][0]].tulPos)
            else:
                self.myObjManger.dictObject[bullet].bBomb = True


    def RemoveBullet(self):

        key = -1
        
        for bullet in self.dictBulletindex:
            if self.myObjManger.dictObject[bullet].bBomb == True:
                if self.myObjManger.HaveKey(self.dictBulletindex[bullet][0]):
                    self.myObjManger.dictObject[(self.dictBulletindex[bullet][0]
                        )].nHP -= (self.myObjManger.dictObject[
                        self.dictBulletindex[bullet][1]].nAttackPoint)
                key = bullet
                break

        if self.dictBulletindex.has_key(key):
            self.dictBulletindex.pop(key)
            self.myObjManger.DeleteObjectNode(key)


    def RemoveMonster(self):

        key = -1

        for monster in self.listMonsterIndex:
            if self.myObjManger.dictObject[monster].nHP <=0:
                key = monster
                break

            if self.myObjManger.dictObject[monster].bSuicideAttack == True:
                key = monster
                self.nLife -= 1
                
                ## demolish one building
                for building in self.listBuildingIndex:
                    self.listBuildingIndex.remove(building)
                    self.myObjManger.DeleteObjectNode(building)
                    break
                    

        if key != -1:
            self.listMonsterIndex.remove(key)
            self.myObjManger.DeleteObjectNode(key)
                



















