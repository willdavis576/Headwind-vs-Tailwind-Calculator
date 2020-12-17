from functions import *
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


# data = [go.Scatter3d(x=lonArr, y=latArr, z=elevArr, mode='markers', marker=dict(size=1, color=255))]
# fig = go.Figure(data=data)
# fig.show()
