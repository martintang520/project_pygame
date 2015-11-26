import pygame
from pygame.locals import*
from CStage import *

class CStageGame(CStage):
    
    def __init__(self, surface):
        self.surface = surface

    def Update(self,deltaTime):
        print CStage.nStage + 0

    def Render(self, deltaTime):
        pass
