import requests
city=str(input("Enter your city: "))
key='69804c504a3bb0ba7fb3f8d3d311375c'
def weather_check(key,city):
    url='http://api.openweathermap.org/data/2.5/find?q={city}&type=like&APPID={key}'
    res= requests.get(url).json() 
    print(json)
