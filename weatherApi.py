import requests
import json
import apiKey

response = requests.get("http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat},{lon}".format(api_key=apiKey.apiKey, lat=apiKey.lat, lon=apiKey.lon))

data = json.loads(response.text)

startTime = "9:00"
startTime = int(startTime[0])
wind = []
windData = data["forecast"]["forecastday"][0]["hour"]
wind.append((windData[startTime]['wind_mph'], windData[startTime]['wind_degree']))

routeLength = int("50")
predictedSpeed = int("13")

predictedTime = routeLength / predictedSpeed

predictedTimeR = round(predictedTime)


for i in range(predictedTimeR):
    time = i + 1 + startTime
    wind.append((windData[time]['wind_mph'], windData[time]['wind_degree']))
