# This is the Raspi version

from pymouse import PyMouse
import time
import math

m = PyMouse()

def click(x,y):
	m.click(x,y,1)



click(1600,750)

delay = 10
seconds = 60
minutes = 60

numHours = .5

totalTime = numHours*minutes*seconds
numLikes = totalTime/delay

for i in range(int(round(numLikes))):
    time.sleep(delay)
    click(1600,750)
