from gpiozero import Servo
from time import sleep

doorServo = Servo(17)
pushServo = Servo(27)
val = -1

try:
    while True:
        doorServo.value = val
        pushServo.value = val
        sleep(0.1)
        val = val + 0.1
        if val > 1:
            val = -1
except KeyboardInterrupt:
        print("Program stopped")
