from gpiozero import Servo
from time import sleep

servo1 = Servo(18)
servo2 = Servo(13)

try:
    while True:
        servo1.min()
        servo2.max()
        sleep(0.5)
        servo1.mid()
        servo2.mid();
        sleep(0.5)
        servo1.max()
        servo2.min();
        sleep(0.5)
except KeyboardInterrupt:
        print("Program stopped")
