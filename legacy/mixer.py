#!/usr/bin/env python3
#
# Title:      Sound playback for Raspberry Pi
# Author:     Martin Brenner
#
# Hardware: using USB audio
# in ~/.asoundrc:
# pcm.!default {
# 	type hw
# 	card 1
# }
# ctl.!default {
# 	type hw
# 	card 1
# }

import pygame
import time
import sys

class tsound:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        # Ensure this path is correct or configurable
        self.sounddir = "/home/pi/projects/ingress118apk/assets/sounds/"


    def deploy(self):
        try:
            sound = pygame.mixer.Sound(self.sounddir + "sfx_resonator_power_up.ogg")
            sound.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def main(self):
        try:  
            self.deploy()
            time.sleep(2)
        except KeyboardInterrupt:
            # self.cls(self.ledpixels) # cls not defined here, removing or commenting out
            sys.exit(0)

if __name__ =='__main__':
        audio = tsound()
        audio.main()



