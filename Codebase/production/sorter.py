from gpiozero import Servo
from time import sleep
from colors import getHue
import board
import adafruit_tcs34725
from statistics import mean

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

doorServo = Servo(14)
pushServo = Servo(15)
val = -1

# moves the ball with the servo
def moveBall():
    pushServo.min()
    sleep(.5)
    pushServo.max()
    sleep(.5)
    pushServo.min()

def keepBall():
    vacuumMotor(False)
    openDoor()
    moveBall()
    vacuumMotor(True)

def dropBall():
    vacuumMotor(False)

def vacuumMotor(on):
    pass

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

    for i in range(3):
        print("getting average...")
        h, t = readColorSensor()
        hueList.append(h)
        tempList.append(t)
        sleep(0.3)

    hueAvg = mean(hueList)
    tempAvg = mean(tempList)

    if hueAvg < 5 or hueAvg > 350:
        # check temp for pink or red
        if tempAvg < 3000:
            return "red"
        else:
            return "pink"
    elif hueAvg < 13:
        return "orange"
    elif hueAvg < 70:
        return "yellow"
    elif hueAvg < 120:
        return "green"
    elif hueAvg < 230:
        return "blue"
    else:
        return "purple"


    

# main function
runSorter = True
chamberColor = -1
vacuumMotor(True)
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
