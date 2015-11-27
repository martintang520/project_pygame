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
