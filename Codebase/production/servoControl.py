from time import sleep

# moves the ball with the servo
def moveBall(pushServo):
    pushServo.min()
    sleep(.5)
    pushServo.max()
    sleep(.5)
    pushServo.min()

def keepBall(doorServo, pushServo, vacuumMotor):
    setVacuumMotor(vacuumMotor, False)
    openDoor(doorServo)
    moveBall(pushServo)
    setVacuumMotor(vacuumMotor, True)

def dropBall(vacuumMotor):
    setVacuumMotor(vacuumMotor, False)

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

# controls the overall mechanism to eject the ball into the holding chamber
# def sortBall(doorServo, pushServo):
#     openDoor(doorServo)
#     sleep(2)
#     moveBall(pushServo)

# arm the motor
def calibrateMotor(vacuumMotor):
    # calibration
    print("The throttle value is now at 100%, wait until after the ascending beeps to continue")
    vacuumMotor.value = 1
    s = input("press enter to move the throttle signal to 0%")
    vacuumMotor.value = 0
    s = input("Press enter to end the calibration process (after the descending beeps)")
