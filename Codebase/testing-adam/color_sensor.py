import time  # to check color every certain period of time
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

from colors import *  # functions I wrote

# open file to write to
filename = input("Enter a filename: ")
f = open(filename, "a")

run = True
while run:
    # prompt user to read color or stop program
    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        run = False
        break

    # read what's in front of the sensor and calculate the hue and temperature
    color_rgb = sensor.color_rgb_bytes
    temp = round(sensor.color_temperature)
    hue = round(getHue(color_rgb))

    # print out info and write hue and temp to file
    print("Hue: {0}, Temperature: {1}".format(hue, temp))
    f.write("{0} {1}\n".format(hue, temp))

# close the file
f.close();
