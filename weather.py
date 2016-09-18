import time
import memcache
from requests_forecast import Forecast
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("temp", "null")
mc.set("hum", "null")
delhi=Forecast(apikey='API-KEY', latitude=28.6667, longitude=77.2167)

current = delhi.get_currently()

print current['temperature']
print current['humidity']
#time.sleep(10)

def getForecast():
	delhi=Forecast(apikey='1a22317442315eaffbd86f5d2fc72eef', latitude=28.6667, longitude=77.2167)
	current = delhi.get_currently()
        mc.set("temp", round(((current['temperature']-32)/1.8), 1))
        mc.set("hum", round(current['humidity'], 1))


while True:
	getForecast()
	time.sleep(600)
