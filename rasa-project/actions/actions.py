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
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
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

'''
class ActionCheckWeather(Action):

    def name(self)-> Text:
        return "action_weather"
    
    def run(self, dispatcher, tracker, domain):
        #api_key = 'Your API Key'
        api_key = "e77820355cbac076ad2f89e8bb738ca5" 
        loc = tracker.get_slot('location')
        #current = requests.get('https://api.openweathermap.org/data/2.5/weather?id=524901&q={}&appid={}'.format(loc, api_key)).json()
        current = requests.get('http://api.openweathermap.org/data/2.5/weather?&q={}&appid={}'.format(loc, api_key)).json()
        print(current)
        country = current['sys']['country']
        city = current['name']
        condition = current['weather'][0]['main'    ]
        temperature_c = current['main']['temp']
        humidity = current['main']['humidity']
        wind_mph = current['wind']['speed']
        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]     

'''


class ActionCheckWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        temperature = Weather(city)['temp']
        response = "The current temperature at {} is {} degree Celsius.".format(city,temperature)
        dispatcher.utter_message(response)

        return [SlotSet('location', city)]

'''    
    
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")#
        return []    
    
'''

'''
if __name__ == "__main__":
  #city = 'Delhi'
  #temperature=Weather(city)['temp']
  #print(temperature)
  run.ActionCheckWeather()
'''  