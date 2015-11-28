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

        self.GameInit()
        self.MusicInit()
        
    def GameInit(self):
        
        self.nMapNumber = 0
        self.listMap = self.myGameMap.listMapGroup[self.nMapNumber]
        self.myObjManger.CreateObjectNode((0, 0, 0), (0, 0),
                    self.surface.get_size(), "picture/background.png")
        self.DrawMap();

        ##test
        MonsterTest = StuProperty(1, 20, 5, "picture/monster1.png")
        self.myObjManger.CreateMonsterNode((0, 0, 0), (0, 0),
                          self.surface.get_size(), MonsterTest)

    def MusicInit(self):
        self.Sound = sound
        self.boolSound = self.Sound.soundState()
        self.Sound.play(1)
        self.nGamePagelevel=0
    
    def Update(self,deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        

    def Render(self, deltaTime):
        self.myObjManger.RenderList(deltaTime, self.surface)
        

    def MouseButtonDown(self,event):

        clickPoint =  (event.pos[0] // 64, event.pos[1] // 64)
        if self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
            self.Bulid(event)
        elif self.myGameMap.IsTower(self.nMapNumber, clickPoint):
            self.Upgrade()


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

    def Bulid(self,event):
        if self.nGamePagelevel==0:
            self.nBuild1 = self.myObjManger.CreateButtonNode((0, 0, 0), (self.nVolumn+382, 190),
                                            (20,40), "picture/volumnButton.png")            
        pass

    def Upgrade(self):
        pass





        
