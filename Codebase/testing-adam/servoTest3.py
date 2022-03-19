from gpiozero import Servo
from time import sleep

servo1 = Servo(14)
servo2 = Servo(15)

# servo.value between -1 and 1
# otherwise min and max

def open():
    print("open")
    servo1.min()
    servo2.max()

def close():
    print("close")
    servo1.max()
    servo2.min()

try:
    while True:
        close()
        open()
        sleep(1.0)
        close()
        sleep(1.0)
except KeyboardInterrupt:
    print("Program stopped")
