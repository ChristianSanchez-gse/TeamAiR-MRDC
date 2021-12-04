import time # to check color every certain period of time
import webcolors # for human color names
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

# loop through to keep getting values
while True:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    print(sensor.color_raw)

    color = sensor.color
    color_rgb = sensor.color_rgb_bytes
    print("RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(color, color_rgb))
    # print("RGB to human language value: ", webcolors.rgb_to_name(color_rgb))
    # Read the color temperature and lux of the sensor too.
    # temp = sensor.color_temperature
    # lux = sensor.lux
    # print("Temperature: {0}K Lux: {1}\n".format(temp, lux))
    # Delay for a second and repeat.
    time.sleep(1.0)
