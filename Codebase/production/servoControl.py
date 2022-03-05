from time import sleep

# moves the ball with the servo
def moveBall(pushServo):
    pushServo.min()
    sleep(.5)
    pushServo.max()
    sleep(.5)
    pushServo.min()

# turn off vacuum, open the door, push the ball, turn on the vacuum 
def keepBall(doorServo, pushServo, vacuumMotor):
    setVacuumMotor(vacuumMotor, False)
    openDoor(doorServo)
    moveBall(pushServo)
    setVacuumMotor(vacuumMotor, True)

# turn off the vacuum
def dropBall(vacuumMotor):
    setVacuumMotor(vacuumMotor, False)

# turn vacuum on/off
def setVacuumMotor(vacuumMotor, on):
    if on:
        vacuumMotor.value = 0.5
    else:
        vacuumMotor.value = 0

# opens the door of the sorting mechanism
def openDoor(doorServo):
    doorServo.min()
    sleep(.5)
    doorServo.max()
    sleep(.5)
    doorServo.min()

# arm the motor
def calibrateMotor(vacuumMotor):
    # calibration
    print("The throttle value is now at 100%, wait until after the ascending beeps to continue")
    vacuumMotor.value = 1
    s = input("press enter to move the throttle signal to 0%")
    vacuumMotor.value = 0
    s = input("Press enter to end the calibration process (after the descending beeps)")
