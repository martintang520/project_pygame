import pygame
from pygame.locals import*

## abstract class
class CStage():
    nStage = 1  ##Finite State Machine, initial stage
    
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass
        
    def Render(self, deltaTime):
        pass

    def MouseButtonDown(self, event):
        pass

    def MouseMotion(self,event):
        pass

    def KeyDown(self,event):
        pass

    @staticmethod
    def SetStage(state):
        CStage.nStage = state
        print CStage.nStage

    @staticmethod
    def GetStageState():
        return CStage.nStage
