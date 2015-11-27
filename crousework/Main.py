import pygame
from ball import *
from CGame import *
SIZE = (960,640)

pygame.init()
surface = pygame.display.set_mode(SIZE)
pygame.display.flip()

gGame = CGame(50, surface)

while True :
    gGame.Update()
    pygame.display.update()
    
    event = pygame.event.poll()
    gGame.EventListener(event)
    if event.type == pygame.QUIT or CGame.myCStage.GetStageState()==4:
        break
    
pygame.quit()
