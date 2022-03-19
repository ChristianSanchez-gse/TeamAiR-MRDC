import time  # to check color every certain period of time
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

from colors import *  # functions I wrote

# open file to write to
filename = input("Enter a filename: ")
f = open("color-data/" + filename, "w")

while True:
    # prompt user to read color or stop program
    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        break

    # read what's in front of the sensor
    color_rgb = sensor.color_rgb_bytes

    # print rgb values and write to file
    print("RGB: {0}".format(color_rgb))
    f.write("{0} {1} {2}\n".format(color_rgb[0], color_rgb[1], color_rgb[2]))

# close the file
f.close();
