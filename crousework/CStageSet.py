import pygame
from pygame.locals import*
from CStage import *
from CButton import *
from CObjectManager import *

class CStageSet(CStage):

    def __init__(self, surface,music,sound):
        self.surface = surface
        self.myObjManger = CObjectManager()
        self.musicVoice = music # music
        self.soundVoice = sound # sound

        self.GameInit()


    def GameInit(self):

        self.nVolumn=self.musicVoice.musicVolumn()*4 # number of Volumn 1-100
        self.boolMusic=self.musicVoice.musicState() # music static True or False
        #nVolumn bar
        self.nVolumnIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (360, 180),
                                            (460,60), "picture/volumn.png")
        #nVolumn point
        self.nVolumnPointIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (self.nVolumn+382, 190),
                                            (20,40), "picture/volumnButton.png")

        #ok button return start stage
        self.nOKIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (800, 500),
                                            (100,100), "picture/OKButton1.png")

        self.nText1Index = self.myObjManger.CreateButtonNode((0, 0, 0), (90, 180),
                                            (200,60), "picture/TEXT1.png")
        self.nText2Index = self.myObjManger.CreateButtonNode((0, 0, 0), (90, 380),
                                            (200,60), "picture/TEXT2.png")

        #according music and sound state to change button and volumn bar
        self.SoundStateDecision()
        # instance the button and text image 
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
    #mouse click event
    def MouseButtonDown(self,event):
        self.VolumnDecision(event) # listen the volumn event
        self.SoundDecision(event)#listen the sound event
        self.OkDecision(event)# listen the ok event


    #click Ok Button return to the first page
    def OkDecision(self,event):
        if self.butOK.OnButton(event):
            CStage.SetStage(1)
            
    #opened or closeed music. if the music and sound is opened, show the open button same with closed
    def SoundStateDecision(self):
        if self.boolMusic:
            self.nSoundOpenIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (360, 360),
                                                (105,100), "picture/musicOpen2.png")
            self.nSoundCloseIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (500, 360),
                                                (105,100), "picture/musicClose1.png")
            self.nTextSoundIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (630, 360),
                                                (200,100), "picture/TEXT3.png")
        else:
            self.nSoundOpenIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (360, 360),
                                                (105,100), "picture/musicOpen1.png")
            self.nSoundCloseIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (500, 360),
                                                (105,100), "picture/musicClose2.png")
            self.nTextSoundIndex = self.myObjManger.CreateButtonNode((0, 0, 0), (630, 360),
                                                (200,100), "picture/TEXT4.png")
    #open or close music
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
        self.Play()

    # according to self.boolMusic variable, the music will be played or pauseed
    # the sound can be stoped and begined
    def Play(self):
        if self.boolMusic:
            self.musicVoice.play(0)
            self.soundVoice[0].State = True
            self.soundVoice[1].State = True
            self.soundVoice[2].State = True
        else:
            self.musicVoice.pause()
            self.soundVoice[0].State = False
            self.soundVoice[1].State = False
            self.soundVoice[2].State = False

##turn up or down the Volumn of music and sound
#event.pos[0] get the x value of the click, 378 is the position of the volumn bar
#778 = 378 + 400, 400 is weight of volumn bar  
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
        self.Volume()
## according to the position to change the volumn of music and sound
    def Volume(self):
        self.musicVoice.setvolumn(self.nVolumn)
        self.soundVoice[0].setvolumn(self.nVolumn)
        self.soundVoice[1].setvolumn(self.nVolumn)
        self.soundVoice[2].setvolumn(self.nVolumn)

#listen the event of mouse movement 
    def MouseMotion(self, event):
        self.MotionDecision(event)
#butOK.OnButton is to judge wheather the mouse on the button
# the pictur can change by the resule
    def MotionDecision(self,event):
        if self.butOK.OnButton(event):
            self.butOK.SetImage("picture/OKButton2.png")
        else :
            self.butOK.SetImage("picture/OKButton1.png")
#return sound and music state
    def GetSoundState(self):
        return self.boolMusic
#return sound and music state
    def GetVolumn(self):
        return self.nVolumn
