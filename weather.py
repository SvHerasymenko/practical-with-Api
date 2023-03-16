import requests
import json

city=str(input("Enter your city: "))



def weather_check(city):
    key='69804c504a3bb0ba7fb3f8d3d311375c'
    url='http://api.openweathermap.org/data/2.5/find?q={city}&type=like&APPID={key}'
    res= requests.get(url)
    try:
        data = {'Weather': res['weather'][0]['main'], 'Description': res['weather'][0]['description'], 'Curent temp': res['main']['temp'], 'Temp_min': res['main']['temp_min'], 'Temp_max': res['main']['temp_max']'}
        print(pd.DataFrame([data]))
    except:print('Enter the city name correctly')
    
weather_check(city)