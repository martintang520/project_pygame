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
        self.nStartIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (330, 240),
                                            (300,90), "picture/butStart1.png")
        self.nSetIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (330, 360),
                                            (300,90), "picture/butSet1.png")
        self.nExitIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (330, 480),
                                            (300,90), "picture/butExit1.png")

        self.butStart = self.myObjManger.GetObject(self.nStartIndex)
        self.butSet = self.myObjManger.GetObject(self.nSetIndex)
        self.butExit = self.myObjManger.GetObject(self.nExitIndex)

        
        
    def Update(self, deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        

    def Render(self, deltaTime):
        
        self.surface.fill((82,180,255))
        self.myObjManger.RenderList(deltaTime, self.surface)
        

    def MouseButtonDown(self,event):
        self.ButtonDecision(event)

        
    def ButtonDecision(self,event):
        
        if self.butStart.OnButton(event):
            CStage.SetStage(2)
        elif self.butSet.OnButton(event):
            CStage.SetStage(3)
        elif self.butExit.OnButton(event):
            CStage.SetStage(4)

    def MouseMotion(self,event):
        self.MotionDecision(event)
        
    def MotionDecision(self,event):
        
        if self.butStart.OnButton(event):
            self.butStart.SetImage("picture/butStart2.png")
        else:
            self.butStart.SetImage("picture/butStart1.png")

        if self.butSet.OnButton(event):
            self.butSet.SetImage("picture/butSet2.png")
        else:
            self.butSet.SetImage("picture/butSet1.png")
            
        if self.butExit.OnButton(event):
            self.butExit.SetImage("picture/butExit2.png")
        else:
            self.butExit.SetImage("picture/butExit1.png")
