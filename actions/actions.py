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
import sqlite3
import random
import geocoder
from fuzzywuzzy import process

def price(company):



    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey=3JRG5VREY5BWKEX4'.format(company)
    r = requests.get(url)
    data = r.json()
    c=list(data['Time Series (Daily)'])
    #print(s)
    return data['Time Series (Daily)'][c[0]]['4. close']

def get_ticker(res):
         url = 'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&search={}&active=true&limit=2&apiKey=QaOyhDuUX8posM1cMva5_WSeO5F0xvAg'.format(res)
         r = requests.get(url)
         data = r.json()
         return data['results'][0]['ticker']

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_price"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         res=tracker.get_slot("company")
         SlotSet("company",res)
         print(res)


         company=get_ticker(res)
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

        
         print("convert forex");
        
         from_currency=tracker.get_slot("from_currency")
         to_currency=tracker.get_slot("to_currency")
         print(from_currency)
         print(to_currency)
         url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=31CJKLU0PE8QLM7X'.format(from_currency,to_currency)
         r = requests.get(url)
         data = r.json()

        
         money=int(tracker.get_slot("money"))

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
        
         print("iam in forex again")
         from_currency=tracker.get_slot("from_currency")
         to_currency=tracker.get_slot("to_currency")
         print(from_currency)
         print(to_currency)
         url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=31CJKLU0PE8QLM7X'.format(from_currency,to_currency)
         r = requests.get(url)
         data = r.json()
         print("iam in forex again")

        
         money=tracker.get_slot("money")
         print(type(money))
         print(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
         print(float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']))
         finalvalue= float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])*float(money)
         SlotSet("money",finalvalue)
         SlotSet("from_currency",to_currency)


         dispatcher.utter_template("utter_forex_again",tracker,nextvalue=finalvalue)
        

         return []


class ActionHelloWorld4(Action):

    def name(self) -> Text:
        return "action_insert_stock"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print("iam inside insert stock")
        company=tracker.get_slot("company")
        number=tracker.get_slot("number_stocks")   

        print("in query")
        print(type(number))
        print(number)
        print(company)
        SlotSet("company",company)
        symbol=get_ticker(company)    
        conn = DbQueryingMethods.create_connection(db_file="portfolio.sl3");
        DbQueryingMethods.enter_value_transaction(conn,company,symbol,int(number))
        dispatcher.utter_template("utter_confirmation",tracker)
        return []

class ActionHelloWorld5(Action):

    def name(self) -> Text:
        return "action_insert_number_stock"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print("iam inside number of stock")
        number=tracker.get_slot("number_stocks")
        company=tracker.get_slot("company")
        confirm=tracker.get_slot("confirm")
        print(confirm)
        if confirm.upper()=="YES":

           
           print("in query")
           print(type(number))
           print(number)
           print(company)
           symbol=get_ticker(company)
           conn = DbQueryingMethods.create_connection(db_file="portfolio.sl3");
           DbQueryingMethods.enter_value_transaction(conn,company,symbol,int(number))
           dispatcher.utter_template("utter_confirmation",tracker)
        
        else:
            dispatcher.utter_template("utter_not_added",tracker)

        return []

class ActionHelloWorld6(Action):

    def name(self) -> Text:
        return "action_find_total_assets"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print("iam inside number of stock")
      
        conn = DbQueryingMethods.create_connection(db_file="portfolio.sl3");
        sum=DbQueryingMethods.find_total(conn)
        dispatcher.utter_template("utter_sum",tracker,sum=sum)
        return []

class ActionHelloWorld8(Action):

    def name(self) -> Text:
        return "action_find_number_stock"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print("iam inside number of stock")
        comp=tracker.get_slot("company");
      
        conn = DbQueryingMethods.create_connection(db_file="portfolio.sl3");
        sum=DbQueryingMethods.stock_amount(conn,comp)
        print(sum)
        dispatcher.utter_template("utter_stock_amount",tracker,amount=sum[0][0])
        return []



