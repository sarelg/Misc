from opensky_api import OpenSkyApi
import pandas as pd
import geocoder
from geopy import distance
import numpy as np


def getplane():
    g = tuple(geocoder.ip('me').latlng)
    api = OpenSkyApi()
    statess = api.get_states().states
    dist, altitude, callsign, ICAO24, country, coord = [], [], [], [], [], []
    for state in statess:
        coor = (state.latitude, state.longitude)
        coord.append(coor)
        dist.append(round(distance.distance(coor, g).km, 2))
        altitude.append(state.geo_altitude)
        callsign.append(state.callsign)
        ICAO24.append(state.icao24)
        country.append(state.origin_country)
    d = {'distance': dist, 'callsign': callsign, 'coordinates': coord, 'altitude': altitude,
         'country': country, 'ICAO24': ICAO24}
    df = pd.DataFrame(data=d)
    mini = np.nanmin(df['distance'])
    return df[df['distance'] == mini]


print(getplane())


