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

        self.boolIsBuild=True

        self.currentBuild = []
        self.currentIndex = []

        self.Index = {}
        self.Tower = {}

        
        #self.Position=[]
        self.typeUpgrade =[(1,4),(2,5),(3,6),(4,7),(5,8),(6,9)]

        self.tulCurrentPoint=(1,1)

        self.GameInit()
        self.MusicInit(sound)
        
    def GameInit(self):
        
        self.nMapNumber = 0
        self.listMap = self.myGameMap.listMapGroup[self.nMapNumber]
        self.myObjManger.CreateObjectNode((0, 0, 0), (0, 0),
                    self.surface.get_size(), "picture/background.png")
        self.DrawMap();

        ##test
        MonsterTest = StuProperty(1, 20, 1, "picture/monster.png", (0,1), self.listMap)
        self.MonsterIndex = self.myObjManger.CreateMonsterNode((0, 0, 0), (0, 64),
                          self.surface.get_size(), MonsterTest)

    def MusicInit(self, sound):
        self.Sound = sound
        self.boolSound = self.Sound.soundState()
        self.Sound.play(1)
        
    def Update(self,deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        

    def Render(self, deltaTime):
        self.myObjManger.RenderList(deltaTime, self.surface)
        

    def MouseButtonDown(self,event):

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
            print self.myGameMap.IsBlank(self.nMapNumber, clickPoint)
            if self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
                if self.BuildDecision(event,self.currentBuild)[1] !=-1:
                    self.myGameMap.BuildTower(self.nMapNumber, self.tulCurrentPoint)
                    self.AddIndex(self.myObjManger.CreateTowerNode((0, 0, 0),
                                                               (self.tulCurrentPoint[0]*64,self.tulCurrentPoint[1]*64),
                                                               (64,64), "picture/tower"+str(self.BuildDecision(event,self.currentBuild)[1]+1)+".png"),
                             self.BuildDecision(event,self.currentBuild)[1]+1,self.tulCurrentPoint)
            elif self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
                print 'upgrade'
                pass
            self.DeleteIndex()
        print self.tulCurrentPoint

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

    ##build tower
    def Build(self,event):

        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower1.png"))
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),
                                                                       (64,64), "picture/tower2.png"))


    def BuildDecision(self, event, build):
        for n in range(len(build)):
            if build[n].OnButton(event) :
                print n
                return (build[n],n)
        return('',-1)

    def unBuild(self):
        for n in self.currentIndex:
            self.myObjManger.DeleteObjectNode(n)
            
    def deleteBuild(self,index):
        self.myObjManger.DeleteObjectNode(index)

    ##update tower
    def Upgrade(self,event):
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos),self.GetPointTop(event.pos)),
                                                           (64,64), "picture/cross.png"))
        self.AddNewIndex(self.myObjManger.CreateTowerNode((0, 0, 0), (self.GetPointLeft(event.pos)+64,self.GetPointTop(event.pos)),(64,64),
                                                           "picture/tower"+str(self.typeUpgrade[self.Tower[self.tulCurrentPoint]-1][1])+".png"))


        #find the type of upgrade tower
        #self.typeUpgrade[typeBuild[self.GetPoint(event.pos)[0]][self.GetPoint(event.pos)[1]]][1]

    ## for build or upgrade
    def AddNewIndex(self,index):
        self.currentIndex = self.currentIndex + [index]
        self.currentBuild = self.currentBuild + [self.myObjManger.GetObject(index)]
        
    
    def DeleteIndex(self):
        self.currentIndex=[]
        self.currentBuild=[]

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
        self.Index[position]=index
        self.Tower[position]=buildtype
        print self.Index
        print self.Tower



    def UpgradeDecision(self,event):
        pass






















