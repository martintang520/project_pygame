import pygame
from pygame.locals import*
from CStage import *
from CButton import *
from CObjectManager import *

class CStageStart(CStage):
    
    def __init__(self, surface):
        self.surface = surface
        self.myObjManger = CObjectManager()

        self.GameInit()


    def GameInit(self):
        self.indStart = self.myObjManger.CreateButtonNode((0, 0, 0), (330, 240),
                                            (300,90), "picture/butStart1.png")
        self.nSetIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (330, 360),
                                            (300,90), "picture/butSet1.png")
        self.nExitIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (330, 480),
                                            (300,90), "picture/butExit1.png")
        
        
    def Update(self, deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        

    def Render(self, deltaTime):
        
        self.surface.fill(pygame.color.THECOLORS["blue"])
        self.myObjManger.RenderList(deltaTime, self.surface)
        

    def MouseButtonDown(self,event):
        self.ButtonDecision(event)

        
    def ButtonDecision(self,event):
        butStart = self.myObjManger.GetObject(self.indStart)
        butSet = self.myObjManger.GetObject(self.nSetIndex)
        butExit = self.myObjManger.GetObject(self.nExitIndex)

        if event.pos[0]>butStart.GetPosition()[0] and event.pos[0]<(butStart.GetPosition()[0]+butStart.GetSize()[0])and event.pos[1]>butStart.GetPosition()[1] and event.pos[1]<(butStart.GetPosition()[1]+butStart.GetSize()[1]):
            CStage.SetStage(2)
        elif event.pos[0]>butSet.GetPosition()[0] and event.pos[0]<(butSet.GetPosition()[0]+butSet.GetSize()[0])and event.pos[1]>butSet.GetPosition()[1] and event.pos[1]<(butSet.GetPosition()[1]+butSet.GetSize()[1]):
            CStage.SetStage(3)
        elif event.pos[0]>butExit.GetPosition()[0] and event.pos[0]<(butExit.GetPosition()[0]+butExit.GetSize()[0])and event.pos[1]>butExit.GetPosition()[1] and event.pos[1]<(butExit.GetPosition()[1]+butExit.GetSize()[1]):
            CStage.SetStage(4)

    def MouseMotion(self,event):
        pass
