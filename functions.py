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

    return topCoord, bottomCoord, leftCoord, rightCoord
