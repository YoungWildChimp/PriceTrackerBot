import csv
import json
import time
import requests

from bs4 import BeautifulSoup
from datetime import datetime
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.by import By
from requests.exceptions import RequestException
from selenium.webdriver.firefox.options import Options

class PriceTrackerBot():

    class Item():

        def __init__(self, index : int, url : str, lowest_price : float, desired_price : float):
            self.url = url
            self.date = None
            self.index = index
            self.lowest_price = lowest_price if lowest_price is not None else float('inf')
            self.desired_price = desired_price

    class Website():

        def __init__(self, index_bis : int, website_name : str, information_price : str, website_rendering : str):
            self.index_bis = index_bis
            self.website_name = website_name
            self.information_price = information_price
            self.website_rendering = website_rendering

    def __init__(self):

        try:
        
            with open("items_list.json") as json_file:

                self.items_data = json.load(json_file)

        except FileNotFoundError:

            print("JSON file is missing")

        self.items_list = []

        for index, i in enumerate(self.items_data):
            
            url = i["url"]
            lowest_price = i["lowest_price"]
            desired_price = i["desired_price"]
            self.items_list.append(self.Item(index = index, url = url, lowest_price = lowest_price, desired_price = desired_price))

        try:
                
            with open("generic_websites_list.csv") as csv_file:
        
                self.website_data = list(csv.reader(csv_file, delimiter = ','))

        except FileNotFoundError:
        
            print("CSV file is missing")

        self.website_list = []

        for index_bis, j in enumerate(self.website_data):
                    
            website_name = j[0]
            information_price = j[1]
            website_rendering = j[2]
            self.website_list.append(self.Website(index_bis = index_bis, website_name = website_name, information_price = information_price, website_rendering = website_rendering))
    
    def Check_Website(self, url : str, website : list[Website]):

        for k in website:
            if k.website_name.lower() in url.lower():
                return k.index_bis

        return None
        
    def Check_Price(self, item : Item):

        Index_ter = self.Check_Website(item.url, self.website_list)
        
        try:

            if "HTML" in self.website_list[Index_ter].website_rendering:

                r = requests.get(item.url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"})

                r_information = BeautifulSoup(r.content, features = "html.parser")

                r_price = r_information.find(class_  = self.website_list[Index_ter].information_price.replace(" ","")).get_text()

            elif "JS" in self.website_list[Index_ter].website_rendering:

                # Using Selenium because AliExpress displays the content of a page via JavaScript

                options = Options()
                options.add_argument("--headless")

                Browser = webdriver.Firefox(options = options)

                Browser.get(item.url)

                r_price = Browser.find_element(By.CLASS_NAME, self.website_list[Index_ter].information_price.replace(" ","")).text

                Browser.quit()

            if r_price is not None:

                self.Check_Price_Lower_or_Desired(item = item, r_price = float(r_price.replace("€","").replace(".", "", r_price.count(".")).replace(",",".")))
        
        except RequestException as err:

            print(f"Request error for {item.url}: {err}")

        except Exception as err:

            print(f"Unknown error for {item.url}: {err}")

    def Check_Price_Lower_or_Desired(self, item : Item, r_price):

        if item.lowest_price > r_price and item.desired_price < r_price:

            self.items_data[item.index]["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.items_data[item.index]["lowest_price"] = r_price
 
            notification.notify("PriceTrackerBot", f"New lowest price for {item.url[:116]} : {r_price}€", timeout = 5)

        if item.desired_price > r_price:

            self.items_data[item.index]["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.items_data[item.index]["lowest_price"] = r_price
            
            notification.notify("PriceTrackerBot", f"Desired price reached for {item.url[:116]} : {r_price}", timeout = 5)

        self.data_update()

    def data_update(self):
        
        with open("items_list.json", "w") as json_file:

            json.dump(self.items_data, json_file, indent = 4)
            
    def run(self, quick_check : bool = False, sleep_duration : int = 21600):

        if quick_check == True:

            for j in self.items_list:
                                    
                self.Check_Price(item = j)

        elif quick_check == False:
        
            while True:

                for j in self.items_list:
                    
                    self.Check_Price(item = j)
                
                notification.notify("PriceTrackerBot", f"Waiting for {sleep_duration // 3600} hours before the next check.", timeout = 5)

                time.sleep(sleep_duration)

        else:

            print("Error")
        
PriceTrackerBot().run(quick_check = True)