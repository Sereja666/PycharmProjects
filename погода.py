# import pyowm
# owm = pyowm.OWM('95a56e49619983c664e090256e4be08c')
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('Krasnodar, RU')
# w = observation.weather
# temp = w.temperature('celsius')
# status = w.detailed_status
# print("сейчас " + str(int(temp['temp'])) + " degrees and " + status)

#
# import pyowm
# from pyowm.commons.enums import SubscriptionTypeEnum
# from pyowm.utils.measurables import kelvin_to_celsius
#
# city = 'Krasnodar'
#
# config = {
#     'subscription_type': SubscriptionTypeEnum.FREE,
#     'language': 'ru',
#     'connection': {
#         'use_ssl': True,
#         'verify_ssl_certs': True,
#         'use_proxy': False,
#         'timeout_secs': 5
#     }
#
# }
# owm = pyowm.OWM('95a56e49619983c664e090256e4be08c', config=config)
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(city)
# w = observation.weather
#
# print("В городе " + city + " сейчас температура: " + str(kelvin_to_celsius(w.temp['temp'])) + " по Цельсию.")
# print('облачность  ' + str(w.clouds) )
# print('осадки  ' + str(w.rain) )
# print('влажность  ' + str(w.humidity) )
# print('ветер   ' + str(w.wind()) )
# print('общая   ' + str(w.detailed_status ))
# forecast = mgr.forecast_at_place('Krasnodar,RU', 'daily')
# print("прогноз " + forecast)
from yaweather import *

api_key='c828a84c-1496-4a66-9e24-19183e20d6d9'



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