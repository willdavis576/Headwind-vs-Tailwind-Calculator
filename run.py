from convert import Convert
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from math import *

locData = Convert("14_12_20.gpx")
latArr = np.array([])
lonArr = np.array([])
elevArr = np.array([])
locData
for i in locData:
    lat, lon, elev = i
    latArr = np.append(latArr, lat)
    lonArr = np.append(lonArr, lon)
    elevArr = np.append(elevArr, elev)


def calculateWind(direction):
    direction = direction.split(',')


def windTypeCalc(latArr, lonArr):  # windperH):
    directions = []
    # tantheta = (y/x)
    for i in range(len(latArr)):
        if i < len(latArr) - 1:
            diffLat = latArr[i] - latArr[i + 1]
            diffLon = lonArr[i] - lonArr[i + 1]
            print(diffLat, diffLon, i)
            directions.append(degrees(atan(diffLat / diffLon)))
    return directions


directions = windTypeCalc(latArr, lonArr)
directions

data = [go.Scatter3d(x=lonArr, y=latArr, z=elevArr, mode='markers', marker=dict(size=1, color=255))]
fig = go.Figure(data=data)
fig.show()
