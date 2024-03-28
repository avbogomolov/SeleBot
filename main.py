from selenium import webdriver
import time
import datetime
import random
from selenium.webdriver.common.by import By



# Start of countdown
start_time = time.time()


def random_delay():
    return int(random.randint(1, 30))


def open_site_firefox(site):
    browser = webdriver.Firefox()
    browser.get(site)
    browser.find_element(By.ID, "colophon").click()
    print(f'I found this on {site} the site in the Firefox browser')
    time.sleep(random_delay())
    browser.find_element(By.ID, "menu-item-565").click()
    time.sleep(random_delay())
    browser.find_element(By.ID, "yandex_rtb_R-A-412676-1").location_once_scrolled_into_view
    time.sleep(random_delay())
    browser.quit()


def open_site_chrome(site):
    browser = webdriver.Chrome()
    browser.get(site)
    browser.find_element(By.ID, "colophon").click()
    print(f'I found this on {site} the site in the Google Chrome browser')
    time.sleep(random_delay())
    browser.find_element(By.ID, "menu-item-565").click()
    time.sleep(random_delay())
    browser.find_element(By.ID, "yandex_rtb_R-A-412676-1").location_once_scrolled_into_view
    time.sleep(random_delay())
    browser.quit()


open_site_firefox('https://ironchampion.ru')
open_site_chrome('https://ironchampion.ru')

current_data = datetime.datetime.now().strftime('%m/%d/%Y %H:%M')

# End of countdown
end_time = time.time()

# Calculating execution time
execution_time = round(end_time - start_time, 2)

print(f"Code execution time: {execution_time}")
print(f'Current data is: {current_data}')
