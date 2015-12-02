import pygame
from pygame.locals import*
from CStage import *
from CButton import *
from CObjectManager import *

class CStageIntro(CStage):
    
    #Stageinit#
    def __init__(self, surface):
        self.surface = surface
        self.myObjManger = CObjectManager()

        self.GameInit()


    def GameInit(self):
        #Load Instruction Picture#
        self.nIntroIndex = self.myObjManger.CreateObjectNode((0, 0, 0), (0,0),
                                            (960,640), "picture/instruction.png")

        #Load Ok Button#
        self.nOKIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (800, 500),
                                            (100,100), "picture/OKButton1.png")

        self.Intro = self.myObjManger.GetObject(self.nIntroIndex)
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
            CStage.SetStage(1) #return to start stage#
            
    def MouseMotion(self, event):
        self.MotionDecision(event)

    #Button Change piscture#
    def MotionDecision(self,event):
        if self.butOK.OnButton(event):
            self.butOK.SetImage("picture/OKButton2.png")
        else :
            self.butOK.SetImage("picture/OKButton1.png")
