from gpiozero import Servo
import board
import adafruit_tcs34725

from time import sleep
from statistics import mean

from colors import *
from servoControl import *


i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

doorServo = Servo(14)
pushServo = Servo(15)
vacuumMotor = Servo(25)
val = -1

# moves the ball with the servo
def moveBall():
    pushServo.min()
    sleep(.5)
    pushServo.max()
    sleep(.5)
    pushServo.min()

def keepBall():
    setVacuumMotor(False)
    openDoor()
    moveBall()
    setVacuumMotor(True)

def dropBall():
    setVacuumMotor(False)

def setVacuumMotor(on):
    if on:
        vacuumMotor.value = 0.5
    else:
        vacuumMotor.value = 0


# opens the door of the sorting mechanism
def openDoor():
    doorServo.min()
    sleep(.5)
    doorServo.max()
    sleep(.5)
    doorServo.min()

# controls the overall mechanism to eject the ball into the holding chamber
def sortBall():
    openDoor()
    sleep(2)
    moveBall()

def readColorSensor():
    hue = round(getHue(sensor.color_rgb_bytes))
    temp = round(sensor.color_temperature)
    return hue, temp


# Returns true if the correct color of the ball is found, else false.
def rightColor():
    if (hue > 110 and hue < 130):
        return True
    else:
        return False

def getBallColor():
    hueList = []
    tempList = []
    colorsList = []

    for i in range(3):
        print("getting average...")
        h, t = readColorSensor()
        hueList.append(h)
        tempList.append(t)
        sleep(0.3)

    hueAvg = mean(hueList)
    tempAvg = mean(tempList)

#     if hueAvg < 5 or hueAvg > 350:
#         # check temp for pink or red
#         if tempAvg < 3000:
#             return "red"
#         else:
#             return "pink"
#     elif hueAvg < 13:
#         return "orange"
#     elif hueAvg < 70:
#         return "yellow"
#     elif hueAvg < 120:
#         return "green"
#     elif hueAvg < 230:
#         return "blue"
#     else:
#         return "purple"

    if hueAvg >= 358 or hueAvg <= 4:
        colorsList.append("red")
    if hueAvg >= 5 and hueAvg <= 10:
        colorsList.append("orange")
    if hueAvg >= 30 and hueAvg <= 70:
        colorsList.append("yellow")
    if hueAvg >= 100 and hueAvg <= 130:
        colorsList.append("green")
    if hueAvg >= 210 and hueAvg <= 240:
        colorsList.append("blue")
    if hueAvg >= 250 and hueAvg <= 270:
        colorsList.append("purple")
    if hueAvg >= 350 or  hueAvg <= 2:
        colorsList.append("pink")


    if len(colorsList) == 0:
        return None
    elif len(colorsList) == 1:
        return colorsList[0]
    else:
        if tempAvg >= 2200 or tempAvg <= 2700:
            return "red"
        if tempAvg >= 2400 and tempAvg <= 2500:
            return "orange"
        if tempAvg >= 2400 and tempAvg <= 2900:
            return "yellow"
        if tempAvg >= 4000 and tempAvg <= 7000:
            return "green"
        if tempAvg >= 12000 and tempAvg <= 15000:
            return "blue"
        if tempAvg >= 5800 and tempAvg <= 6100:
            return "purple"
        if tempAvg >= 3600 and tempAvg <= 3800:
            return "pink"



def calibrateMotor():
    # calibration
    print("The throttle value is now at 100%, wait until after the ascending beeps to continue")
    vacuumMotor.value = 1
    s = input("press enter to move the throttle signal to 0%")
    vacuumMotor.value = 0
    s = input("Press enter to end the calibration process (after the descending beeps)")


# main function
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
