from gpiozero import Servo
import board
import adafruit_tcs34725
import numpy as np

from colors import *
from servoControl import *

# initialize sensor and servos
i2c = board.I2C()
colorSensor = adafruit_tcs34725.TCS34725(i2c)
doorServo = Servo(14)
pushServo = Servo(15)
vacuumMotor = Servo(18)
chamberServo = Servo(23)

# arming sequence?
vacuumMotor.value = -1
sleep(0.5)

testVacuumSpeed(vacuumMotor)

# initialize the sequence
sequence = ["blue", "purple", "red", "blue"]
seqIndex = 0

# set this to the "ambient" hue reading of the color sensor
ambientColor = (30, 20, 30)

# determine if ball is in the chamber (sensor color a certain distance from ambient color)
def ballInChamber(sensorRGB):
    # distance = np.linalg.norm(np.array(sensorRGB) - ambientColor)
    # print(distance)
    # return distance > 100 # return true if color is within some distance
    return True

# prompt to look for color
user_input = input("Press any key to start")
runSorter = True
while(runSorter):
    sensorRGB = colorSensor.color_rgb_bytes

    # ball in the chamber
    if ballInChamber(sensorRGB):
        # get color of ball as a string
        ballColor = getBallColor(colorSensor)
        print(ballColor)

        # if it matches the next color we need, keep it
        if ballColor == sequence[seqIndex]:
            print("keeping ball")
            keepBall(doorServo, pushServo, vacuumMotor)
            seqIndex += 1
        else:  # otherwise drop it
            print("dropping ball")
            dropBall(vacuumMotor)

    # reached end of specified sequence
    if seqIndex == len(sequence):
        dropSequence(chamberServo);

    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        runSorter = False



# wtf is servo jitter?!?!?! look into it
# -chris
