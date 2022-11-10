from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from pathlib import Path
import time
from pprint import pprint
from PIL import Image
import pandas as pd


def main():
    url = 'https://lenta.com/catalog/'
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = uc.Chrome(options=options)
    driver.get(url)

    time.sleep(30)


if __name__ == '__main__':
    main()

#
# soup = BeautifulSoup(driver.page_source, features="html.parser")
# main_table = soup.find('div', id='resultatDivId')
# cards = main_table.find_all('div', class_='product-list-data')
#
# DOMEN = 'https://ae.kompass.com'
# name = []
# links = []
# country = []
# text = []
# supplier_of = []
# phone = []
# web = []
#
# for i in range(1, 6):
#     url = f'https://ae.kompass.com/a/furniture-and-linen/15/page-{i}/'
#     driver.get(url)
#
#     for card in cards:
#         name.append(card.span.text)
#         links.append(DOMEN + card.a['href'])
#         country.append(card.find('div', class_='col-left').span.text.strip())
#         try:
#             text.append(card.find('span', class_='text').text.strip())
#         except:
#             text.append('пусто')
#         supplier_of.append('\n'.join([text.text.strip() for text in card.ul.find_all('li')]))
#         phone.append(card.find('div', class_='collapse freePhone').text.strip())
#         try:
#             web.append(card.find('div', class_='companyWeb').a['href'])
#         except:
#             web.append('пусто')
#
#     print('поспим 5 секунд')
#     time.sleep(5)
#
# diction = {
#     'name': name,
#     'links': links,
#     'country': country,
#     'text': text,
#     'supplier_of': supplier_of,
#     'phone': phone,
#     'web': web,
# }


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = uc.Chrome(options=options)

# url = 'https://lenta.com/catalog/chajj-kofe-kakao/?page=2'
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
# time.sleep(4)
# last_page_num = int(soup.find_all('li', class_='pagination__item')[-1].text)

all_in_one = []
brend = []
gacategory = []
description = []
cardPrice = []
regularPrice = []
sku = []
link_small_img = []
many = []
stockValue = []
storeAddress = []
title = []
subTitle = []
img_urls = []
link = []

links = []

last_page_num = 37

for page_num in range(1, last_page_num + 1):

    url = f'https://lenta.com/catalog/chajj-kofe-kakao/?page={page_num}'
    print(url)
    try:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        links += [item.a['href'] for item in soup.find_all('div', class_='sku-card-small-container')]
    except:
        pass

# links = sorted(set(links))
print(f'Найдено {len(links)} товаров')

with open("links.txt", "w") as output:
    output.write(str(links))

