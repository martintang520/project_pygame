import pygame
from pygame.locals import*
from CStage import *
from CButton import *
from CObjectManager import *

class CStageSet(CStage):

    def __init__(self, surface):
        self.surface = surface
        self.myObjManger = CObjectManager()

        self.GameInit()


    def GameInit(self):

        self.nVolumn=0
        self.boolMusic=True
        
        self.nVolumnIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (360, 180),
                                            (460,60), "picture/volumn.png")
        self.nVolumnPointIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (100*self.nVolumn+382, 190),
                                            (20,40), "picture/volumnButton.png")

        self.nSoundOpenIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (360, 360),
                                            (105,100), "picture/musicOpen2.png")
        self.nSoundCloseIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (500, 360),
                                            (105,100), "picture/musicClose1.png")

        self.nOKIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (800, 500),
                                            (100,100), "picture/OKButton1.png")

        self.nText1Index = self.myObjManger.CreateButtonNode((0, 0, 0), (90, 180),
                                            (200,60), "picture/TEXT1.png")
        self.nText2Index = self.myObjManger.CreateButtonNode((0, 0, 0), (90, 380),
                                            (200,60), "picture/TEXT2.png")
        self.nTextSoundIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (630, 360),
                                            (200,100), "picture/TEXT3.png")        
        
        self.butVolumn = self.myObjManger.GetObject(self.nVolumnIndex)
        self.butVolumnPoint = self.myObjManger.GetObject(self.nVolumnPointIndex)
        
        self.butSoundOpen = self.myObjManger.GetObject(self.nSoundOpenIndex)
        self.butSoundClose = self.myObjManger.GetObject(self.nSoundCloseIndex)

        self.butOK = self.myObjManger.GetObject(self.nOKIndex)

        self.imageTEXT1 = self.myObjManger.GetObject(self.nText1Index)
        self.imageTEXT2 = self.myObjManger.GetObject(self.nText2Index)

        self.imageTEXTSound = self.myObjManger.GetObject(self.nTextSoundIndex)
        
    def Update(self,deltaTime):
        self.myObjManger.UpdateList(deltaTime)

    def Render(self, deltaTime):

        self.surface.fill((82,180,255))
        self.myObjManger.RenderList(deltaTime, self.surface)

    def MouseButtonDown(self,event):
        self.VolumnDecision(event)
        self.SoundDecision(event)
        self.OkDecision(event)


## Ok Button
    def OkDecision(self,event):
        if self.butOK.OnButton(event):
            CStage.SetStage(1)
            
## open or close music
    def SoundDecision(self,event):
        
        if self.butSoundOpen.OnButton(event):
            
            self.butSoundOpen.SetImage("picture/musicOpen2.png")
            self.butSoundClose.SetImage("picture/musicClose1.png")
            self.imageTEXTSound.SetImage("picture/TEXT3.png")
            self.boolMusic=True
        elif self.butSoundClose.OnButton(event):
            
            self.butSoundOpen.SetImage("picture/musicOpen1.png")
            self.butSoundClose.SetImage("picture/musicClose2.png")
            self.imageTEXTSound.SetImage("picture/TEXT4.png")
            self.boolMusic=False

##turn up or down the Volumn of music
    def VolumnDecision(self,event):

        if self.butVolumn.OnButton(event):
            self.nVolumn = (event.pos[0]-378)/4
            if self.nVolumn<1:
                self.butVolumnPoint.SetPosition((382,self.butVolumnPoint.GetPosition()[1]))
                self.nVolumn=1
            elif self.nVolumn>100:
                self.butVolumnPoint.SetPosition((778,self.butVolumnPoint.GetPosition()[1]))
                self.nVolumn=100
            else:
                self.butVolumnPoint.SetPosition((event.pos[0],self.butVolumnPoint.GetPosition()[1]))
            print self.nVolumn
            
    def MouseMotion(self, event):
        self.MotionDecision(event)
        
    def MotionDecision(self,event):
        if self.butOK.OnButton(event):
            self.butOK.SetImage("picture/OKButton2.png")
        else :
            self.butOK.SetImage("picture/OKButton1.png")

    def GetSoundState(self):
        return self.boolMusic

    def GetVolumn(self):
        return self.nVolumn