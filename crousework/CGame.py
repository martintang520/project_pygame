import pygame
from pygame.locals import*
from CStageStart import *
from CStageGame import *
from CStageSet import *
from CStageIntro import *
from CMusic import *

class CGame():
    nState = 1  ##Finite State Machine
    myCStage = CStage()  ## Game stage
    
    def __init__(self, nFps, surface):

        self.fTime = 0
        self.nFrames = 0
        self.surface = surface   ## get screen
        self.font = pygame.font.SysFont("Arial",20)  ## Font
        
        if nFps > 0:
            self.nFixedDeltaTime = 1000 / nFps  ## fix maximum frame
        else:
            self.nFixedDeltaTime = 0
        self.fRecordClock = pygame.time.get_ticks() ## record current time

        self.GameInit()

            

    def Update(self):

        fDeltaTime = 0.
        while True:
            fDeltaTime = pygame.time.get_ticks() - self.fRecordClock
            if fDeltaTime > 1: ## ensuring deltaTime at least have one millisecond
                break

        if fDeltaTime > self.nFixedDeltaTime:  ## next frame
            self.fRecordClock = pygame.time.get_ticks()

            fMyDeltaTime = fDeltaTime / 1000. ## real time between two frames
            self.GameUpdate(fMyDeltaTime) ## update all object
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
            self.MouseUpdate() #update the mouse Cursor

    #update the mouse Cursor
    def MouseUpdate(self):
        UrlMouseImage = 'picture/mouse.gif'
        MouseCursor = pygame.image.load(UrlMouseImage).convert_alpha()
        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        x -= MouseCursor.get_width() / 2-12
        y -= MouseCursor.get_height() / 2-13
        self.surface.blit(MouseCursor, (x, y))

    def GameInit(self):
        self.MusicInit()
        CGame.myCStage = CStageStart(self.surface)
        
    def MusicInit(self):
        self.musicVoice = music("2.mp3")
        self.soundVoice = []
        self.soundVoice = self.soundVoice + [sound("1.wav")]
        self.soundVoice = self.soundVoice + [sound("2.wav")]
        self.soundVoice = self.soundVoice + [sound("3.wav")]
        self.musicVoice.play(0)

    def GameUpdate(self, deltaTime):
        self.ChangeState(); ## check and change stage
        
        self.surface.fill((0,0,0,))
        CGame.myCStage.Update(deltaTime)


    def Render(self, deltaTime):
        CGame.myCStage.Render(deltaTime)
        pass


    def EventListener(self, event):
        ##mouse down event
        if event.type == MOUSEBUTTONDOWN:
            CGame.myCStage.MouseButtonDown(event)
        ##mouse move event
        elif event.type == MOUSEMOTION:
            CGame.myCStage.MouseMotion(event)
        ##key down event
        elif event.type == KEYDOWN:
            pass

    ## change stage
    def ChangeState(self):
        
        if CGame.myCStage.GetStageState() != CGame.nState:
            CGame.nState = CGame.myCStage.GetStageState()
            if CGame.nState == 1:
                CGame.myCStage = CStageStart(self.surface)
            elif CGame.nState == 2:
                CGame.myCStage = CStageGame(self.surface,self.soundVoice)
            elif CGame.nState == 3:
                CGame.myCStage = CStageSet(self.surface,self.musicVoice,self.soundVoice)
            elif CGame.nState == 5:
                CGame.myCStage = CStageIntro(self.surface)
