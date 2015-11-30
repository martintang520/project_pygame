import pygame
from pygame.locals import*

class CStage():
    nStage = 2  ##Finite State Machine
    
    def __init__(self):
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
