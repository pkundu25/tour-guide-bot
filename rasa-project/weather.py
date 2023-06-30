import requests

def Weather(city):
    API_key = "e77820355cbac076ad2f89e8bb738ca5"    #"Your API Key here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901&appid=API_KEY"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    
    return weather_data['main']


'''
if __name__ == "__main__":
  city = 'Delhi'
  temperature=Weather(city)['temp']
  humidity = Weather(city)['humidity']
  #wind_mph = Weather(city)['wind_speed']
  #print(temperature)
  print(humidity)
  #print(wind_mph)
'''  
