from bs4 import BeautifulSoup
import urllib.request
url = "https://dining.rochester.edu/locations/douglass-dining/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, features="lxml")
time = soup.findAll("div",{"class":"c-tab is-active"})
food = {"chicken", "beef", "egg", "sausage", "pork", "cream", "fish", "salmon", "talapia"}
for x in time:
    for liclass in x.findAll("li",{"class":"menu-item-li"}):
        string = liclass["data-searchable"]
        if any(x in string.lower() for x in food):
            print(liclass.a.text)