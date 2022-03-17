from time import sleep

# moves the ball with the servo
def moveBall(pushServo):
    pushServo.min()
    sleep(0.5)
    pushServo.max()
    sleep(0.5)
    pushServo.min()
    sleep(0.5)

# turn off vacuum, open the door, push the ball, turn on the vacuum
def keepBall(doorServo, pushServo, vacuumMotor):
    setVacuumMotor(vacuumMotor, False)
    openDoor(doorServo)
    moveBall(pushServo)
    setVacuumMotor(vacuumMotor, True)

# turn off the vacuum
def dropBall(vacuumMotor):
    setVacuumMotor(vacuumMotor, False)
    sleep(3)
    setVacuumMotor(vacuumMotor, True)

# test different speeds for vacuumMotor
def testVacuumSpeed(vacuumMotor):
    while (True):
        user_input = input("Press enter to test speed or # to stop: ")
        if (user_input == "#"):
            break

        for i in range(3):
            vacuumMotor.value = 1
            print(1)
            sleep(5)
            vacuumMotor.value = 0.7
            print(0.7)
            sleep(5)
            vacuumMotor.value = 0.5
            print(0.5)
            sleep(5)
            vacuumMotor.value = 0.3
            print(0.3)
            sleep(5)
            vacuumMotor.value = -1
            print("off")
            sleep(2)

# turn vacuum on/off
def setVacuumMotor(vacuumMotor, on):
    if on:
        vacuumMotor.value = 0
    else:
        vacuumMotor.value = -1

# opens the door of the sorting mechanism
def openDoor(doorServo):
    doorServo.min()
    sleep(0.5)
    doorServo.max()
    sleep(0.5)
    doorServo.min()
    sleep(0.5)

# # calibrate motor
# def calibrateMotor(vacuumMotor):
#     # calibration
#     print("The throttle value is now at 100%, wait until after the ascending beeps to continue")
#     vacuumMotor.value = 1
#     s = input("press enter to move the throttle signal to 0%")
#     vacuumMotor.value = 0
#     s = input("Press enter to end the calibration process (after the descending beeps)")

def dropSequence(chamberServo):
    chamberServo.min()
    sleep(0.5)
    chamberServo.max()
    sleep(0.5)
    chamberServo.min()
    sleep(0.5)
