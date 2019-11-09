from typing import Any, Text, Dict, List
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, timedelta
import requests
"""
"""
def request_time():
    """
    Collect the current time at Rochester using timeanddate.com
    :return: time: time as datetime format
    :return: timestr: time as string fotmat
    """
    url = "https://www.timeanddate.com/worldclock/usa/rochester"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, features="html.parser")
    time = soup.findAll("span", {"id": "ct"})
    date = soup.findAll("span", {"id": "ctdat"})
    timestr = time[0].text.strip()
    date = date[0].text.strip()
    time = datetime.strptime(date+timestr, '%A, %B %d, %Y%I:%M:%S %p')
    timestr = date+" "+timestr
    return time, timestr
def request_dining():
    """
    Collect dining halls that are currently open at UR
    :return: list of open dining halls
    """
    url = "https://dining.rochester.edu/menu-hours/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, features="html.parser")
    #Find all dining locations and opening hours using beautiful soup
    locations = soup.findAll("table", {"class": "open-now-table"})
    dict = {}
    time, timestr = request_time()

    #Add actual opening time and date to the opening hours
    for i, a in enumerate(locations):
        name = a.find('a').text.strip()
        open_hours = a.findAll("span", {"class": "hour open_at"})
        closing_hours = a.findAll("span", {"class": "hour close_at"})
        open = [
            (datetime.strptime(x.text.strip(), "%I:%M %p").replace(year=time.year, month=time.month, day=time.day))
            for x in open_hours]
        close = [
            (datetime.strptime(x.text.strip(), "%I:%M %p").replace(year=time.year, month=time.month, day=time.day))
            for x in closing_hours]
        hours = [list(a) for a in zip(open, close)]
        open1 = datetime(year=time.year, month=time.month, day=time.day, hour=0, minute=0)
        open2 = datetime(year=time.year, month=time.month, day=time.day, hour=4, minute=0)
        for x in hours:
            if (time >= open1 and time <= open2):
                if x[1] <= x[0]:
                    x[0] = x[0] - timedelta(days=1)
            else:
                if x[1] <= x[0]:
                    x[1] = x[1] + timedelta(days=1)
        dict.update({name: hours})
    opens = {}

    #Compare the hours with current time and returns list of opening places
    for location in dict:
        for hours in dict.get(location):
            if (time >= hours[0] and time <= hours[1]):
                opens.update({location: [hours[0], hours[1]]})
    return opens
class ActionDiningHall(Action):

    def name(self) -> Text:
        return "request_open_dininghalls"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        value = next(tracker.get_latest_entity_values("dininghall"), None)
        opens = request_dining()

        if not opens:
            dispatcher.utter_message("Sorry, nothing is open right now :( You must be hungry")
        else:
            if value:
                dininghalls = {"hillside":"Hillside Market", "rockys":"Rocky's Sub Shop", "douglass":"Douglass Dining", "dfo":"Danforth Dining Center", "connections":"Connections'", "southside":"Southside Market"
                               , "grabngo":"Grab & Go", "wilson":"The Pit", "faculty":"Faculty Club", "cave":"The Cave", "optikale":"OptiKale", "peets":"Peet's Coffee @ Wegmans Hall", "peet 's":"Peet's Coffee @ Wegmans Hall",
                               "starbucks":"Starbucks"}
                chosen_place = dininghalls.get(value)
                print(value)
                print(chosen_place)
                if chosen_place in opens:
                    dispatcher.utter_message("Yes, "+chosen_place+" is open, it will close at "+opens.get(chosen_place)[1].strftime("%I:%M %p"))
                else:
                    dispatcher.utter_message("Sorry "+chosen_place+" is not open right now, try another place!")
            else:
                message = ""
                for x in opens:
                    message = message + "- " + x + "\n"
                dispatcher.utter_message("Here are some places to get some food: \n"+message)
        return[]
class ActionDirection(Action):
    def name(self) -> Text:
        return "return_direction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        r = 'http://www.rochester.edu/sba/wp-content/uploads/2018/04/map-to-SBAC-1.jpg'

        dispatcher.utter_template("utter_sorry", tracker, image=r)
        return []
class ActionCoffee(Action):
    def name(self):
        return "request_coffee"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        cafe = ["Hillside Market", "Connections", "Grab & Go", "The Pit", "Peet's Coffee @ Wegmans Hall","Starbucks"]
        opens = request_dining()
        for x in cafe:
            if not x in opens:
                cafe.remove(x)
        if not cafe:
            dispatcher.utter_message("Sorry, there is no café open right now :(")
        else:
            message = ""
            for x in cafe:
                message = message + "- " + x + "\n"
            dispatcher.utter_message("Here are some places for your caffeine craving: \n"+message)
        return[]

class ActionWeather(Action):
    def name(self):
        return "request_weather"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        value = next(tracker.get_latest_entity_values("weather"), None)
        url = "https://weather.com/weather/tenday/l/14627:4:US"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                                  'AppleWebKit/537.11 (KHTML, like Gecko) '
                                                  'Chrome/23.0.1271.64 Safari/537.11',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                                    'Accept-Encoding': 'none',
                                    'Accept-Language': 'en-US,en;q=0.8',
                                    'Connection': 'keep-alive'})
        soup = BeautifulSoup(urllib.request.urlopen(req), features="lxml")
        des = soup.findAll("td", {"class": "description"})
        des = [x["title"] for x in des]
        if value == "tomorrow":
            dispatcher.utter_message("Here's the weather for tomorrow: "+des[1]);
        else:
            dispatcher.utter_message(des[0])
