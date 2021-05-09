import requests, bs4
from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import os

# Change this to your own chromedriver path!
chromedriver_path = os.environ.get("chromedriver_path")

# Add options for webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# Configure webdriver
driver = webdriver.Chrome(chromedriver_path, options=options)

def contact_kayak(city_from, city_to, date_start, date_end):
    """City codes - it's the IATA codes!
    Date format -  YYYY-MM-DD"""
    # Contact Kayak
    try:
        url = ('https://www.kayak.com/flights/' + city_from + '-' + city_to + '/' + date_start + '-flexible/' + date_end + '-flexible?sort=bestflight_a')
        driver.get(url)
        print("Kayak contacted...")
        return driver.page_source

    except:
        print("Error contacting Kayak")
        return None

def page_scrape(city_from, city_to, date_start, date_end):
    """This function takes care of the scraping part"""
    # Print statement to user
    print('starting scrape.....')
    
    # Run contact_kayak to retrieve page source
    page_source = contact_kayak(city_from, city_to, date_start, date_end)

    soup = bs4.BeautifulSoup(page_source, features="html.parser")

    print(soup)

    prices = soup.find_all('span', class_="price-text")
    print(prices)
    return 1

# city_from = input('From which city? ')
# city_to = input('Where to? ')
# date_start = input('Search around which departure date? Please use YYYY-MM-DD format only ')
# date_end = input('Return when? Please use YYYY-MM-DD format only ')

city_from = 'MAN'
city_to = 'TLV'
date_start = '2021-06-06'
date_end = '2021-06-10'

page_scrape(city_from, city_to, date_start, date_end)