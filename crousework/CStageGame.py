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

        self.boolIsBuild = True

        self.Index = {}
        self.Tower = {}

        self.currentIndex=[]
        self.currentTower=[]

        #self.Position=[]
        self.typeUpgrade =[(1,4),(2,5),(3,6),(4,7),(5,8),(6,9),(7,7),(8,8),(9,9)]

        self.GameInit()
        self.MusicInit(sound)
        
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
        self.listCreatMonster = [(0, 5, 5), (0, 3, 3), (1, 3, 5), (0, 0, 0)]
        self.dictMonsterType = {0:StuProperty(1, 20, 1.5, "picture/monster1.png",
                                            (0,1), self.listMap),
                                1:StuProperty(2, 20, 1., "picture/monster2.png",
                                            (0,1), self.listMap)}
        
        self.MonsterIndex = self.myObjManger.CreateMonsterNode((0, 0, 0), (0, 64),
                          self.surface.get_size(), self.dictMonsterType[0])

        ## attack 
        self.listBulletindex = []


    def MusicInit(self, sound):
        self.Sound = sound
        self.boolSound = self.Sound.soundState()
        self.Sound.play(1)
        
    def Update(self,deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        self.MonsterCreater(deltaTime)
        self.detection(deltaTime)
        

    def Render(self, deltaTime):
        self.myObjManger.RenderList(deltaTime, self.surface)
        

    def MouseButtonDown(self,event):

        clickPoint =  (event.pos[0] // 64, event.pos[1] // 64)
        
        if self.boolIsBuild:
            self.boolIsBuild = False
            self.tulCurrentPoint = self.GetPoint(event.pos)
            
            if self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
                self.Build(event)
            elif self.myGameMap.IsTower(self.nMapNumber, clickPoint):
                self.Upgrade(event)
        else:
            self.boolIsBuild = True
            self.unBuild()
            if self.myGameMap.IsBlank(self.nMapNumber, self.tulCurrentPoint):
                if self.BuildDecision(event,self.currentTower) !=-1:
                    self.myGameMap.BuildTower(self.nMapNumber, self.tulCurrentPoint)
                    self.AddIndex(self.myObjManger.CreateTowerNode((0, 0, 0),
                                                                   (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),
                                                                   (64,64), "picture/tower"+str(self.BuildDecision(event,self.currentTower)+1)+".png",128),
                                 self.BuildDecision(event,self.currentTower)+1,self.tulCurrentPoint)
                self.DeleteIndex()
                    
            elif self.myGameMap.IsTower(self.nMapNumber, self.tulCurrentPoint):
                if self.UpgradeDecision(event,self.currentTower)!=-1:
                    if self.UpgradeDecision(event,self.currentTower)==1:
                        self.deleteBuild(self.Index[self.tulCurrentPoint])
                        self.myGameMap.DeleteTower(self.nMapNumber, self.tulCurrentPoint)
                        self.myObjManger.CreateTowerNode((0, 0, 0), (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),(64,64),
                                                           "picture/blank.png",128)
                    elif self.UpgradeDecision(event,self.currentTower)==2:
                        self.deleteBuild(self.Index[self.tulCurrentPoint])
                        self.AddIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),(64,64),
                                                                        "picture/tower"+str(self.typeUpgrade[self.Tower[self.tulCurrentPoint]-1][1])+".png",128),
                                      self.typeUpgrade[self.Tower[self.tulCurrentPoint]-1][1],self.tulCurrentPoint)
  
                self.DeleteIndex()

    def DrawMap(self):
        categoryPicture = {
            1 : "picture/path.png",
            2 : "picture/tree.png",
            3 : "picture/house.png",
            4 : "picture/blank.png",
            5 : "picture/path.png"}
        
        for x in range(0, 15):
            for y in range(0, 10):
                if self.listMap[y][x] != 0:
                    self.myObjManger.CreateObjectNode((0, 0, 0), (x * 64, y * 64),
                                 (64, 64), categoryPicture[self.listMap[y][x]])
    ##create monster in update
    def MonsterCreater(self, deltaTime):
        if self.listCreatMonster[self.nOrder][2] == 0:
            return
            
        
        if self.nMonsterNumber < self.listCreatMonster[self.nOrder][1]:
            if self.fGap >= 1.5:
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



    ##build tower
    def Build(self,event):

        ntower1 = self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower1.png",128)
        ntower2 = self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower2.png",128)
        ntower3 = self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+128,self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower3.png",128)
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
                                                           (64,64), "picture/cross.png",128))
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),(64,64),
                                                           "picture/tower"+str(self.typeUpgrade[self.Tower[self.tulCurrentPoint]-1][1])+".png",128))          


    ## for build or upgrade
    def AddNewIndex(self,index):

        self.currentIndex = self.currentIndex + [index]

        self.currentTower = self.currentTower + [self.myObjManger.GetObject(index)]
    
    def DeleteIndex(self):
        self.currentIndex = []
        self.currentTower = []

    ##get the box's left and top

    def GetPoint(self,position):
        return (position[0] // 64,position[1] // 64)
    
    def GetPointLeft(self,position):
        tulLeft = self.GetPoint(position)[0] * 64
        return tulLeft

    
    def GetPointTop(self,position):
        tulTop = self.GetPoint(position)[1] * 64
        return tulTop


    ## after build or upgrade 
    def AddIndex(self,index,buildtype,position):
        self.Index[position] = index
        self.Tower[position] = buildtype


    def UpgradeDecision(self,event,tower):
        if tower[0].OnButton(event) :
            return 1
        elif tower[1].OnButton(event):
            return 2
        return -1


    #Each town detects all of the monsters
    def detection(self,deltaTime):

        for k in self.Index:
            for j in self.listMonsterIndex:
                oTowner = self.myObjManger.dictObject[self.Index[k]]
                oMonster =self.myObjManger.dictObject[j]
                
                attackTime = oTowner.attacktimer
                if ((oMonster.tulPos[0] - oTowner.tulPos[0]) ** 2 +
                         (oMonster.tulPos[1] - oTowner.tulPos[1]) ** 2 <= oTowner.rangeTower ** 2 
                          and attackTime > 2):
                    self.myObjManger.dictObject[self.Index[k]].attacktimer = 0
                    self.bulletattack(self.Index[k], j)

    def bulletattack(self, towerIndex, monsterIndex):

        newBullet = self.myObjManger.CreateBulletNode((0, 0, 0),
            self.myObjManger.dictObject[towerIndex].tulPos, (64, 64), "picture/cross.png")
        self.listBulletindex.append(newBullet)
        self.myObjManger.dictObject[monsterIndex].nHP -= 5
        pass























