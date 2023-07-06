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
from rasa_sdk.events import SlotSet, FollowupAction, Restarted, AllSlotsReset
#from weather import Weather
from utils.helper import LocalSearch
from utils.helper import Weather



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


class ActionMenu(Action):

    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("inside action menu")        
        dispatcher.utter_message(template="utter_show_menu")
        #return [SlotSet('LOC', None), SlotSet('GPE', None), SlotSet('location', None), SlotSet('poi', None)]
        return [AllSlotsReset(), Restarted()]
        #return []

class ActionWeome(Action):

    def name(self) -> Text:
        return "action_welcome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("inside action menu")        
        dispatcher.utter_message(template="utter_welcome")
        return [SlotSet('LOC', None), SlotSet('GPE', None), SlotSet('location', None), SlotSet('poi', None)]

class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("inside action menu")        
        dispatcher.utter_message(template="utter_goodbye")
        return [SlotSet('LOC', None), SlotSet('GPE', None), SlotSet('location', None), SlotSet('poi', None)]                
  

class ActionGoodMorning(Action):

    def name(self) -> Text:
        return "action_greet_timeofday"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        now = datetime.now()
        hour = int(now.strftime('%H'))
        if(hour>=0 and hour<12):
            response = "Hi! Good Morning\n"
            #print("Hi! Good Morning")
        elif(hour>=12 and hour<=17):
            response = "Hi! Good Afternoon\n"
            #print("Hi! Good Afternoon")
        if (hour>=17 and hour<24):
            response = "Hi! Good Evening\n"
            #print("Hi! Good Evening")            
        
        dispatcher.utter_message(text=response)
        dispatcher.utter_message(template="utter_show_menu")
        return []    
        #return [FollowupAction(name = "action_menu")]


class ActionCheckWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot('GPE')
        if city is None:
            city = tracker.get_slot('LOC')
        if city is None:
            city = tracker.get_slot('location')              

        if city:

            temperature = Weather(city)['temp']
            #humidity = Weather(city)['humidity']
            #wind_mph = Weather(city)['speed']

            response = "The current temperature at {} is {} degree Celsius.".format(city, temperature)
            
            if (temperature > 27):
                response+= " \nOutside is hot.\n"
            else:
                response+= " \nOutside is cold.\n"
                        

            dispatcher.utter_message(response)        

            #return [SlotSet('location', city)]
        
            #return [FollowupAction(name: "action_weather_humidity", timestamp: Optional[float] = None)]
            return [FollowupAction(name = "action_weather_humidity")]
        else:
            dispatcher.utter_message(template="utter_invalid_city_found")
            return [FollowupAction(name = "action_menu")]
        #return []
        
   
class ActionCheckHumidity(Action):

    def name(self) -> Text:
        return "action_weather_humidity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot('GPE')

        if city is None:
            city = tracker.get_slot('LOC')
        if city is None:
            city = tracker.get_slot('location')             

        #city = city.lower() 
        #city_found = (city == "goa")
        #if city_found == True:

            #temperature = Weather(city)['temp']
        humidity = Weather(city)['humidity']
        #wind_mph = Weather[]'wind']['speed']

        response = "\nThe current humidity at {} is {} %.".format(city, humidity)
        dispatcher.utter_message(response)
        #dispatcher.utter_message(template="utter_flow_complete", flow = "1")

        return [SlotSet('GPE', None), FollowupAction(name = "action_menu")]
        #return [FollowupAction(name = "action_menu")]
        #else:
             #dispatcher.utter_message(template="utter_invalid_city_found")

        #return [SlotSet('city_found', city_found)]             

 


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
        
        city = tracker.get_slot('GPE')
        if city is None:
            city = tracker.get_slot('LOC')
        if city is None:
            city = tracker.get_slot('location')             

        if city:

            poi = tracker.get_slot('poi')
            #poi = "beaches"
            #print(poi)
            
            if poi == None:        
                search1 = "place" + " around " + city
                # features is a list  that contains centers (having list of values) around the search place
                centers =  LocalSearch(search1, "Goa", "place%2Cpoi%2Clocality")
        
                #center_list = [i['center'] for i in features]
                '''
                center_list = []
                
                for i in features:
                    d = []
                    d['center'] = i['center']
                    center_list.append(d['center'])
                '''            
            else:
                search = poi + " around " + city
                centers =  LocalSearch(search, "Goa", "place%2Cpoi%2Clocality")

                #(center, bbox)  = LocalSearch(city)
                #center_list = []    
                # center_list is a list if lists (each having 2 values)
            if len(centers) == 0:   
                dispatcher.utter_message(template="utter_invalid_city_found")
                return [FollowupAction(name = "action_menu")] 

            elif len(centers) < 5:
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
            #return []
    
        else:
            dispatcher.utter_message(template="utter_invalid_city_found")
            #return [FollowupAction(name = "action_menu")]
            #return [SlotSet(city_found, False)] 
        #return [SlotSet('city_found', city_found)]
        #dispatcher.utter_message(template="utter_show_menu")
        #return [SlotSet('LOC', None), SlotSet('GPE', None), SlotSet('poi', None), FollowupAction(name = "action_menu")]
        return [FollowupAction(name = "action_menu")]


'''
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

'''        
        
        


  

        
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