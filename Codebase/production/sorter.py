from gpiozero import Servo
import board
import adafruit_tcs34725

from time import sleep
from statistics import mean

from colors import *
from servoControl import *

# initialize sensor and servos
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

doorServo = Servo(14)
pushServo = Servo(15)
vacuumMotor = Servo(25)
val = -1

calibrateMotor()

runSorter = True
chamberColor = -1
setVacuumMotor(True)
sequence = ["blue", "purple", "red", "blue"]
seqIndex = 0
user_input = input("Press any key to start")

while(runSorter):
    hue, temp = readColorSensor()
    if hue != chamberColor:
        ballColor = getBallColor()
        print(ballColor)
        if ballColor == sequence[seqIndex]:
            keepBall()
            seqIndex += 1
        else:
            dropBall()

    if seqIndex == len(sequence):
        break

    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        runSorter = False




# wtf is servo jitter?!?!?! look into it
# -chris
