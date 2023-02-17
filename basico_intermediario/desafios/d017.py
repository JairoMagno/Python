#Algorítimo que abre e reproduz um áudio mp3:

import vlc
import time

media = vlc.MediaPlayer("tnbhd.mp3")
media.play()
time.sleep(174) #media.stop()
