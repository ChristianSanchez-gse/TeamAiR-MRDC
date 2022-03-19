def getHue(color_rgb):
    R = color_rgb[0] / 255
    G = color_rgb[1] / 255
    B = color_rgb[2] / 255

    new_rgb = (R, G, B)

    max = -1
    max_index = -1
    min = 256
    for i in range(3):
        if (new_rgb[i] > max):
            max = new_rgb[i]
            max_index = i
        if (new_rgb[i] < min):
            min = new_rgb[i]

    hue = -1
    if (max_index == 0):
        hue = (G-B)/(max-min)
    elif (max_index == 1):
        hue = 2.0 + (B-R)/(max-min)
    elif (max_index == 2):
        hue = 4.0 + (R-G)/(max-min)

    hue *= 60
    if hue < 0:
        hue += 360
    return hue
