def MonteCarlo(funct, points, scales, multiplicationFactor=1):  #
    numberInFunc = 0
    scalingFactor = 1
    for point in points:
        value = []
        for i in range(len(scales) - 1):
            value.append(point[i])
        result = funct(value)
        if result >= point[-1]:
            numberInFunc += 1
    for i in range(len(scales)):
        scalingFactor *= scales[i]
    integral = float((float(numberInFunc) / float(len(points))) * scalingFactor)
    error = float((float(np.sqrt(len(points))) / float(len(points))) * scalingFactor)
    return "%0.6f +/- %0.6f" % (integral * multiplicationFactor, error * multiplicationFactor)