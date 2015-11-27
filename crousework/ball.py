import pygame
from pygame.locals import*


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ic_launcher.png").convert_alpha()
        self.rect = self.image.fill(color, None, BLEND_ADD)
        self.rect.topleft = initial_position

        self.x = 0.
        self.speed = 100
        self.contro = 0
        


    def Update(self, deltaTime, surface):
        distance_moved = deltaTime * self.speed
        self.x += distance_moved
        surface.blit(self.image, (self.rect.x, (self.rect.y +
                                                               self.x)))
        pass
