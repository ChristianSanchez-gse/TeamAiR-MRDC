from gpiozero import Servo
from time import sleep
motor = Servo(18)

motor.value = -1
for i in range(5):
    print(5-i)
    sleep(1)

motor.value = 0
sleep(1)
motor.value = -1