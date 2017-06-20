def randomNcoordinates(dataPointsNum, scales):
    dataPoints = []
    for j in range(dataPointsNum):
        datapoint = []
        for i in range(len(scales)):
            dataPointi = random.random() * scales[i]
            datapoint.append(dataPointi)
        dataPoints.append(datapoint)
    return dataPoints