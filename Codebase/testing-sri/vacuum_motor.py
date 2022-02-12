import pigpio
import time
motor_pin = 2 # noted GPIO number

pi = pigpio.pi()

pi.set_servo_pulsewidth(motor_pin, 1300)
time.sleep(5)

for i in range(3):
        pi.set_servo_pulsewidth(motor_pin, 1500)
        time.sleep(1)

pi.set_servo_pulsewidth(motor_pin, 0)
pi.stop()
