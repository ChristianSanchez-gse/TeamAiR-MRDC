from gpiozero import Servo
from time import sleep
from colors import getHue
import board
import adafruit_tcs34725

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

# Returns true if the correct color of the ball is found, else false.
def rightColor():
    color_rgb = sensor.color_rgb_bytes
    hue = round(getHue(color_rgb))
    if (hue > 110 and hue < 130):
        return True
    else:
        return False


#main function
runSorter = True
#vacuumMotor(True)
while(runSorter == True):
    sleep(4)
    if (rightColor() == True):
        sortBall()
        #vacuumMotor(False)



# wtf is servo jitter?!?!?! look into it
# -chris
