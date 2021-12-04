import time # to check color every certain period of time
import webcolors # for human color names
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

# loop through to keep getting values
while True:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    # print(sensor.color_raw)
    input("Press Enter to read color...")
    color = sensor.color
    color_rgb = sensor.color_rgb_bytes
    R = color_rgb[0] / 255
    G = color_rgb[1] / 255
    B = color_rgb[2] / 255

    new_rgb = (R, G, B)

    max = -1
    max_index = -1
    min = 256
    min_index = -1
    for i in range(3):
        if (new_rgb[i] > max):
            max = new_rgb[i]
            max_index = i
        if (new_rgb[i] < min):
            min = new_rgb[i]
            min_index = i

    hue = -1
    if (max_index == 0):
        hue = (G-B)/(max-min)
    if (max_index == 1):
        hue = 2.0 + (B-R)/(max-min)
    if (max_index == 2):
        hue = 4.0 + (R-G)/(max-min)

    hue = hue * 60
    print("RGB: ", color_rgb)
    print("R: {0}, G: {1}, B; {2}".format(R, G, B))
    print("Hue: ", hue)

    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    print("  Temperature: {0}K Lux: {1}\n".format(temp, lux))
