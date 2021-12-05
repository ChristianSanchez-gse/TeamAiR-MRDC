import time # to check color every certain period of time
import webcolors # for human color names
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

from colors import *

filename = input("Enter a filename: ")

f = open(filename, "a")

# loop through to keep getting values
run = True
while run:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    # print(sensor.color_raw)
    user_input = input("Press enter to read color or # to stop: ")
    if (user_input == "#"):
        run = False
        break

    color_rgb = sensor.color_rgb_bytes
    temp = round(sensor.color_temperature)
    hue = round(getHue(color_rgb))

    print("Hue: {0}, Temperature: {1}".format(hue, temp))
    f.write("{0} {1}\n".format(hue, temp))

f.close();
