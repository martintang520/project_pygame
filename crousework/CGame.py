import pygame
from pygame.locals import*
##from ball import *
from CStageStart import *
from CStageGame import *
from CStageSet import *

class CGame():
    nState = 1  ##Finite State Machine
    myCStage = CStage()  ## Game stage
    
    def __init__(self, nFps, surface):

        self.fTime = 0
        self.nFrames = 0
        self.surface = surface   ## get screen
        self.font = pygame.font.SysFont("Arial",20)  ## Font
        
        if nFps > 0:
            self.nFixedDeltaTime = 1000 / nFps
        else:
            self.nFixedDeltaTime = 0
        self.fRecordClock = pygame.time.get_ticks()

        self.GameInit()

            

    def Update(self):

        fDeltaTime = 0.
        while True:
            fDeltaTime = pygame.time.get_ticks() - self.fRecordClock
            if fDeltaTime > 1:
                break

        if fDeltaTime > self.nFixedDeltaTime:  ## next frame
            self.fRecordClock = pygame.time.get_ticks()

            fMyDeltaTime = fDeltaTime / 1000. ## real time between two frames
            self.GameUpdate(fMyDeltaTime)
            self.Render(fMyDeltaTime) ## render all object
            self.fTime += fMyDeltaTime

            if self.fTime > 1:  ## one secend
                self.fTime = 0
                self.nFrames = 0
            self.nFrames += 1

            if self.fTime > 0:
                nFps = self.nFrames / self.fTime  ## frames in the game
                self.surface.blit(self.font.render("FPS : {} ".format(int(nFps)),1,
                                               pygame.color.THECOLORS["white"]),(0,0))


    def GameInit(self):
        CGame.myCStage = CStageStart(self.surface)
        

    def GameUpdate(self, deltaTime):
        self.ChangeState(); ## check and change stage
        
        self.surface.fill((0,0,0,))
        CGame.myCStage.Update(deltaTime)


    def Render(self, deltaTime):
        CGame.myCStage.Render(deltaTime)
        pass


    def EventListener(self, event):
        if event.type == MOUSEBUTTONDOWN:
            CGame.myCStage.MouseButtonDown(event)
            print "click"
        elif event.type == MOUSEMOTION:
            CGame.myCStage.MouseMotion(event)
            pass
        elif event.type == KEYDOWN:
            print "key"

    def ChangeState(self):
        
        if CGame.myCStage.GetStageState() != CGame.nState:
            CGame.nState = CGame.myCStage.GetStageState()
            if CGame.nState == 1:
                CGame.myCStage = CStageStart(self.surface)
            elif CGame.nState == 2:
                CGame.myCStage = CStageGame(self.surface)
            elif CGame.nState == 3:
                CGame.myCStage = CStageSet(self.surface)

    ##@staticmethod
    ##def SetState(state):
##        nState = state
