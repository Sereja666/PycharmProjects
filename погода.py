
from yaweather import *

api_key='1111'



y = YaWeather(api_key=api_key)

# res = y.forecast(Russia.Krasnodar)
# forc = {}
# for key, value in res:
#     # print("ключ " + str(key) + " значение " + str(value))
#     forc.update(res)
# forecasts = forc['forecasts']
# print(forecasts)
forc = {}
raw_dict = y.forecast_raw(Russia.Krasnodar)
print(raw_dict['forecasts'])
# for key in raw_dict['forecasts'].items():
#     print(key)
forc.setdefault(raw_dict['forecasts'])
print(forc)
