#!/usr/bin/env python2

#global
import os
import time
from subprocess import Popen

# local
import screen
import zonedata


globalvol = 25
pipefile = '/tmp/mplayer_pipe'
currentzone = 'Menu'


def loadenv():
    os.mkfifo(pipefile)
    Popen([
        'mplayer',
        '-vo', 'null', '-ao', 'alsa',
        '-volume', '0', '-loop', '0',
    ])

def loadsong(songfile):
    with open(pipefile, 'w') as fp:
        for x in range(globalvol):
            fp.write('volume -1\n')
            time.sleep(1.5/globalvol)
        fp.write('volume %d 1\n' % globalvol)
        fp.write('loadfile \"%s\"\n' % songfile)

def grabscreen():
    pixel_list = screen.get_pixeldata(os.getenv('DISPLAY'), '875621')
    if not pixel_list:
        Popen(['xte','\'key Tab\''])
        pixel_list = screen.get_pixeldata(os.getenv('DISPLAY'), '875621')
        Popen(['xte','\'key Tab\''])
        if not pixel_list:
            return None
    return pixel_list

def pixelmatch():
    match = True
    pixels = grabscreen()
    
    for zone in zonedata.zonelist:
        for idx in range(len(pixels)):
            if pixels[idx] == zonedata.zones[zone]['pixels'][idx]:
                match *= True
            else:
                match *= False
                break
        if match:
            print("You're in %s. GOTCHA!" % zone)
            break


if __name__ == '__main__':
    pixelmatch()
