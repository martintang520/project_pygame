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

        self.GameInit()

    def GameInit(self):
        
        self.nMapNumber = 0
        self.listMap = self.myGameMap.listMapGroup[self.nMapNumber]
        self.myObjManger.CreateObjectNode((0, 0, 0), (0, 0),
                    self.surface.get_size(), "picture/background.png")
        self.DrawMap();

        ##test
        MonsterTest = StuProperty(1, 20, 5)
        self.myObjManger.CreateMonsterNode((0, 0, 0), (0, 0),
                    self.surface.get_size(), "picture/house.png", MonsterTest)

    
    def Update(self,deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        

    def Render(self, deltaTime):
        self.myObjManger.RenderList(deltaTime, self.surface)
        

    def MouseButtonDown(self,event):

        clickPoint =  (event.pos[0] // 64, event.pos[1] // 64)
        if self.myGameMap.IsBlank(self.nMapNumber, clickPoint):
            self.Bulid()
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

    def Bulid(self):
        pass

    def Upgrade(self):
        pass





        
