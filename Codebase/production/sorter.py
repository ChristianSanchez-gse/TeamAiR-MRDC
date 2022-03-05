from gpiozero import Servo
import board
import adafruit_tcs34725

from colors import *
from servoControl import *

# initialize sensor and servos
i2c = board.I2C()
colorSensor = adafruit_tcs34725.TCS34725(i2c)
doorServo = Servo(14)
pushServo = Servo(15)
vacuumMotor = Servo(18)

# arming sequence
vacuumMotor.value = -1
sleep(0.5)
vacuumMotor.value = 0

# initialize the sequence
sequence = ["blue", "purple", "red", "blue"]
seqIndex = 0
chamberColor = -1

# prompt to look for color
user_input = input("Press any key to start")
runSorter = True
while(runSorter):
    hue, temp = readColorSensor(colorSensor)
    if hue != chamberColor:
        ballColor = getBallColor(colorSensor)
        print(ballColor)
        if ballColor == sequence[seqIndex]:
            keepBall(doorServo, pushServo, vacuumMotor)
            seqIndex += 1
        else:
            dropBall(vacuumMotor)

    if seqIndex == len(sequence):
        break

    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        runSorter = False


# wtf is servo jitter?!?!?! look into it
# -chris
