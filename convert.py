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
