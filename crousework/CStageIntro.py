import pygame
from pygame.locals import*
from CStage import *
from CButton import *
from CObjectManager import *

class CStageIntro(CStage):
    
    def __init__(self, surface):
        self.surface = surface
        self.myObjManger = CObjectManager()

        self.GameInit()


    def GameInit(self):
        self.nOKIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (800, 500),
                                            (100,100), "picture/OKButton1.png")

        self.butOK = self.myObjManger.GetObject(self.nOKIndex)

        
    def Update(self, deltaTime):
        self.myObjManger.UpdateList(deltaTime)
        

    def Render(self, deltaTime):
        
        self.surface.fill((82,180,255))
        self.myObjManger.RenderList(deltaTime, self.surface)

    def MouseButtonDown(self,event):
        self.OkDecision(event)

    def OkDecision(self,event):
        if self.butOK.OnButton(event):
            CStage.SetStage(1)
            
    def MouseMotion(self, event):
        self.MotionDecision(event)

    def MotionDecision(self,event):
        if self.butOK.OnButton(event):
            self.butOK.SetImage("picture/OKButton2.png")
        else :
            self.butOK.SetImage("picture/OKButton1.png")
