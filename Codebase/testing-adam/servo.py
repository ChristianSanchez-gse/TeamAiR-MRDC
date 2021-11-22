from gpiozero import Servo
from time import sleep

servo1 = Servo(18)
servo2 = Servo(13)

def open(x):
    servo1.value(x)
    servo2.value(1-x)

def close(x=0):
    servo1.value(x)
    servo2.value(1-x)

try:
    while True:
        close()
        open(1)
        print("open")
        sleep(1.0)
        close(0)
        print("close")
        sleep(1.0)
except KeyboardInterrupt:
    print("Program stopped")
