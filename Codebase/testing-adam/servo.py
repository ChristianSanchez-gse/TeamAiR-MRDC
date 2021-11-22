from gpiozero import Servo
from time import sleep

servo1 = Servo(18)
servo2 = Servo(13)

def open():
    servo1.min()
    servo2.max()

def close():
    servo1.max()
    servo2.min()

try:
    while True:
        close()
        open()
        print("open")
        sleep(1.0)
        close()
        print("close")
        sleep(1.0)
except KeyboardInterrupt:
    print("close")
    sleep(1.0)
    print("we sleep")
    servo1.max()
    servo2.min()
    print("Program stopped")
