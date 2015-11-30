import pygame
from pygame.locals import *
from CXmladapter import *

class CMap():

    listMapGroup = []
    
    def __init__(self):
        self.XMLreader = CXmladapter('map.xml','map')
        self.InitMap()
        pass

    def InitMap(self):
        CMap.listMapGroup += [self.XMLreader.Read(0)]


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

    def BuildTower(self, mapNumber, index):
        CMap.listMapGroup[mapNumber][index[1]][index[0]]=6

    def DeleteTower(self, mapNumber, index):
        CMap.listMapGroup[mapNumber][index[1]][index[0]]=4
