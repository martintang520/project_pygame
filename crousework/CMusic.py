import pygame


class sound:
       def __init__(self, strmusicname):
             
              self.strmusicname = strmusicname
              pygame.mixer.init()
              self.State = True
              strsoundname = "sound/"+self.strmusicname #the path of music file#
              channel = pygame.mixer.find_channel()
              self.sound = pygame.mixer.Sound(strsoundname)

       #function play sound,0 means loop play,n means n times#
       def play(self, ntimes):
              if ntimes ==0:
                     self.sound.play(-1, 0)
              else:
                     self.sound.play(ntimes-1, 0)

       #function stop music#
       def stop(self):             
              self.sound.stop()

       #function set play volumn,c between 0-1#
       def setvolumn(self,nvolumn):
              self.nvolumn = nvolumn
              nvolumn=nvolumn / 100.0
              self.sound.set_volume(nvolumn)

       #get sound state true or false#
       def soundState(self):
              return self.State


class music:
       def __init__(self, strmusicname):
              strmusicname = "music/"+strmusicname
              pygame.mixer.init()
              track = pygame.mixer.music.load(strmusicname)
              pygame.mixer.music.set_volume(0.5)
              self.State = False
              self.c=100

       #function play music#
       def play(self, ntimes):
              if ntimes == 0:
                     pygame.mixer.music.play(-1,0.0)
              else:
                     pygame.mixer.music.play(ntimes,0.0)
              self.State = True

       #function music Pause#
       def pause(self):
              pygame.mixer.music.pause()
              self.State = False

       #function music stop#
       def stop(self):
              pygame.mixer.music.stop()
              self.State = False

       #function set music volumn, c beween 0-1#      
       def setvolumn(self, nvolumn):
              self.nvolumn = nvolumn
              nvolumn=nvolumn / 100.0
              pygame.mixer.music.set_volume(nvolumn)

       #return music state#
       def musicState(self):
              return self.State
              
       #return music volumn#
       def musicVolumn(self):
              return self.nvolumn



















              
