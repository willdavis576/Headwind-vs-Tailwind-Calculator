

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
