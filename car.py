#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from subprocess import *
import time
import web

ioport = [11, 12, 13, 15]
#TAKE_PHOTO = 'streamer -c /dev/video0 -o static/out.jpeg'.split(' ')
TAKE_PHOTO = 'fswebcam -S 2 -d /dev/video0 static/out.jpeg'.split(' ')

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for i in xrange(4):
        GPIO.setup(ioport[i], GPIO.OUT)
        time.sleep(0.1)

urls = (
        '/takephoto', 'TakePhoto', 
        '/speak', 'Speak', 
        '/move', 'Move'
        )

def doMove(s):
    for i in xrange(4):
	GPIO.output(ioport[i], int(s[i]))

class TakePhoto:
    def GET(self):
        call(TAKE_PHOTO)

class Speak:
    def POST(self):
        i = web.input()
        call(['espeak', i.content])

class Move:
    def POST(self):
        i = web.input()
        if i.direction == 'forward':
            doMove('1010')
        elif i.direction == 'back':
            doMove('0101')
        elif i.direction == 'right':
            doMove('0010')
        elif i.direction == 'left':
            doMove('1000')
        else:
            doMove('0000')

if __name__ == '__main__':
    try:
	init()
        app = web.application(urls, globals())
        app.run()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print "All Cleanup!"

