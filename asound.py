'''
Created on 12/30/23

@author: saul

play some music...

'''

# import vlc
from playsound import playsound

class music:
    songfile = "./asi.mp3"

    def __init__(self):
         print("playing file: ")
         print(self.songfile)
         playsound(self.songfile)
         # p = vlc.MediaPlayer(self.songfile)
         # p.play()



if __name__ == '__main__':
    h = music()
