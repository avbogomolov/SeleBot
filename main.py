from selenium import webdriver
import time
import datetime
import random
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys

# Start of countdown
start_time = time.time()

url = 'https://ironchampion.ru'

# Def generation random link of site
def random_link(url_site):
    response = requests.get(url_site)
    # Парсим HTML содержимое
    soup = BeautifulSoup(response.text, 'html.parser')
    # Находим все ссылки на странице
    links = soup.find_all('a', href=True)
    # Рандомно выбираем одну из ссылок
    only_link = random.choice(links)
    best_link = only_link['href']
    return best_link


def random_delay():
    return int(random.randint(1, 30))


element_1 = 'colophon'
element_2 = 'menu-item-565'
yandex_rtb = "yandex_rtb_R-A-412676-1"


def open_site_firefox(a):
    browser = webdriver.Firefox()
    browser.get(a)
    try:
        browser.find_element(By.ID, element_1).click()
        print(f'Firefox ---- {element_1} ')
        for i in range(3000):
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)
        time.sleep(random_delay())
    except:
        print(f'Firefox dont finded  {element_1}')
    try:
        browser.find_element(By.ID, element_2).click()
        print(f'Firefox ---- {element_2} ')
        for i in range(3000):
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)
        time.sleep(random_delay())
    except:
        print(f'Firefox dont finded  {element_2}')
    try:
        browser.find_element(By.ID, yandex_rtb)
        print(f'Firefox ---- {yandex_rtb} ')
        for i in range(3000):
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)
        time.sleep(random_delay())
    except:
        print(f'Firefox dont finded  {yandex_rtb}')
    browser.quit()


def open_site_chrome(a):
    browser = webdriver.Chrome()
    browser.get(a)
    try:
        browser.find_element(By.ID, element_1).click()
        print(f'Chrome ---- {element_1} ')
        for i in range(3000):
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)
        time.sleep(random_delay())
    except:
        print(f'Chrome dont finded  {element_1}')
    try:
        browser.find_element(By.ID, element_2).click()
        print(f'Chrome ---- {element_2} ')
        for i in range(3000):
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)
        time.sleep(random_delay())
    except:
        print(f'Chrome dont finded  {element_2}')
    try:
        browser.find_element(By.ID, yandex_rtb)
        print(f'Chrome ---- {yandex_rtb} ')
        for i in range(3000):
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)
        time.sleep(random_delay())
    except:
        print(f'Chrome dont finded  {yandex_rtb}')
    browser.quit()


open_site_firefox(random_link(url))
open_site_chrome(random_link(url))




current_data = datetime.datetime.now().strftime('%m/%d/%Y %H:%M')

# End of countdown
end_time = time.time()

# Calculating execution time
execution_time = round(end_time - start_time, 2)

print(f"Code execution time: {execution_time} sec")
print(f'Current data is: {current_data}')
