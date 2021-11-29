from gpiozero import Servo
from time import sleep

servo1 = Servo(18)
servo2 = Servo(13)

# servo.value between -1 and 1
# otherwise min and max

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
        print("hello")
        sleep(1.0)
        close()
        print("close")
        sleep(1.0)
except KeyboardInterrupt:
    print("Program stopped")
