import pygame
from pygame.locals import*
from CStage import *
from ball import *
from CButton import *

class CStageStart(CStage):
    
    def __init__(self, surface):
        self.surface = surface
        self.ball = Ball((0, 0, 0), (100, 100))
        self.butStart = CButton((0, 0, 0), (500, 100))

    def Update(self, deltaTime):
        print CStage.nStage

    def Render(self, deltaTime):
        self.ball.Update(deltaTime, self.surface)
        self.butStart.Render(deltaTime, self.surface)

    def MouseButtonDown(self,event):
        pass
