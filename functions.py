def Convert(file):
    line = ""
    data = {}
    header = ""
    loc = ""
    next = False
    counter = 0
    data = []
    f = open(file, "rt")
    while "</gpx" not in line:
        next = False
        line = f.readline()
        if "<gpx" in line and next == False:
            next = True

        if "<trk>" in line and next == False:
            next = True

        if "<trkseg" in line and next == False:
            next = True

        if "<trkpt" in line and next == False:
            start, lat, lon = line[line.index("<") + 1:].split(" ")
            elevation = f.readline()
            elevation = float(elevation[elevation.index(">") + 1:-7])
            data.append((float(lat[5:-1]), float(lon[5: - 3]), elevation))
            next = True
    f.close()
    return data


def getMaxCoords():
    import numpy as np
    maxLat = (np.where(latArr == np.amax(latArr)), np.amax(latArr))
    topCoord = (maxLat[1], lonArr[maxLat[0][0][0]])

    minLat = (np.where(latArr == np.amin(latArr)), np.amin(latArr))
    bottomCoord = (minLat[1], lonArr[minLat[0][0][0]])

    minLon = (np.where(lonArr == np.amin(lonArr)), np.amin(lonArr))
    leftCoord = (latArr[minLon[0][0][0]], minLon[1])

    maxLon = (np.where(lonArr == np.amax(lonArr)), np.amax(lonArr))
    rightCoord = (latArr[maxLon[0][0][0]], maxLon[1])

    return [topCoord, bottomCoord, leftCoord, rightCoord]


def getWind(coords, startTime, routeLength, predictedSpeed):
    import requests
    import json
    import apiKey

    data = []
    for i in range(4):
        response = requests.get(
            "http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat},{lon}".format(api_key=apiKey.apiKey, lat=coords[i](0), lon=coords[i](1)))
        data.append(json.loads(response.text))

        startTime = int(startTime[0])
        predictedTime = routeLength / predictedSpeed
        predictedTimeR = round(predictedTime)

        wind = []
        for i in range(predictedTimeR):
            time = i + startTime
            windData = data[i]["forecast"]["forecastday"][0]["hour"]
            wind.append((windData[time]['wind_mph'], windData[time]['wind_degree']))

    return wind
