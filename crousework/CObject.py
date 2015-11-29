import pygame
from pygame.locals import*


class CObject(pygame.sprite.Sprite):
    def __init__(self, color, initialPos, size, pictureName):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(pictureName).convert_alpha()        
        
        self.tulSize = size
        self.tulPos = initialPos

    def Update(self, deltaTime):
        pass

    def Render(self, deltaTime, surface):
        surface.blit(self.image, self.tulPos)
        pass

    def SetImage(self, pictureName):
        self.image = pygame.image.load(pictureName).convert_alpha()


    def SetPosition(self,pos):
        self.tulPos = pos

    def OnButton(self,event):

        if event.pos[0]>self.tulPos[0] and event.pos[0]<(self.tulPos[0]+self.tulSize[0])and event.pos[1]>self.tulPos[1] and event.pos[1]<(self.tulPos[1]+self.tulSize[1]):
            return True
        else:
            return False
