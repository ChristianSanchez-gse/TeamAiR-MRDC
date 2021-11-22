from gpiozero import Servo
from time import sleep

servo1 = Servo(18)
servo2 = Servo(13)

def open():
    servo1.min()
    servo2.max()

def close():
    servo1.max()
    servo2.min();

try:
    while True:
        open()
        sleep(1.0)
        close()
        sleep(1.0)
except KeyboardInterrupt:
        print("Program stopped")
