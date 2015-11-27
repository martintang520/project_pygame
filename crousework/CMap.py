import pygame
from pygame.locals import *

class CMap():

    listMapGroup = []
    
    def __init__(self):
        self.InitMap()
        pass

    def InitMap(self):
        CMap.listMapGroup += [[[0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 2],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                               [2, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 1, 0, 2],
                               [2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 4, 2],
                               [2, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 2],
                               [2, 4, 1, 0, 3, 3, 3, 3, 3, 3, 3, 0, 1, 4, 2],
                               [2, 0, 1, 0, 3, 3, 3, 3, 3, 3, 3, 0, 1, 0, 2],
                               [2, 4, 1, 0, 0, 4, 0, 0, 0, 4, 0, 0, 1, 4, 2],
                               [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                               [2, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 2]]]


    def IsBlank(self, mapNumber, index):
        
        nodeType = CMap.listMapGroup[mapNumber][index[1]][index[0]]
        if nodeType == 4:
            return True
        else:
            return False


    def IsTower(self, mapNumber, index):
        
        nodeType = CMap.listMapGroup[mapNumber][index[1]][index[0]]
        if nodeType == 6:
            return True
        else:
            return False
