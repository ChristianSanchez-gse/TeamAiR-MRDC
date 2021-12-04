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
    input("Press Enter to read color...")
    color = sensor.color
    color_rgb = sensor.color_rgb_bytes

    hue = getHue(color_rgb)
    # print("R: {0}, G: {1}, B; {2}".format(R, G, B))
    print("Hue: ", hue)

    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    print("  Temperature: {0}K Lux: {1}\n".format(temp, lux))
