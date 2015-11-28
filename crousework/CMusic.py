import pygame


class sound:
       def __init__(self,a):
             
              self.a=a
              pygame.mixer.init()
       #0 loop ,n means times#
       def play(self,c):
              b="sound/"+self.a
              channel=pygame.mixer.find_channel()
              self.sound = pygame.mixer.Sound(b)
              if c ==0:
                     self.sound.play(-1,0)
              else:
                     self.sound.play(c-1,0)
       def stop(self):             
              self.sound.stop()
       #c between 0-1#
       def setvolume(self,c):
              c=c/100.0
              self.sound.set_volume(c)


class music:
       def __init__(self,b=""):
              b="music/"+b
              pygame.mixer.init()
              track = pygame.mixer.music.load(b)
              pygame.mixer.music.set_volume(0.5)
              self.State = False
       def play(self,a):
              if a == 0:
                     pygame.mixer.music.play(-1,0.0)
              else:
                     pygame.mixer.music.play(c,0.0)
              self.State = True
              
       def pause(self):
              pygame.mixer.music.pause()
              self.State = False
              
       def stop(self):
              pygame.mixer.music.stop()
              self.State = False
              
       def setvolume(self,c):
              c=c/100.0
              pygame.mixer.music.set_volume(c)

       def musicState(self):
              return self.State



















              
