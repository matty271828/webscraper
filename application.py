from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
import os

# Change this to your own chromedriver path!
chromedriver_path = os.environ.get("chromedriver_path")

# This will open the Chrome window
driver = webdriver.Chrome(executable_path=chromedriver_path) 
sleep(2)

def start_kayak(city_from, city_to, date_start, date_end):
    """City codes - it's the IATA codes!
    Date format -  YYYY-MM-DD"""
    # Contact Kayak
    try:
        kayak = ('https://www.kayak.com/flights/' + city_from + '-' + city_to +
                '/' + date_start + '-flexible/' + date_end + '-flexible?sort=bestflight_a')
        driver.get(kayak)
        print("Kayak successfully contacted")
        sleep(randint(8,10))
    except:
        print("Error contacting Kayak")
        return 0

    # sometimes a popup shows up, so we can use a try statement to check it and close
    try:
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[5].click()
    except Exception as e:
        pass
    sleep(randint(1,5))

    print('starting first scrape.....')
    df_flights_best = page_scrape()
    print(df_flights_best)
    sleep(randint(60,80))

def page_scrape():
    """This function takes care of the scraping part"""
    return 1

# city_from = input('From which city? ')
# city_to = input('Where to? ')
# date_start = input('Search around which departure date? Please use YYYY-MM-DD format only ')
# date_end = input('Return when? Please use YYYY-MM-DD format only ')

city_from = 'MAN'
city_to = 'TLV'
date_start = '2021-06-06'
date_end = '2021-06-10'

start_kayak(city_from, city_to, date_start, date_end)