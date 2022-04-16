from gpiozero import Servo
from time import sleep
motor = Servo(18)

motor.value = 0.1
sleep(2)
motor.value = -1