class ActionHelloWorld7(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = "https://api.geoapify.com/v1/ipinfo?apiKey=95d0380f0a4c42e7a845168b0636d84e"
          
        response = requests.get(url)
        s=response.json()
        print(s['location'])

        url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=f825344b0cf0672c689378549f9868db".format(s['location']['latitude'],s['location']['longitude'])
        r = requests.get(url)
        data = r.json()
        print(data)
        a=1.8*(data['main']['temp']-273)+32
        a=round(a,2)
      
        dispatcher.utter_template("utter_weather",tracker,weather=a)


        return []

class ActionHelloWorld9(Action):

    def name(self) -> Text:
        return "action_find_total_value"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        comp=tracker.get_slot("company")
      
        conn = DbQueryingMethods.create_connection(db_file="portfolio.sl3");
        sum=DbQueryingMethods.stock_total_amount(conn,comp)
        sum=round(sum,2)
        dispatcher.utter_template("utter_total_sum",tracker,sum=sum)
        return []

class ActionHelloWorld21(Action):

    def name(self) -> Text:
        return "action_show_portfolio"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        
      
        conn = DbQueryingMethods.create_connection(db_file="portfolio.sl3");
        sum=DbQueryingMethods.show_portfolio(conn,dispatcher)

        return []

class ActionHelloWorldtry(Action):

    def name(self) -> Text:
        return "action_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        print("Iam in confirmation")
        number=tracker.get_slot("number_stocks")
        company=tracker.get_slot("company")    
        dispatcher.utter_template("utter_confirmation_transaction",tracker,company=company,number=number)


        return []

class ActionHelloWorlddesc(Action):

    def name(self) -> Text:
        return "action_get_description"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        print("Iam in desc")
        
        company=tracker.get_slot("company")  
        res=get_ticker(company)
        url='https://api.polygon.io/v3/reference/tickers/{}?apiKey=QaOyhDuUX8posM1cMva5_WSeO5F0xvAg'.format(res)
        r = requests.get(url)
        data = r.json()
        desc=data['results']['description']  
        dispatcher.utter_template("utter_desc",tracker,company=company,desc=desc)


        return []

class ActionHelloWorldgetmetric(Action):

    def name(self) -> Text:
        return "action_get_metric"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
      
        
        company=tracker.get_slot("company")  
        res=get_ticker(company)
        confirm=tracker.get_slot("confirm")
        print(confirm)
        if confirm.upper()=="YES":
              dispatcher.utter_template("utter_def_metric",tracker)
        

        url='https://api.polygon.io/v1/indicators/rsi/{}?timespan=day&adjusted=true&window=14&series_type=close&order=desc&apiKey=QaOyhDuUX8posM1cMva5_WSeO5F0xvAg'.format(res)
        r = requests.get(url)
        data = r.json()
        rsi=data['results']['values'][0]['value']
        rsi=round(rsi,2) 
        dispatcher.utter_template("utter_metric",tracker,rsi=rsi,company=company)


        return []

class DbQueryingMethods:
    def create_connection(db_file):
        """ 
        create a database connection to the SQLite database
        specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def select_by_slot(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute(f'''SELECT (output) FROM trial
                    WHERE Name="Abhishek"''')

        # return an array
        rows = cur.fetchall()

        return(rows)

    def enter_value_transaction(conn,stock_name,stock_symbol,amount):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("INSERT INTO portfolio(stock_name,stock_symbol,amount)  VALUES (?,?,?)",(stock_name,stock_symbol,amount))
        
    
        conn.commit()
        print(cur.rowcount, "Record inserted successfully into Laptop table")
        cur.close()

        return;

    def find_total(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        sum=0.00
        cur = conn.cursor()
        cur.execute(f'''SELECT * FROM portfolio''')
        rows = cur.fetchall()
        for x in rows:
            print(x)
            symb=x[1]
            val=x[2]
            print(symb);
            print(type(symb))
            print(val)
            print(type(val))

            temp=price(symb)
            sum=val*float(temp)+sum

            print("row")
        cur.close()
        print(sum)

        return sum;

    def stock_amount(conn,comp):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute(f'''SELECT (amount) FROM portfolio
                    WHERE UPPER(stock_name)=UPPER("{comp}")''')

        # return an array
        rows = cur.fetchall()

        return(rows)

    def stock_total_amount(conn,comp):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute(f'''SELECT * FROM portfolio
                    WHERE UPPER(stock_name)=UPPER("{comp}")''')

        # return an array
        rows = cur.fetchall()
        print(rows[0][1])
        k=price(rows[0][1])
        print(rows[0][2])
        sum=float(k)*rows[0][2]
        print(sum)

        return sum

    def show_portfolio(conn,dispatcher):
        cur = conn.cursor()
        cur.execute(f'''SELECT * FROM portfolio''')    
        rows = cur.fetchall()
        for x in rows: 
              dispatcher.utter_message(f"{x[0]},{x[1]},{x[2]}")

        return;

