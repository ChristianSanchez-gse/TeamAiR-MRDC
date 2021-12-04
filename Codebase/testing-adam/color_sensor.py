import time # to check color every certain period of time
import webcolors # for human color names
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

from colors import *

# loop through to keep getting values
while True:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    # print(sensor.color_raw)
    input("Press enter to read color...")
    color_rgb = sensor.color_rgb_bytes
    temp = round(sensor.color_temperature)
    hue = round(getHue(color_rgb))

    print("Hue: {0}, Temperature: {1}".format(hue, temp))
