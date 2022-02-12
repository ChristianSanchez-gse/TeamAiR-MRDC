import pigpio
import time
import os
open_io = "sudo pigiod" # starts the pigpio daemon (required to get motor working)
motor_pin = 18 # noted GPIO number
# test comment
pi = pigpio.pi()

pi.set_servo_pulsewidth(motor_pin, 1500)
time.sleep(5)

for i in range(3):
        pi.set_servo_pulsewidth(motor_pin, 2000)
        time.sleep(1)

pi.set_servo_pulsewidth(motor_pin, 0)
pi.stop()
