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
chamberServo = Servo(23)

# arming sequence
vacuumMotor.value = -1
sleep(0.5)

# test speeds
# for i in range(3):
#     vacuumMotor.value = 1
#     print(1)
#     sleep(5)
#     vacuumMotor.value = 0.7
#     print(0.7)
#     sleep(5)
#     vacuumMotor.value = 0.5
#     print(0.5)
#     sleep(5)
#     vacuumMotor.value = 0.3
#     print(0.3)
#     sleep(5)
#     vacuumMotor.value = -1
#     print("off")
#     sleep(2)

# initialize the sequence
sequence = ["blue", "purple", "red", "blue"]
seqIndex = 0

# set this to the "ambient" hue reading of the color sensor
chamberColor = -1

# prompt to look for color
user_input = input("Press any key to start")
runSorter = True
while(runSorter):
    # hue, temp = readColorSensor(colorSensor)
    sensorRGB = colorSensor.color_rgb_bytes

    # ball in the chamber
    # if hue != chamberColor:
    #     # get color of ball as a string
    #     ballColor = getBallColor(colorSensor)
    #     print(ballColor)

    #     # if it matches the next color we need, keep it
    #     if ballColor == sequence[seqIndex]:
    #         keepBall(doorServo, pushServo, vacuumMotor)
    #         seqIndex += 1
    #     else:  # otherwise drop it
    #         dropBall(vacuumMotor)



    # reached end of specified sequence
    if seqIndex == len(sequence):
        break

    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        runSorter = False


# wtf is servo jitter?!?!?! look into it
# -chris
