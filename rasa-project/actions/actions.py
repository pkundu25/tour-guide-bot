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
import requests
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from weather import Weather


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

        return [SlotSet('location', city)]  

        
'''
if __name__ == "__main__":
  #city = 'Delhi'
  #temperature=Weather(city)['temp']
  #print(temperature)
  run.ActionCheckWeather()
'''