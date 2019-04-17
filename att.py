# This is the Raspi version

from pymouse import PyMouse
import time
import math

m = PyMouse()

def click(x,y):
	m.click(x,y,1)

x = 470
y = 115

click(x,y)

delay = 3
seconds = 60
minutes = 60

numHours = 5

totalTime = numHours*minutes*seconds
numLikes = totalTime/delay

for i in range(int(round(numLikes))):
    time.sleep(delay)
    click(x,y)
    time.sleep(1)
    #click(x,y-150)
