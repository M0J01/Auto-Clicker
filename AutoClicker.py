#!/usr/bin/python2
# This is the Raspi version

from pymouse import PyMouse
import time
import math

m = PyMouse()

def click(x,y):
	m.click(x,y,1)

def reloadPage():
        click(470,115)

def acceptMatch():
        click(400,770)

def Like():
        click(400, 920)


delay = 1
seconds = 60
minutes = 60
numHours = 10

totalTime = numHours*minutes*seconds
numLikes = totalTime/delay

for i in range(int(round(numLikes))):
    time.sleep(delay)

    if i %250 == 0 :
            reloadPage()
    elif i % 50 == 0:
            acceptMatch()
    else:
            Like()
