import pigpio
import time
motor_pin = 2 # noted GPIO number

pi = pigpio.pi()

for i in range(3):
        pi.set_servo_pulsewidth(motor_pin, 1500)
        time.sleep(1)
        pi.set_servo_pulsewidth(motor_pin, 1600)
        time.sleep(1)
        pi.set_servo_pulsewidth(motor_pin, 1700)
        time.sleep(1)
        pi.set_servo_pulsewidth(motor_pin, 1800)
        time.sleep(1)
        pi.set_servo_pulsewidth(motor_pin, 1900)
        time.sleep(1)
        pi.set_servo_pulsewidth(motor_pin, 2000)
        time.sleep(1)


pi.set_servo_pulsewidth(motor_pin, 0)
pi.stop()
