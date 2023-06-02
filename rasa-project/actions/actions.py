# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#

import logging
from typing import Any, Text, Dict, List
import os
import re
import string
import requests, json
import flask
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
#from weather import Weather
from utils.helper import LocalSearch


logging.basicConfig(level=logging.DEBUG)

'''
class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return []
'''        

'''
class ActionGreet(Action):
    def name(self):
        return "action_PN_2_save_name"

    def run(self, dispatcher, tracker, domain):
        intros = ["im ", "i am ", "i am called ", "im called ", "call me "]
        name = ""
        stripped = ""
        sentence = (tracker.latest_message)['text']
        exclude = set(string.punctuation)
        stripped = stripped.join(ch for ch in sentence if ch not in exclude).lower()
        for intro in intros:
            if re.search(intro, stripped):
                name = stripped.split(intro)[1]
                name = name.title()
        if name is "":
            name = sentence.title()
        logging.debug("*** ActionGreet: Name saved as: " + name)
        return [SlotSet("name", name)]
    

class ActionUtterGreet(Action):

    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tell = "Hey! How are you?"
        dispatcher.utter_message(text=tell)

        return []    
'''    

'''
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        temperature=Weather(city)['temp']
        response = "The current temperature at {} is {} degree Celsius.".format(city,temperature)
        dispatcher.utter_message(response)

        return [SlotSet('location',city)]
'''  

class ActionGoodMorning(Action):

    def name(self) -> Text:
        return "action_greet_timeofday"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        now = datetime.now()
        hour = int(now.strftime('%H'))
        if(hour>=0 and hour<12):
            response = "Hi! Good Morning"
            #print("Hi! Good Morning")
        elif(hour>=12 and hour<=17):
            response = "Hi! Good Afternoon"
            #print("Hi! Good Afternoon")
        if (hour>=17 and hour<24):
            response = "Hi! Good Evening"
            #print("Hi! Good Evening")            
        
        dispatcher.utter_message(text=response)
        return []    
        #return [FollowupAction(name = "action_weather")]

'''
class ActionCheckWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot('location')
        temperature = Weather(city)['temp']
        #humidity = Weather(city)['humidity']
        #wind_mph = Weather(city)['speed']

        response = "The current temperature at {} is {} degree Celsius.".format(city, temperature)
        
        if (temperature > 27):
            response+= " Outside is hot"
        else:
            response+= " Outside is cold"
                    

        dispatcher.utter_message(response)        

        #return [SlotSet('location', city)]
    
        #return [FollowupAction(name: "action_weather_humidity", timestamp: Optional[float] = None)]
        return [FollowupAction(name = "action_weather_humidity")]
    

class ActionCheckHumidity(Action):

    def name(self) -> Text:
        return "action_weather_humidity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot('location')
        #temperature = Weather(city)['temp']
        humidity = Weather(city)['humidity']
        #wind_mph = Weather[]'wind']['speed']

        response = "The current humidity at {} is {} %.".format(city, humidity)
        dispatcher.utter_message(response)

        return [SlotSet('location', None)]  
    
'''

'''
app = Flask(__name__)
@app.route('/')
def child():
    return render_template("mapview.html")
'''    

class ActionSearchPlaces(Action):

    def name(self) -> Text:
        return "action_local_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot('location')

        #search1 = "goa"
        # features is a list  that contains centers (having list of values) around the search place
        centers =  LocalSearch(city, "place")
 
        #center_list = [i['center'] for i in features]
        '''
        center_list = []
        
        for i in features:
            d = []
            d['center'] = i['center']
            center_list.append(d['center'])
        '''            
                   

        #(center, bbox)  = LocalSearch(city)
        #center_list = []    
        # center_list is a list if lists (each having 2 values)
        if len(centers) < 5:
            center0 = centers[0]                

            lng0 = center0[0]
            lat0 = center0[1]
            lng1 = None
            lat1 = None
            lng2 = None
            lat2 = None
            lng3 = None
            lat3 = None
            lng4 = None
            lat4 = None       
            
        else:     
            center0 = centers[0]
            center1 = centers[1] 
            center2 = centers[2] 
            center3 = centers[3] 
            center4 = centers[4]                     

            lng0 = center0[0]
            lat0 = center0[1]
            lng1 = center1[0]
            lat1 = center1[1]
            lng2 = center2[0]
            lat2 = center2[1]
            lng3 = center3[0]
            lat3 = center3[1]
            lng4 = center4[0]
            lat4 = center4[1]

            #response = "You can find the places in the map at {}, {}.".format(lng,lat)
            #dispatcher.utter_message(response)

        dispatcher.utter_message(
            template ="utter_user_details",            
            lng0 = lng0,
            lat0 = lat0,
            lng1 = lng1,
            lat1 = lat1,
            lng2 = lng2,
            lat2 = lat2,
            lng3 = lng3,
            lat3 = lat3,
            lng4 = lng4,
            lat4 = lat4,
            city = city            
        )

        #return [SlotSet('location', None)]   
        return []


class ActionSearchPoi(Action):

    def name(self) -> Text:
        return "action_local_search_poi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot('location')
        poi = tracker.get_slot('poi')
        #poi = "beaches"
        print(poi)
        search = poi + " nearby " + city
        print(search)

        #search1 = "Indore"
        # List of center coordinates around the search place
        centers =  LocalSearch(search, "poi")

        #(center, bbox)  = LocalSearch(city)

        #response = "You can find the places in the map at {}, {}.".format(lng,lat)
        #dispatcher.utter_message(response)

        if len(centers) < 5:
            center0 = centers[0]                

            lng0 = center0[0]
            lat0 = center0[1]

            dispatcher.utter_message(
                template ="utter_user_details",            
                lng0 = lng0,
                lat0 = lat0,
                city = city            
            )
        else: 
            center0 = centers[0]
            center1 = centers[1] 
            center2 = centers[2] 
            center3 = centers[3] 
            center4 = centers[4]                     

            lng0 = center0[0]
            lat0 = center0[1]
            lng1 = center1[0]
            lat1 = center1[1]
            lng2 = center2[0]
            lat2 = center2[1]
            lng3 = center3[0]
            lat3 = center3[1]
            lng4 = center4[0]
            lat4 = center4[1]

            #response = "You can find the places in the map at {}, {}.".format(lng,lat)
            #dispatcher.utter_message(response)

            dispatcher.utter_message(
                template ="utter_user_details",            
                lng0 = lng0,
                lat0 = lat0,
                lng1 = lng1,
                lat1 = lat1,
                lng2 = lng2,
                lat2 = lat2,
                lng3 = lng3,
                lat3 = lat3,
                lng4 = lng4,
                lat4 = lat4,
                city = search            
            )

        #return [SlotSet('location', None)]   
        return []
        
        


  

        
'''
if __name__ == "__main__":
  #city = 'Delhi'
  #temperature=Weather(city)['temp']
  #print(temperature)
  run.ActionCheckWeather()
'''



'''
if __name__ == "__main__":
  app.run(debug=True)
  ActionSearchPlaces()
'''  