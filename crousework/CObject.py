import pygame
from pygame.locals import*


class CObject(pygame.sprite.Sprite):
    def __init__(self, color, initialPos, size, pictureName):
        pygame.sprite.Sprite.__init__(self) ## call superclass function

        self.image = pygame.image.load(pictureName).convert_alpha() ## load picture       
        
        self.tulSize = size  ## size of the picture
        self.tulPos = initialPos  ## psition in the screen

    def Update(self, deltaTime):
        pass

    def Render(self, deltaTime, surface):
        surface.blit(self.image, self.tulPos)
        pass

    ## change picture
    def SetImage(self, pictureName):
        self.image = pygame.image.load(pictureName).convert_alpha()


    def SetPosition(self,pos):
        self.tulPos = pos

