import os

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from slugify import slugify

options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)


def crname(url):
    q = url.rfind('/')
    stq = url[q + 1:]

    return stq


link = 'https://rant.ru/catalog/kolyaska-universalnaya-2-v-1-riko-basic-bella.html'

#
# driver.get("https://rant.ru/catalog/modulnye-kolyaski-2-v-1/")
#
# s3 = driver.find_element_by_xpath('//*[@id="catalog_sorter"]/ul[2]/li[2]/a')
#
# s3.click()
#
# S4 = driver.find_element_by_css_selector(
#     "#catalog_sorter > ul.sorter__limit.nav-tabs > li.active.dropdown.open > ul > li:nth-child(4)")
#
# S4.click()
#
# for product in driver.find_elements_by_class_name("catalog_item__pic"):
#     product_link = product.get_attribute("href")
#
#     print(product_link)
#
#     driver.get(product_link)

driver.get(link)

e = crname(link)

if e.endswith('.html'):
    e = e[:-5]

path = '/home/enk/projects/jo/pic/' + e

try:
    os.mkdir(path)
except OSError:
    print("Создать директорию %s не удалось" % path)
else:
    print("Успешно создана директория %s " % path)

name = driver.find_element_by_xpath('//*[@id="bx_117848907_34674"]/div[1]/div/h1').text

select = Select(driver.find_element_by_xpath('//*[@id="bx_117848907_34674"]/div[3]/div/div[1]/div[1]/div/select'))

for index in range(len(select.options)):
    select = Select(driver.find_element_by_xpath('//*[@id="bx_117848907_34674"]/div[3]/div/div[1]/div[1]/div/select'))
    select.select_by_index(index)
    r = select.options
    sl = slugify(r[index].text)
    print(sl)

    newPath = path + '/' + sl

    try:
        os.mkdir(newPath)
    except OSError:
        print("Создать директорию %s не удалось" % newPath)
    else:
        print("Успешно создана директория %s " % newPath)

    pic = driver.find_elements_by_class_name('picbox__img')
    arr = []
    for pi in pic:
        # btn = driver.find_element_by_class_name('owl-dot').click()
        btns = pi.get_attribute("src")
        # btns = driver.find_elements_by_class_name('owl-dot')
        # pi.click()
        # time.sleep(1)
        if not btns in arr:
            arr.append(btns)

    # src = driver.find_element_by_xpath('//*[@id="bx_117848907_34674"]/div[2]/div/div/div/div[2]')
    #
    # print(src)

    for url in arr:

        with open(newPath + '/' + crname(url), 'wb') as handle:
            response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

# path = os.getcwd()
# print("Текущая рабочая директория %s" % path)


driver.close()
