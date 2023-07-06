from logging import getLogger
from datetime import datetime as dt
import requests
#from flask import Flask, render_template, request, jsonify

#app = Flask(__name__, template_folder='templates')

logger = getLogger()


def button_it(lists):
    buttons = []
    try:
        if not isinstance(lists[0], tuple):
            for i in lists:
                buttons.append(
                    {
                        "title": i,
                        "payload": i,
                    }
                )
        else:
            for i in lists:
                buttons.append({
                    "title": i[0],
                    "payload": i[1]
                })
        return buttons
    except Exception as e:
        logger.exception(e)

'''
def hour_min_etc(time):
    time = time.split("-")[-1]
    try:
        time = dt.strptime(time, "%H:%M")
    except Exception as e:
        logger.exception("First try")
        logger.exception(e)
        try:
            time = dt.strptime(time, "%H:%M %p")
        except Exception as e:
            logger.exception("Second try")
            logger.exception(e)
    hour = time.strftime("%H")
    minute = time.strftime("%M")

    hour = int(hour)
    minute = int(minute)
    ampm = time.strftime("%p")
    if minute == 0:
        minute = "00"

    return hour, minute, ampm


def get_ampm(hour, context):
    
    """
        Returns AM or PM based on the hour given
    """
    logger.info(f"{__file__} : INSIDE get_ampm")
    logger.info(f"{__file__} : Hour : {hour}")
    logger.info(f"{__file__} : Context : {context}")
    if context == "sleep":
        if 8 <= hour <= 12:
            return "PM"
        elif 1 <= hour <= 12:
            return "AM"
    elif context == "breakfast":
        if hour > 11:
            return "PM"
        return "AM"
    elif context == "lunch":
        return "PM"
    elif context == "dinner":
        if 6 <= hour <= 12:
            return "PM"
        else:
            return "AM"
            

def get_time_diff(start, limit, context):
    """
        :start : start time Ex: wakeup time upper limit for breakfast time
        :limit : limit time Ex: for breakfast limit would be 12 PM
        :return : time difference between start and limit
    """
    logger.info(f"{__file__} : INSIDE get_time_diff")
    logger.info(f"{__file__} : Start : {start}")
    logger.info(f"{__file__} : Limit : {limit}")
    logger.info(f"{__file__} : Context : {context}")

    hour, minute, ampm = hour_min_etc(start)
    if limit < hour:
        limit = limit + 12
    if context == "breakfast":
        if hour < 6:
            hour = 6
    elif context == "lunch":
        if hour < 12:
            hour = 12
    elif context == "dinner":
        if hour < 7:
            hour = 7

    time_ranges = []
    for i in range(hour, limit + 1):
        
        if i == limit:
            break
        # if i == hour:
        
        if i < 12:
            # time_ranges.append(f"{i}:00-{i+1}:00 AM")
            time_ranges.append(f"{i}:{minute}-{i+1}:{minute} {get_ampm(i+1,context)}")
        elif i == 12:
            # time_ranges.append(f"{i}:00-{1}:00 PM")
            time_ranges.append(f"{i}:{minute}-{1}:{minute} {get_ampm(1,context)}")
        else:
            # time_ranges.append(f"{i-12}:00-{i-11}:00 PM")
            time_ranges.append(f"{i-12}:{minute}-{i-11}:{minute} {get_ampm(i-11,context)}")

    return time_ranges


def get_recommendation():
    """
        Returns the recommendation based on the persons health status given by doctor
    """
    logger.info(f"{__file__} : [INSIDE] get_recommendation")
    r = ["Morning Rounds", "Premeal", "Postmeal", "Mid Day Rounds", "Premeal", "Postmeal", "Evening Rounds", "Workout", "Premeal", "Postmeal", "Bedmeal"]
    t = {}
    for i in r:
        t[i] = "9:30"

    print(t)

    tell = "Based on your routine I recommend you following timings for your regular nursing rounds"

    for i, j in t.items():
        tell += f"<br><strong class=\"imp\">{i}</strong> : {j}"
    tell += "<br> Do you want to change the timings of any of your regular nursing rounds?"

    return tell
'''    

def Weather(city):
    API_key = "e77820355cbac076ad2f89e8bb738ca5"    #"Your API Key here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901&appid=API_KEY"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    #print("_________________")
    #print(Final_url)
    #print(weather_data)
    #print("_________________")
        
    #return weather_data['main']
    return weather_data.get('main')

def LocalSearch(search, city, place_type):
      access_token = "pk.eyJ1IjoicGt1bmR1MjUiLCJhIjoiY2xoaWwwNDBrMDFyaDNrcGNvMmhrZXlsaCJ9.sOxWZOMT9vWN-YyhQm4cwg"
      # Search text could be "city" or "place" if place_type="place" or it could be "beach", "hotel", "hospital" etc. if place_type="poi" (point of interest)
      # `proximity` is set to the coordinates of the campus
      # `bbox` is set to encompass the place/city such as Berkeley CA
      #Final_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/place.json?proximity=-122.25948,37.87221&bbox=-122.30937,37.84214,-122.23715,37.89838&access_token=" + access_token
      #print(Final_url)
      #Final_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + city + ".json" + "?proximity=ip" + "&access_token=" + access_token
      url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + search + ".json?limit=10&country=in&proximity=ip&types="+ place_type + "&access_token=" + access_token      
          
      #print(url)
      local_search_data = requests.get(url).json()
      features = local_search_data['features']
      #print(features)

      #return local_search_data['features']

      #return local_search_data['features'][0]['center'], local_search_data['features'][0]['bbox']

      
      # Defining a list of center coordinates
      city = city.lower()
      center_list = []
      for i in features:
            place_name = i['place_name'].lower()
            
            if place_name.find(city) != -1:
                #print(place_name)  
                center_list.append(i['center'])
      #print("_____________________")                       
      #print(center_list) 
     
      return center_list
      

if __name__ == "__main__":
  #city = 'Berkeley CA'
  #temperature=Weather(city)['temp']
  #humidity = Weather(city)['humidity']
  #places = LocalSearch(city)
  #wind_mph = Weather(city)['wind_speed']
  #print(temperature)
  #LocalSearch('Pune')
  #child()
  #print(wind_mph)
  #LocalSearch('gas station around Panaji, goa', "Goa", "poi")
  place_list = [
      "Ponda",
"Panjim", 
"Vasco da Gama",
"Verna",
"Cancolim",
"Baga", 
"Calangute", 
"Butterfly", 
"Mapusa",
"Agonda", 
"Chapora", 
"Sinquerim", 
"Palolem", 
"Anjuna", 
"Cabo de Rama", 
"Vagator",
"Arambol",
"Morjim",
"Madgao"
  ]
  '''
  for p in place_list:
      l = LocalSearch(f"places around {p}", "Goa", "place%2Cpoi%2Clocality")
      if len(l) == 0 : 
        #print(f" {p} - not found\n\n")
        print("not found")
      else:
        #print(f" {p} -  found\n\n")
        print("found")
    '''        
            
  #app.run(debug=True, port = 8001)
  
  for p in place_list:
      l = Weather(p)
      #l = Weather(f"{p}, Goa")
      #sprint(f"{p} - {l}")
      if l is None : 
        #print(f" {p} - not found\n\n")
        print("not found")
      else:
        #print(f" {p} -  found\n\n")
        print("found")
            

 