for idx, url in enumerate(links):
    if idx == 20:
        break
    print(f'{idx + 1} из {len(links)}  {url})

    try:
        driver.get(urls)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        all_in_one.append('\n'.join([item['key'] + ' : ' + item['value'] for item in properties]))
        brend.append(json_file['brand'])
        gacategory.append(json_file['gaCategory'])
        description.append(json_file['description'])
        cardPrice.append(json_file['cardPrice']['value'])
        regularPrice.append(json_file['regularPrice']['value'])
        sku.append(json_file['code'])
        link_small_img.append(json_file['shareSkuMetaImageUrl'])
        many.append(json_file['stock'])
        stockValue.append(json_file['stockValue'])
        storeAddress.append(json_file['storeAddress'])
        title.append(json_file['title'])
        subTitle.append(json_file['subTitle'])
        img_urls.append(', '.join([item['full'] for item in json_file['imageUrls']]))
    except:
        print('Error')
        nothing = 'missing'
        all_in_one.append(nothing)
        brend.append(nothing)
        gacategory.append(nothing)
        description.append(nothing)
        cardPrice.append(nothing)
        regularPrice.append(nothing)
        sku.append(nothing)
        link_small_img.append(nothing)
        many.append(nothing)
        stockValue.append(nothing)
        storeAddress.append(nothing)
        title.append(nothing)
        subTitle.append(nothing)
        img_urls.append(nothing)
    link.append(url)

    from bs4 import BeautifulSoup
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import undetected_chromedriver as uc
    import time
    from pprint import pprint
    import pandas as pd
    import requests
    import json
    import ast

    domen = 'https://lenta.com'
    options = webdriver.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')
    # options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.get(domen)
    # address = driver.find_element_by_class_name("address-container__adress-location").click()
    # button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div/div[3]/button[1]').click()
    # inpt = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div[1]/div/div/input').click()
    # inpt.clear()
    # inpt.send_keys('бугры')

    # domen = 'https://lenta.com'
    # options = webdriver.ChromeOptions()
    # options.add_argument('--blink-settings=imagesEnabled=false')
    # # options.add_argument("--headless")
    # driver = uc.Chrome(options=options)

    all_links = [
        'https://lenta.com/catalog/bakaleya/',
        #     'https://lenta.com/catalog/chajj-kofe-kakao/',
        #     'https://lenta.com/catalog/zdorovoe-pitanie/',
        #     'https://lenta.com/catalog/krasota-i-zdorove/',
        #     'https://lenta.com/catalog/bytovaya-himiya/',
        #     'https://lenta.com/catalog/sport-i-aktivnyjj-otdyh/',
        #     'https://lenta.com/catalog/tovary-dlya-zhivotnyh/',
        #     'https://lenta.com/catalog/lenta-zoomarket---professionalnyjj-uhod/',
        #     'https://lenta.com/catalog/avtotovary/',
    ]

    for i, url in enumerate(all_links):
        #     if i == 3:
        #         break
        print(f'{i + 1} из {len(all_links)}  {url}')

        file_name_txt = f"{url.split('/')[-2]}.txt"
        file_name_xlsx = f"{url.split('/')[-2]}.xlsx"

        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        time.sleep(4)
        last_page_num = int(soup.find_all('li', class_='pagination__item')[-1].text)

        links = []

        last_page_num = 155

        for page_num in range(1, last_page_num + 1):
            url2 = f'{url}?page={page_num}'
            print(url2)
            try:
                driver.get(url2)
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 1000)")
                time.sleep(0.5)

                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                links += [domen + item.a['href'] for item in soup.find_all('div', class_='sku-card-small-container')]
                print(len(links))
                if len(links) == 0:
                    break
            except:
                pass

        links = sorted(set(links))
        print(f'Найдено {len(links)} товаров')

        with open(file_name_txt, "w") as f:
            f.write(str(links))

        all_in_one = []
        brend = []
        gacategory = []
        description = []
        cardPrice = []
        regularPrice = []
        sku = []
        link_small_img = []
        many = []
        stockValue = []
        storeAddress = []
        title = []
        subTitle = []
        img_urls = []
        link = []

        #     with open(file_name_txt, "r") as f:
        #         links = ast.literal_eval(f.read())

        for idx, url in enumerate(links):
            #         if idx == 3:
            #             break
            print(f'{idx + 1} из {len(links)}  {url}')
            try:
                driver.get(url)
                time.sleep(0.5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                json_file = json.loads(
                    soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])

                properties = json_file['attributesGroups'][0]['properties']
                all_in_one.append('\n'.join([item['key'] + ' : ' + item['value'] for item in properties]))
                brend.append(json_file['brand'])
                gacategory.append(json_file['gaCategory'])
                description.append(json_file['description'])
                cardPrice.append(json_file['cardPrice']['value'])
                regularPrice.append(json_file['regularPrice']['value'])
                sku.append(json_file['code'])
                link_small_img.append(json_file['shareSkuMetaImageUrl'])
                many.append(json_file['stock'])
                stockValue.append(json_file['stockValue'])
                storeAddress.append(json_file['storeAddress'])
                title.append(json_file['title'])
                subTitle.append(json_file['subTitle'])
                img_urls.append(', '.join([item['full'] for item in json_file['imageUrls']]))
            except Exception as e:
                print('Error', e)
                nothing = 'missing'
                all_in_one.append(nothing)
                brend.append(nothing)
                gacategory.append(nothing)
                description.append(nothing)
                cardPrice.append(nothing)
                regularPrice.append(nothing)
                sku.append(nothing)
                link_small_img.append(nothing)
                many.append(nothing)
                stockValue.append(nothing)
                storeAddress.append(nothing)
                title.append(nothing)
                subTitle.append(nothing)
                img_urls.append(nothing)
            link.append(url)

        try:
            df = pd.DataFrame({

                'Категория': gacategory,
                'Артикул': sku,
                'Наименование': title,
                'Подзаголовок': subTitle,
                'Изображение товара': link_small_img,
                'Ссылка на страницу': link,
                'Обычная цена': regularPrice,
                'Цена по акции': cardPrice,
                'Склад': storeAddress,
                'Кол-во ед': many,
                'Кол-во': stockValue,
                'Описание товара': description,
                'Бренд': brend,
                'Ссылки на фото': img_urls,
                'Характеристики': all_in_one,
            })

            df.to_excel(file_name_xlsx, index=False)

        except Exception as e:
            print('Не удалось сохранить df изза ошибки\n', e)