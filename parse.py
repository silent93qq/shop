import os
import pprint
import time

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jo.settings')
django.setup()
import requests
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from slugify import slugify
from shop.models import Product, ProductInfo, ProductImage

options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)


def crname(url):
    q = url.rfind('/')
    stq = url[q + 1:]

    return stq


def crdir(newPath):
    try:
        os.mkdir(newPath)
    except OSError:
        pass


link = "https://rant.ru/catalog/modulnye-kolyaski-2-v-1"

driver.get(link)

s3 = driver.find_element_by_xpath('//*[@id="catalog_sorter"]/ul[2]/li[2]/a')
s3.click()

S4 = driver.find_element_by_css_selector(
    "#catalog_sorter > ul.sorter__limit.nav-tabs > li.active.dropdown.open > ul > li:nth-child(4)")
S4.click()

categoryName = '/home/enk/projects/jo/media/' + crname(link)

crdir(categoryName)

time.sleep(4)
urls=[]

for product in driver.find_elements_by_class_name("catalog_item__pic"):

    product_link = product.get_attribute("href")

    urls.append(product_link)

pprint.pprint(len(urls))

for url in urls:

    driver.get(url)

    e = crname(url)

    if e.endswith('.html'):
        e = e[:-5]

    path = categoryName + '/' + e
    DJANGOpath = 'media/' + crname(link) + '/' + e

    crdir(path)

    DJANGOname = driver.find_element_by_css_selector('div:nth-child(1) > div > h1').text
    DJANGOinfo = driver.find_element_by_id('detail_detail').get_attribute('innerHTML')
    DJANGOcharacter = driver.find_element_by_id('detail_props').get_attribute('innerHTML')

    pro = Product.objects.create(
        name=DJANGOname,
        info=DJANGOinfo,
        character=DJANGOcharacter,
        is_active=1,
        created=timezone.now(),
        updated=timezone.now(),
        category_id=1,
    )

    select = Select(driver.find_element_by_xpath('//div[3]/div/div[1]/div[1]/div/select'))

    arrColor = []
    for index in range(len(select.options)):
        select = Select(driver.find_element_by_xpath('//div[3]/div/div[1]/div[1]/div/select'))
        select.select_by_index(index)
        r = select.options
        sl = slugify(r[index].text)
        newPath = path + '/' + sl

        DJANGOcolor = r[index].text

        DJANGOprice = driver.find_element_by_css_selector(
            'div:nth-child(3) > div > div.col-xs-12.col-sm-6.col-md-6.col-lg-5 > div > div.detail__'
            'price.price > div.price__pdv.js-price_pdv-1').text
        DJANGOdisPrice = driver.find_element_by_css_selector(
            'div:nth-child(3) > div > div.col-xs-12.col-sm-6.col-md-6.col-lg-5 > div > div.detail_'
            '_price.price > div.price__pv.js-price_pv-1').text

        ProductInfo.objects.create(
            color=DJANGOcolor,
            price=DJANGOprice,
            priceDis=DJANGOdisPrice,
            created=timezone.now(),
            updated=timezone.now(),
            product_id=pro.id
        )

        crdir(newPath)

        time.sleep(5)
        er = driver.find_element_by_css_selector('div.col-xs-12.col-sm-12.col-md-5.col-lg-5 > div > div > div >'
                                                 ' div.picbox__carousel.owl-loaded.owl-drag.owl-carousel > '
                                                 'div.owl-stage-outer > div.owl-stage')
        item_list = er.find_elements_by_css_selector('div.owl-item')

        gg = []
        for r in item_list:
            img = r.find_element_by_class_name('picbox__img').get_attribute('src')
            jj = r.get_attribute('class')
            if not jj == 'owl-item cloned':
                gg.append({'className': jj, 'urlImg': img})
        print('--------------------------------------------------')
        i = 0
        for url in gg:
            if i == 0:
                picPath = newPath + '/' + crname(url['urlImg'])
                ProductImage.objects.create(
                    image=DJANGOpath + '/'+sl+'/' + crname(url['urlImg']),
                    is_active=1,
                    is_main=1,
                    created=timezone.now(),
                    updated=timezone.now(),
                    product_id=pro.id
                )
                i = 1
            else:
                picPath = newPath + '/' + crname(url['urlImg'])
                ProductImage.objects.create(
                    image=DJANGOpath + '/' + sl + '/' + crname(url['urlImg']),
                    is_active=1,
                    is_main=0,
                    created=timezone.now(),
                    updated=timezone.now(),
                    product_id=pro.id
                )
            with open(picPath, 'wb') as handle:
                response = requests.get(url['urlImg'], stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
