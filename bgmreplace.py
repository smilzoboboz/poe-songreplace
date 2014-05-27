#!/usr/bin/env python2

#global
import os
import sys
import time
from subprocess import Popen

# local
import screen
import zonedata


globalvol = 25
pipefile = '/tmp/mplayer_pipe'
currentzone = 'Menu'

'''
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
'''

def grabscreen():
    pixel_list = screen.get_pixeldata(os.getenv('DISPLAY'), '875621')
    #if not pixel_list:
    #    Popen(['xte','\'key Tab\''])
    #    pixel_list = screen.get_pixeldata(os.getenv('DISPLAY'), '875621')
    #    Popen(['xte','\'key Tab\''])
    #    if not pixel_list:
    #        return None
    return pixel_list

def pixelmatch():
    pixels = grabscreen()
    for zone in zonedata.zonelist:
        for serie in zonedata.zones[zone]['pixels']:
            matchcount = 0
            for idx in range(len(pixels)):
                if pixels[idx] in serie:
                    matchcount += 1
                if idx > 5 and matchcount == 0:
                    break
            if matchcount > len(pixels) * 0.9:
                global currentzone
                print("You're in %s (you were in %s). GOTCHA!" % (zone, currentzone))
                if zone != currentzone:
                    Popen(['bash', 'songreplace.sh',
                           zonedata.zones[zone]['song']])
                    currentzone = zone
                return


if __name__ == '__main__':
    while True:
        pixelmatch()
        time.sleep(2)
