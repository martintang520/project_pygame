import pygame
from pygame.locals import*

class CStage():
    nStage = 1  ##Finite State Machine
    
    def __init__(self):
        pass

    def MouseButtonDown(self, event):
        pass

    def MouseMotion(self):
        pass

    def KeyDown(self):
        pass

    @staticmethod
    def SetStage(state):
        CStage.nStage = state
        print CStage.nStage

    @staticmethod
    def GetStageState():
        return CStage.nStage
