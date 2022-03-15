from time import sleep
from statistics import mean
import numpy as np

# these are the values we get from testing
red = (74, 5, 3)
orange = (67, 8, 2)
yellow = (27, 27, 2)
green = (8, 41, 7)
blue = (2, 18, 47)
purple = (13, 11, 27)
pink = (43, 6, 1)
colorsRGB = (red, orange, yellow, green, blue, purple, pink)

# read color 10 times, get the average, then return a string color depending on hue and temp values
def getBallColor(sensor):
    rgbReadings = []

    print("getting average...")

    for i in range(10):
        rgbReadings.append(sensor.color_rgb_bytes)
        sleep(0.1)
    
    print("done")

    rgbAverage = np.mean(rgbReadings, axis=0)

    return getClosestColor(rgbAverage)

def getClosestColor(rgbAverage):
    distances = []
    for c in colorsRGB:
        distances.append(np.linalg.norm(c - rgbAverage))
    return colorsRGB[distances.index(min(distances))]