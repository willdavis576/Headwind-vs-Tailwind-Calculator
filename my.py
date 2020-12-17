import metoffer
import pprint

api_key = "b48a2753-32e0-4ecc-8ddc-b2bdaf9de164"

M = metoffer.MetOffer(api_key)
x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)

y = metoffer.Weather(x)

pprint.pprint(y.data)
