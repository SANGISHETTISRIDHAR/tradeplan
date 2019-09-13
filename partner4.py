
""" In this i entered banglore woeid  at the endpoint of the location"""

import requests
baseurl="https://www.metaweather.com/api/location/"
endpointurl='2295420/'
findurl=baseurl+endpointurl
resp=requests.get(findurl)
print(resp)

""" I copied output below for my understand purpose and also did operations on data like below"""

outputdata={'consolidated_weather':
         [
             {'id': 4661362456264704, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'W', 'created': '2019-09-13T03:52:09.119314Z', 'applicable_date': '2019-09-13', 'min_temp': 20.525, 'max_temp': 28.5, 'the_temp': 28.25, 'wind_speed': 5.905701557949574, 'wind_direction': 272.6663655959727, 'air_pressure': 1012.4200000000001, 'humidity': 69, 'visibility': 12.999396027201144, 'predictability': 77}, 
             {'id': 5184534855286784, 'weather_state_name': 'Light Rain', 'weather_state_abbr': 'lr', 'wind_direction_compass': 'WNW', 'created': '2019-09-13T03:52:11.872949Z', 'applicable_date': '2019-09-14', 'min_temp': 19.68, 'max_temp': 28.47, 'the_temp': 27.674999999999997, 'wind_speed': 4.824230473106392, 'wind_direction': 281.4829889165135, 'air_pressure': 1011.995, 'humidity': 68, 'visibility': 12.295382466396244, 'predictability': 75}, 
             {'id': 5661729595850752, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'WNW', 'created': '2019-09-13T03:52:14.892181Z', 'applicable_date': '2019-09-15', 'min_temp': 19.54, 'max_temp': 28.78, 'the_temp': 28.075, 'wind_speed': 5.3677107718126145, 'wind_direction': 282.8237775410464, 'air_pressure': 1010.88, 'humidity': 67, 'visibility': 13.246391076115483, 'predictability': 77}, 
             {'id': 6461118052564992, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'WNW', 'created': '2019-09-13T03:52:17.870262Z', 'applicable_date': '2019-09-16', 'min_temp': 19.11, 'max_temp': 26.994999999999997, 'the_temp': 27.27, 'wind_speed': 6.410827271905407, 'wind_direction': 291.1967573593125, 'air_pressure': 1009.77, 'humidity': 71, 'visibility': 13.481890757973435, 'predictability': 77}, 
             {'id': 5426347822284800, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'WNW', 'created': '2019-09-13T03:52:21.116516Z', 'applicable_date': '2019-09-17', 'min_temp': 18.814999999999998, 'max_temp': 27.555, 'the_temp': 26.89, 'wind_speed': 6.39634809023569, 'wind_direction': 297.30055437849165, 'air_pressure': 1009.52, 'humidity': 71, 'visibility': 13.199166865505447, 'predictability': 77}, 
             {'id': 6037006540865536, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'WNW', 'created': '2019-09-13T03:52:23.804406Z', 'applicable_date': '2019-09-18', 'min_temp': 19.07, 'max_temp': 27.285, 'the_temp': 25.37, 'wind_speed': 6.099740515390122, 'wind_direction': 285.0, 'air_pressure': 1009.66, 'humidity': 77, 'visibility': 9.893472122802832, 'predictability': 77}
         ], 
        'time': '2019-09-13T11:52:34.320849+05:30', 'sun_rise': '2019-09-13T06:08:36.163367+05:30', 'sun_set': '2019-09-13T18:22:25.684064+05:30', 'timezone_name': 'LMT', 'parent': {'title': 'India', 'location_type': 'Country', 'woeid': 23424848, 'latt_long': '21.786600,82.794762'}, 
        'sources': 
            [
                {'title': 'BBC', 'slug': 'bbc', 'url': 'http://www.bbc.co.uk/weather/', 'crawl_rate': 360}, 
                {'title': 'Forecast.io', 'slug': 'forecast-io', 'url': 'http://forecast.io/', 'crawl_rate': 480}, 
                {'title': 'Met Office', 'slug': 'met-office', 'url': 'http://www.metoffice.gov.uk/', 'crawl_rate': 180},
                {'title': 'OpenWeatherMap', 'slug': 'openweathermap', 'url': 'http://openweathermap.org/', 'crawl_rate': 360}, 
                {'title': 'Weather Underground', 'slug': 'wunderground', 'url': 'https://www.wunderground.com/?apiref=fc30dc3cd224e19b', 'crawl_rate': 720}, 
                {'title': 'World Weather Online', 'slug': 'world-weather-online', 'url': 'http://www.worldweatheronline.com/', 'crawl_rate': 360}
            ], 
        'title': 'Bangalore', 'location_type': 'City', 'woeid': 2295420, 'latt_long': '12.955800,77.620979', 'timezone': 'Asia/Kolkata'}
day=[]
temp=[]
for x,y in outputdata.items():
    if x=='consolidated_weather':
        a=len(y)
        print(a)
        for z in range(a):
           day.append(y[z]['applicable_date'])
           temp.append(y[z]['the_temp'])
print(day)
print(temp)

from matplotlib import pyplot
x=day
y=temp
pyplot.plot(x,y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

pyplot.xlabel('dates')
pyplot.ylabel('temparature')
pyplot.title(" This week Weather graph")
pyplot.grid(True)
pyplot.show()