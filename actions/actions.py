# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
def price(company):


    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey=31CJKLU0PE8QLM7X'.format(company)
    r = requests.get(url)
    data = r.json()
    s=[]
    s=list(data['Time Series (5min)'])
    #print(s)
    return data['Time Series (5min)'][s[0]]['4. close']

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_price"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         res=tracker.get_slot("company")
         print(res)
         url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey=31CJKLU0PE8QLM7X'.format(res)
         r = requests.get(url)
         data = r.json()

         company=data['bestMatches'][0]['1. symbol']
         print(company)
         temp=price(company)
         print(temp)
       

         dispatcher.utter_template("utter_price",tracker,value=temp)
        

         return []



class ActionHelloWorld2(Action):

     def name(self) -> Text:
         return "action_convert_forex"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         from_currency=tracker.get_slot("from_currency")
         to_currency=tracker.get_slot("to_currency")
         print(from_currency)
         print(to_currency)
         url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=31CJKLU0PE8QLM7X'.format(from_currency,to_currency)
         r = requests.get(url)
         data = r.json()

        
         money=tracker.get_slot("money")
         print(type(money))
         print(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
         print(float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']))
         finalvalue= float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])*float(money)
         SlotSet("money",finalvalue)
         SlotSet("from_currency",to_currency)


         dispatcher.utter_template("utter_forex",tracker,finalvalue=finalvalue)
        

         return []

class ActionHelloWorld3(Action):

     def name(self) -> Text:
         return "action_convert_forex_again"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         from_currency=tracker.get_slot("from_currency")
         to_currency=tracker.get_slot("to_currency")
         print(from_currency)
         print(to_currency)
         url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=31CJKLU0PE8QLM7X'.format(from_currency,to_currency)
         r = requests.get(url)
         data = r.json()
         print("iam here")

        
         money=tracker.get_slot("money")
         print(type(money))
         print(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
         print(float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']))
         finalvalue= float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])*float(money)
         SlotSet("money",finalvalue)
         SlotSet("from_currency",to_currency)


         dispatcher.utter_template("utter_forex_again",tracker,nextvalue=finalvalue)
        

         return []