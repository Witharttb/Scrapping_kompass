from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from pathlib import Path
import time
from pprint import pprint
from PIL import Image
import pandas as pd

url = 'https://ae.kompass.com/a/furniture-and-linen/15/page-2/'

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get(url)

time.sleep(30)

soup = BeautifulSoup(driver.page_source, features="html.parser")
main_table = soup.find('div', id='resultatDivId')
cards = main_table.find_all('div', class_='product-list-data')

DOMEN = 'https://ae.kompass.com'
name = []
links = []
country = []
text = []
supplier_of = []
phone = []
web = []

for i in range(1, 6):
    url = f'https://ae.kompass.com/a/furniture-and-linen/15/page-{i}/'
    driver.get(url)

    for card in cards:
        name.append(card.span.text)
        links.append(DOMEN + card.a['href'])
        country.append(card.find('div', class_='col-left').span.text.strip())
        try:
            text.append(card.find('span', class_='text').text.strip())
        except:
            text.append('пусто')
        supplier_of.append('\n'.join([text.text.strip() for text in card.ul.find_all('li')]))
        phone.append(card.find('div', class_='collapse freePhone').text.strip())
        try:
            web.append(card.find('div', class_='companyWeb').a['href'])
        except:
            web.append('пусто')

    print('поспим 5 секунд')
    time.sleep(5)

diction = {
    'name': name,
    'links': links,
    'country': country,
    'text': text,
    'supplier_of': supplier_of,
    'phone': phone,
    'web': web,
}