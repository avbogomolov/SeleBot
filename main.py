from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def random_delay():
    return int(random.randint(1,30))
def open_site_firefox(site):
    browser = webdriver.Firefox()
    browser.get(site)
    browser.find_element(By.ID, "colophon").click()
    print(f'I found this on {site} the site in the Firefox browser')
    time.sleep(random_delay())
    browser.find_element(By.ID, "menu-item-565").click()
    print(f'2 random time is')
    time.sleep(random_delay())
    browser.quit()

def open_site_chrome(site):
    browser = webdriver.Chrome()
    browser.get(site)
    browser.find_element(By.ID, "colophon").click()
    print('i founded it')
    time.sleep(random_delay())
    browser.find_element(By.ID, "menu-item-565").click()
    time.sleep(random_delay())
    browser.quit()


open_site_firefox('https://ironchampion.ru')

open_site_chrome('https://ironchampion.ru')




