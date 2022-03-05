from gpiozero import Servo
from time import sleep
motor = Servo(18)

# Documentation:

# The ESC that we use for the motor is able to be controlled by the motor library since both components
# use a pwm signal for control.

# After research, I found that reason for a motor not spinning after giving it a command is due to the fact that the
# ESC needs to be calibrated before first use. The calibration process was used with wrong values at first so the motor was not
# spinning because it could never find the 0% value before startup.

# If the ESC should ever need calibration, run this script in order to calibrate it along with following the picture of the
# documentation listed in the github page.



# How to control the motor once calibrated:
# ----------------------------------------------------------------------------------------------------------------------------------------------
# The motor can be controlled by changing the values of the pwm duty cycle just like a servo. In this library, 
# we can just set the motor value from a range -1 to 1 where 0 would be mid throttle. For safety reasons, the first 
# signal that the ESC should read is "0% throttle", or depicted by the code as "motor.value = -1". When this occurs, 
# the motor will beep 3 to let the user know that the power is connected, and then another 2 beeps (a low and high tone) 
# to let the user know that it correctly recieved the 0% throttle value. After this, the motor can then be used by changing 
# motor.value




try:
    # calibration
    print("The throttle value is now at 100%, wait until after the ascending beeps to continue")
    motor.value = 1
    s = input("press enter to move the throttle signal to 0%")
    motor.value = -1
    s = input("Press enter to end the calibration process (after the descending beeps)")



except KeyboardInterrupt:
	print("Program stopped")