import requests, bs4
from time import sleep, strftime
from random import randint
import os

def contact_kayak(city_from, city_to, date_start, date_end):
    """City codes - it's the IATA codes!
    Date format -  YYYY-MM-DD"""
    # Contact Kayak
    try:
        url = ('https://www.kayak.com/flights/' + city_from + '-' + city_to + '/' + date_start + '-flexible/' + date_end + '-flexible?sort=bestflight_a')
        response = requests.get(url)
        response.raise_for_status()
        print(f'Kayak successfully contacted: {response.status_code}')

    except requests.RequestException:
        print(f'Site connection error: {response.status_code}')
        return None

    print('starting scrape.....')
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    return soup

def page_scrape(city_from, city_to, date_start, date_end):
    """This function takes care of the scraping part"""
    soup = contact_kayak(city_from, city_to, date_start, date_end)
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