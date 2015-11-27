import pygame
from pygame.locals import*


class CButton(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ic_launcher.png").convert_alpha()
        self.rect = self.image.fill(color, None, BLEND_ADD)
        self.rect.topleft = initial_position

    def Update(self, surface):
        pass

    def Render(self, deltaTime, surface):
        surface.blit(self.image, ((surface.get_width() - self.rect.width) / 2,
                                  self.rect.y))
